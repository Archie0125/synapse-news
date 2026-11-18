"""FAQ.com.tw article generation through the Anthropic API.

    python -m pipeline.api_daily --mode daily [--date YYYY-MM-DD] [--trial]
    python -m pipeline.api_daily --mode week --week-start YYYY-MM-DD [--until YYYY-MM-DD] [--trial]

Flow: research (Sonnet + web search) -> fetch sources ourselves (robots, caps)
-> write EN+ZH (Opus) -> code gates -> fact check (Sonnet) -> one rewrite if
needed -> write Markdown. Every API call is reserved against a budget before it
is made and recorded in data/api-runs/ledger.json whether it succeeds or not.

If the API cannot be used (429, no credit, spend limit, bad key, or our own cap reached) the run continues
on the owner's Claude subscription through `claude -p`, account claude, then claude2…claude5 as each one
hits its usage limit; the run log's `source` says which was used. FAQ_AUTO_FALLBACK=0 turns that off.

Daily mode refuses to run (unless --trial) after `daily_until` in
data/api-runs/config.json: the owner has to renew it after reviewing traffic.
"""

from __future__ import annotations

import argparse
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from contextlib import contextmanager
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

import anthropic
import frontmatter
import yaml

from pipeline import api_gates as G
from pipeline.api_fetch import Fetcher
from pipeline.ingest.dedup import _normalize_url

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "src" / "content" / "articles"
RUNS = ROOT / "data" / "api-runs"
CACHE_DIR = ROOT / "data" / "api-cache"  # gitignored: source texts are other people's articles
LEDGER = RUNS / "ledger.json"
CONFIG = RUNS / "config.json"
PROMPTS = ROOT / "prompts"
TPE = ZoneInfo("Asia/Taipei")

RESEARCH_MODEL = "claude-sonnet-5-5"
WRITE_MODEL = "claude-opus-5-5"
VERIFY_MODEL = "claude-sonnet-5-5"
# Per-day recap research: Haiku. The owner's 2026-11-11 model eval found search results identical
# across models, and Haiku 5.5 only offers the basic search tool and no server-side fallback.
DAY_RESEARCH_MODEL = "claude-haiku-5-5"
DAY_SEARCH_TOOL = "web_search_20250305"
SEARCH_TOOL = "web_search_20260209"
BETAS = ["server-side-fallback-2026-07-01"]

# USD per million tokens (input, output). A model we did not expect (e.g. a
# refusal fallback) is priced at the top row so the budget errs high.
PRICES = {
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-sonnet-5-5": (2.0, 10.0), "claude-sonnet-5": (2.0, 10.0), "claude-sonnet-4-6": (3.0, 15.0),
    "claude-opus-5-5": (4.0, 20.0), "claude-opus-5": (5.0, 25.0), "claude-opus-4-8": (5.0, 25.0),
    "claude-fable-5-2": (8.0, 40.0), "claude-fable-5-1": (10.0, 50.0), "claude-fable-5": (10.0, 50.0),
}
MAX_PRICE = (10.0, 50.0)
SEARCH_USD = 0.01
# week_total 40 -> 70 and audit_total: owner's 2026-11-13 plan (US$100 for this round).
# 70 -> 120 and 30 -> 90: owner's 2026-11-15 go-ahead (all old articles audited, Jan–Mar recaps; US$150 round).
# fix_total: the correction plan of 2026-11-15, approved by the owner the same night (round cap US$230).
CAPS = {"daily_run": 2.0, "daily_month": 35.0, "week_total": 120.0, "audit_total": 90.0, "fix_total": 150.0}
SOURCE_CHARS = 40_000

AI_NOTE_EN = ("\n\n---\n\n*This article was written by AI from the sources listed on this page. "
              "Figures, names and quotes were checked against those sources by software before publishing.*\n")
AI_NOTE_ZH = "\n\n---\n\n*本文由 AI 依本頁列出的來源撰寫；文中的數字、人名與引言在發佈前已由程式逐一對照來源。*\n"


# ================================================================ budget

class BudgetExceeded(RuntimeError):
    pass


def price_of(model: str) -> tuple[float, float]:
    return PRICES.get(model, MAX_PRICE)


def usage_usd(model: str, usage) -> float:
    if usage is None:
        return 0.0
    pin, pout = price_of(model)
    if model == "claude-haiku-5-5" and (usage.input_tokens or 0) > 100_000:
        pin, pout = 0.50, 2.50  # Haiku 5.5 long-prompt rate
    cache_w = getattr(usage, "cache_creation_input_tokens", 0) or 0
    cache_r = getattr(usage, "cache_read_input_tokens", 0) or 0
    stu = getattr(usage, "server_tool_use", None)
    searches = (getattr(stu, "web_search_requests", 0) or 0) if stu else 0
    return ((usage.input_tokens or 0) * pin + cache_w * pin * 1.25 + cache_r * pin * 0.1
            + (usage.output_tokens or 0) * pout) / 1e6 + searches * SEARCH_USD


class Ledger:
    """Spend record shared by every run (CI and local).

    A call's worst case is written as a pending entry *before* the request, so a
    process killed mid-call still leaves a charge behind; it is replaced by the
    real cost afterwards. A lock file serialises processes, so two runs cannot
    both spend the same headroom or overwrite each other's entries."""

    LOCK_STALE_SECONDS = 600

    def __init__(self, path: Path, mode: str, run_id: str, today: date):
        self.path, self.mode, self.run_id, self.today = path, mode, run_id, today
        self.entries: list[dict] = []
        self._pending: str | None = None
        # Read under the lock: another run may be rewriting the file right now (Codex, 2026-11-15).
        with self._locked(write=False):
            pass

    @contextmanager
    def _locked(self, write: bool = True):
        lock = self.path.with_suffix(".lock")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        deadline = time.monotonic() + 120
        while True:
            try:
                fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                break
            except FileExistsError:
                try:  # a lock this old belongs to a process that died
                    if time.time() - lock.stat().st_mtime > self.LOCK_STALE_SECONDS:
                        lock.unlink()
                        continue
                except FileNotFoundError:
                    continue
                if time.monotonic() > deadline:
                    raise BudgetExceeded("ledger is locked by another run")
                time.sleep(0.2)
        try:
            self.entries = json.loads(self.path.read_text("utf-8")) if self.path.exists() else []
            yield
            if write:
                self.path.write_text(json.dumps(self.entries, ensure_ascii=False, indent=1), "utf-8")
        finally:
            os.close(fd)
            lock.unlink(missing_ok=True)

    def _sum(self, pred) -> float:
        return sum(e["usd"] for e in self.entries if pred(e))

    def run_spent(self) -> float:
        return self._sum(lambda e: e["run"] == self.run_id)

    def month_spent(self) -> float:
        ym = self.today.strftime("%Y-%m")
        return self._sum(lambda e: e["mode"] == "daily" and e["ts"][:7] == ym)

    def week_spent(self) -> float:
        return self._sum(lambda e: e["mode"] == "week")

    def audit_spent(self) -> float:
        return self._sum(lambda e: e["mode"] == "audit")

    def reserve(self, worst_usd: float, step: str) -> None:
        with self._locked():
            if self.mode == "daily":
                if self.run_spent() + worst_usd > CAPS["daily_run"]:
                    raise BudgetExceeded(f"{step}: run would exceed US${CAPS['daily_run']} "
                                         f"(spent {self.run_spent():.2f}, worst case {worst_usd:.2f})")
                if self.month_spent() + worst_usd > CAPS["daily_month"]:
                    raise BudgetExceeded(f"{step}: month would exceed US${CAPS['daily_month']}")
            elif self.mode == "audit":
                if self.audit_spent() + worst_usd > CAPS["audit_total"]:
                    raise BudgetExceeded(f"{step}: audits would exceed US${CAPS['audit_total']} "
                                         f"(spent {self.audit_spent():.2f}, worst case {worst_usd:.2f})")
            elif self.mode == "fix":
                if self._sum(lambda e: e["mode"] == "fix") + worst_usd > CAPS["fix_total"]:
                    raise BudgetExceeded(f"{step}: corrections would exceed US${CAPS['fix_total']}")
            elif self.week_spent() + worst_usd > CAPS["week_total"]:
                raise BudgetExceeded(f"{step}: weekly recaps would exceed US${CAPS['week_total']} "
                                     f"(spent {self.week_spent():.2f}, worst case {worst_usd:.2f})")
            self._pending = uuid.uuid4().hex
            self.entries.append({
                "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), "run": self.run_id,
                "mode": self.mode, "step": step, "model": "", "ok": None, "usd": round(worst_usd, 5),
                "pending": self._pending, "note": "reserved before the call; replaced when it returns",
            })

    def record(self, step: str, model: str, usage, ok: bool, note: str = "",
               usd_override: float | None = None, source: str = "api") -> float:
        usd = usage_usd(model, usage) if usd_override is None else usd_override
        with self._locked():
            if self._pending:
                self.entries = [e for e in self.entries if e.get("pending") != self._pending]
                self._pending = None
            self._append(step, model, usage, ok, note, usd, source)
        return usd

    def _append(self, step: str, model: str, usage, ok: bool, note: str, usd: float, source: str) -> None:
        self.entries.append({
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), "run": self.run_id,
            "mode": self.mode, "step": step, "model": model, "source": source, "ok": ok, "usd": round(usd, 5),
            "input": getattr(usage, "input_tokens", 0) if usage else 0,
            "output": getattr(usage, "output_tokens", 0) if usage else 0,
            "cache_r": (getattr(usage, "cache_read_input_tokens", 0) or 0) if usage else 0,
            "cache_w": (getattr(usage, "cache_creation_input_tokens", 0) or 0) if usage else 0,
            "note": redact(note)[:300],
        })


def est_tokens(text: str) -> int:
    cjk = sum(1 for ch in text if "㐀" <= ch <= "鿿")
    return int((len(text) - cjk) / 3.5 + cjk * 1.2) + 500


def worst_case(model: str, prompt_tokens: int, max_tokens: int, searches: int = 0) -> float:
    pin, pout = (0.50, 2.50) if model == "claude-haiku-5-5" else price_of(model)  # Haiku: long-prompt rate
    pin, pout = pin * 1.5, pout * 1.5  # margin for the character-based token estimate (fallbacks are off)
    # Search results are re-read on every server-side sampling step; x3 covers it.
    search_tokens = searches * 15_000 * 3
    return ((prompt_tokens + search_tokens) * pin + max_tokens * pout) / 1e6 + searches * SEARCH_USD


# ================================================================ API calls

# ---------------------------------------------------------------- subscription fallback
# When the API cannot be used (429, out of credit, spend limit, revoked key, or our own cap reached) the
# rest of the run goes through the owner's logged-in Claude Code accounts instead (owner 2026-11-15
# 「API忽然不能用了 就用訂閱去跑完剩下的」; 2026-11-18: also on 429, across claude～claude5, and say which
# source was used). `claudeN` is the account in ~/.claude-acctN (see ~/bin/claudeN.cmd); `claude` is the
# default ~/.claude. An account that reports a usage limit or a login problem is skipped for the rest
# of the run and the next one takes over.
CLI_ACCOUNTS = "claude,claude2,claude3,claude4,claude5"
CLI_TIMEOUT = 1200
# The CLI's web search has no max_uses; a session searching this many times the API's cap is runaway.
CLI_SEARCH_OVERRUN = 2
API_LIMIT_STATUS = (401, 402, 403, 429)
# Also matched in the body, for errors that arrive inside a 200 stream or with an unexpected status.
API_LIMIT_HINTS = ("credit balance", "insufficient balance", "usage limit", "enforced_spend_limit",
                   "billing_error", "rate_limit_error")
CLI_ACCOUNT_ERRORS = ("authentication_failed", "billing_error", "rate_limit", "oauth_org_not_allowed")
# Word-bounded: "prompt is too long: 214290 tokens" is not a 429 (Fable, 2026-11-18).
CLI_LIMIT_RE = re.compile(r"usage limit|limit reached|hit your limit|rate.?limit|\b429\b|not logged in|/login"
                          r"|authenticat|credit balance|billing", re.I)
_KEY_RE = re.compile(r"sk-ant-[A-Za-z0-9_\-]+")

# Which source served each model call of this run; main() writes it into the run log.
CALLS: list[dict] = []
FALLBACK: dict = {}
_SPENT_ACCOUNTS: set[str] = set()


class AccountUnavailable(RuntimeError):
    """This subscription account cannot take requests now (usage limit, logged out, no access)."""


def redact(text: str) -> str:
    """Error text goes into logs that are committed; never let a key ride along in it."""
    text = _KEY_RE.sub("sk-ant-***", str(text))
    for var in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
        secret = os.environ.get(var)
        if secret and len(secret) >= 8:
            text = text.replace(secret, "***")
    return text


def _note_call(step: str, source: str, ok: bool, why: str = "") -> None:
    CALLS.append({"step": step, "source": source, "ok": ok, **({"why": redact(why)[:200]} if why else {})})


def switch_to_subscription(step: str, reason: str) -> bool:
    """Moves the rest of this process to the subscription. False when the owner turned that off or this
    machine has no Claude Code CLI (e.g. the GitHub runner): then the original error stands."""
    if os.environ.get("FAQ_AUTO_FALLBACK", "1") == "0" or not shutil.which("claude"):
        return False
    reason = redact(reason)
    os.environ["FAQ_BACKEND"] = "cli"
    if not FALLBACK:
        FALLBACK.update(step=step, reason=reason[:300],
                        at=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    print(f"{step}: {reason[:200]}; continuing on the Claude subscription", file=sys.stderr)
    return True


def api_unusable(e: anthropic.APIStatusError) -> bool:
    """Out of quota, out of credit or locked out — not a server error (5xx, 529), whatever its text says."""
    if e.status_code >= 500:
        return False
    if e.status_code in API_LIMIT_STATUS:
        return True
    text = f"{e.message} {getattr(e, 'body', '')}".lower()
    return any(h in text for h in API_LIMIT_HINTS)


def cli_accounts() -> list[tuple[str, str | None]]:
    """(name, CLAUDE_CONFIG_DIR) in the order to try; `FAQ_CLI_ACCOUNTS` overrides the order."""
    out = []
    for name in (n.strip() for n in os.environ.get("FAQ_CLI_ACCOUNTS", CLI_ACCOUNTS).split(",")):
        m = re.fullmatch(r"claude(\d*)", name)
        if not m:
            raise ValueError(f"FAQ_CLI_ACCOUNTS: {name!r} is not claude or claudeN")
        if m.group(1) in ("", "1"):
            out.append((name, None))
        elif (d := Path.home() / f".claude-acct{m.group(1)}").is_dir():
            out.append((name, str(d)))
    return out


def cli_env(config_dir: str | None) -> dict:
    """The child must not see the API key (it would bill the API) or a base URL meant for the SDK."""
    env = {k: v for k, v in os.environ.items()
           if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL", "CLAUDE_CONFIG_DIR")}
    env.update(CLAUDE_CODE_DISABLE_CLAUDE_MDS="1", CLAUDE_CODE_DISABLE_AUTO_MEMORY="1")
    if config_dir:
        env["CLAUDE_CONFIG_DIR"] = config_dir
    return env


def _block_field(b, key: str):
    return b.get(key) if isinstance(b, dict) else getattr(b, key, None)


def cli_prompt(messages: list) -> str:
    """One prompt from the conversation. An earlier assistant turn (a research follow-up) keeps its answer
    and the search results it saw, so the new session can still cite them."""
    parts = []
    for m in messages:
        c = m["content"]
        if isinstance(c, str):
            text = c
        else:
            bits, found = [], []
            for b in c:
                kind = _block_field(b, "type")
                if kind == "text":
                    bits.append(_block_field(b, "text") or "")
                elif kind == "web_search_tool_result" and isinstance(_block_field(b, "content"), list):
                    found += [f"- {_block_field(r, 'title') or ''} — {_block_field(r, 'url')}"
                              for r in _block_field(b, "content") if _block_field(r, "url")]
            if found:
                bits.insert(0, "Search results you already found (you may cite these URLs):\n" + "\n".join(found))
            text = "\n\n".join(bits)
        parts.append(text if m["role"] == "user" else f"[YOUR EARLIER ANSWER]\n{text}")
    return "\n\n".join(parts)


def cli_events(args: list[str], prompt: str, env: dict, timeout: int):
    """Runs `claude -p --output-format stream-json` and yields its events as they arrive, then one
    {"type": "_exit"} event. Streaming lets a usage-limit event stop the call at once instead of the CLI
    waiting hours in its own retry loop. Closing the generator kills the process."""
    errf = tempfile.TemporaryFile("w+", encoding="utf-8")
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=errf, text=True,
                         encoding="utf-8", env=env, cwd=tempfile.gettempdir(), start_new_session=os.name != "nt")
    lines: queue.Queue = queue.Queue()

    def pump():
        # Read on a thread so the deadline below holds even when something the CLI started keeps stdout
        # open after the CLI itself exited: taskkill /T cannot find an orphan's tree (Codex, 2026-11-18).
        try:
            for line in p.stdout:
                lines.put(line)
        except (OSError, ValueError):
            pass
        lines.put(None)

    def feed():
        try:
            p.stdin.write(prompt)
            p.stdin.close()
        except OSError:
            pass

    threading.Thread(target=feed, daemon=True).start()
    threading.Thread(target=pump, daemon=True).start()
    deadline = time.monotonic() + timeout
    try:
        while True:
            remaining = deadline - time.monotonic()  # checked per event: a CLI that never stops talking
            if remaining <= 0:                        # must still time out (Codex, 2026-11-18)
                raise subprocess.TimeoutExpired(args[0], timeout)
            try:
                line = lines.get(timeout=remaining)
            except queue.Empty:
                raise subprocess.TimeoutExpired(args[0], timeout) from None
            if line is None:
                break
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if isinstance(ev, dict):
                yield ev
        try:
            p.wait(timeout=max(0.0, deadline - time.monotonic()))
        except subprocess.TimeoutExpired:
            raise subprocess.TimeoutExpired(args[0], timeout) from None
        errf.seek(0)
        # Masked before any cut: a cut through a key's prefix would leave its tail unrecognisable (Codex)
        yield {"type": "_exit", "rc": p.returncode, "stderr": redact(errf.read())[-400:]}
    finally:
        if p.poll() is None:
            _kill_tree(p)
        errf.close()


def _kill_tree(p: subprocess.Popen) -> None:
    """Kills the CLI and anything it started: a child still holding stdout would keep the read blocked
    after the timeout (Codex, 2026-11-18)."""
    if os.name == "nt":
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)], capture_output=True)
    else:
        import signal
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
    if p.poll() is None:
        p.kill()
    p.wait()


def _reset_text(epoch) -> str:
    try:
        return datetime.fromtimestamp(float(epoch), TPE).strftime("%m-%d %H:%M")
    except (TypeError, ValueError, OverflowError, OSError):
        return "?"


def cli_once(args: list[str], prompt: str, env: dict, schema: dict | None, search_cap: int):
    """One `claude -p` session -> (text, search results [{url, title}], queries).
    Raises AccountUnavailable when the account itself is the problem, RuntimeError otherwise."""
    results: list[dict] = []
    queries: list[str] = []
    searches = 0
    events = cli_events(args, prompt, env, CLI_TIMEOUT)
    try:
        for ev in events:
            kind = ev.get("type")
            if kind == "rate_limit_event":
                info = ev.get("rate_limit_info") or {}
                if info.get("status") == "rejected" and not info.get("isUsingOverage"):
                    raise AccountUnavailable(f"usage limit ({info.get('rateLimitType')}), "
                                             f"resets {_reset_text(info.get('resetsAt'))} Taipei")
            elif kind == "system" and ev.get("subtype") == "api_retry" and ev.get("error_status") in API_LIMIT_STATUS:
                raise AccountUnavailable(f"api_retry {ev.get('error_status')}")
            elif kind == "assistant" and ev.get("error") in CLI_ACCOUNT_ERRORS:
                raise AccountUnavailable(str(ev["error"]))
            elif kind == "user" and isinstance(ev.get("tool_use_result"), dict):
                tur = ev["tool_use_result"]
                if not isinstance(tur.get("results"), list):
                    continue
                n = tur.get("searchCount")
                searches += n if isinstance(n, int) else 1
                if tur.get("query"):
                    queries.append(str(tur["query"]))
                for r in tur["results"]:  # result blocks and the tool's own prose summary (a str) alternate
                    for c in (r.get("content") or []) if isinstance(r, dict) else []:
                        if isinstance(c, dict) and c.get("url"):
                            results.append({"url": c["url"], "title": c.get("title") or ""})
                if search_cap and searches > search_cap:
                    raise RuntimeError(f"searched {searches} times (cap {search_cap})")
            elif kind == "result":
                text = str(ev.get("result") or "")
                if ev.get("is_error"):
                    msg = redact(text or str(ev.get("subtype") or ""))
                    if CLI_LIMIT_RE.search(msg):
                        raise AccountUnavailable(msg[:200])
                    raise RuntimeError(f"error result: {msg[:300]}")
                if schema and ev.get("structured_output") is not None:
                    return json.dumps(ev["structured_output"], ensure_ascii=False), results, queries
                if not text.strip():
                    raise RuntimeError(f"empty result ({ev.get('subtype')})")
                return text, results, queries
            elif kind == "_exit":
                tail = ev.get("stderr") or ""
                if CLI_LIMIT_RE.search(tail):
                    raise AccountUnavailable(tail.strip()[-200:])
                raise RuntimeError(f"no result event (rc={ev.get('rc')}): {tail.strip()[-300:]}")
        raise RuntimeError("no result event")
    finally:
        events.close()


class _CliResponse:
    """The parts of an API response the pipeline reads. Search results come back as the same block types
    the API uses, so research() builds its allowlist from them without a separate path."""
    def __init__(self, text: str, model: str, results: list[dict] = (), queries: list[str] = ()):
        blocks = [SimpleNamespace(type="server_tool_use", name="web_search", input={"query": q}) for q in queries]
        if results:
            blocks.append(SimpleNamespace(type="web_search_tool_result", content=[
                SimpleNamespace(type="web_search_result", url=r["url"], title=r["title"], page_age=None)
                for r in results]))
        blocks.append(SimpleNamespace(type="text", text=text))
        self.content, self.model, self.stop_reason, self.usage = blocks, model, "end_turn", None


def call_model_cli(ledger: Ledger, step: str, model: str, *, system: str, messages: list, effort: str,
                   schema: dict | None, searches: int = 0) -> _CliResponse:
    """Same prompt, model and schema through `claude -p` on the owner's subscription. `searches` > 0 opens
    only the WebSearch tool (no WebFetch: the pipeline fetches sources itself), and source URLs still come
    only from what the search tool returned. Costs US$0; the ledger row says which account served it."""
    prompt = cli_prompt(messages)
    if searches:
        prompt += f"\n\n(You may run at most {searches} web searches.)"
    args = [shutil.which("claude") or "claude", "-p", "--model", model, "--effort", effort,
            "--no-session-persistence", "--strict-mcp-config", "--disable-slash-commands",
            "--setting-sources", "project", "--system-prompt", system,
            "--output-format", "stream-json", "--verbose"]
    args += ["--tools", "WebSearch", "--allowedTools", "WebSearch"] if searches else ["--tools", ""]
    if schema:
        args += ["--json-schema", json.dumps(schema)]
    skipped = []
    for name, config_dir in cli_accounts():
        if name in _SPENT_ACCOUNTS:
            continue
        source = f"subscription:{name}"
        try:
            text, results, queries = cli_once(args, prompt, cli_env(config_dir), schema,
                                              searches * CLI_SEARCH_OVERRUN)
        except AccountUnavailable as e:
            why = redact(str(e))
            _SPENT_ACCOUNTS.add(name)
            skipped.append(f"{name}: {why}")
            ledger.record(step, model, None, ok=False, note=f"{name} unavailable: {why}", usd_override=0.0,
                          source=source)
            _note_call(step, source, False, why)
            print(f"{step}: {name} unavailable ({why}); trying the next account", file=sys.stderr)
            continue
        except (RuntimeError, OSError, subprocess.TimeoutExpired) as e:
            why = redact(f"{type(e).__name__}: {e}")
            ledger.record(step, model, None, ok=False, note=f"{name}: {why}", usd_override=0.0, source=source)
            _note_call(step, source, False, why)
            raise RuntimeError(f"{step}: claude -p ({name}) failed: {why[:300]}") from e
        ledger.record(step, model, None, ok=True, note=f"served by {name}", usd_override=0.0, source=source)
        _note_call(step, source, True)
        return _CliResponse(text, model, results, queries)
    raise RuntimeError(f"{step}: no subscription account is available ("
                       + ("; ".join(skipped) or "all already used up this run or none configured") + ")")


def run_source() -> str:
    """The run's model source in one string, for the run log and the summary line."""
    used = []
    for c in CALLS:
        if c["ok"] and c["source"] not in used:
            used.append(c["source"])
    if not used:
        return "none"
    accounts = [s.split(":", 1)[1] for s in used if s.startswith("subscription:")]
    parts = (["api"] if "api" in used else []) + ([f"subscription({','.join(accounts)})"] if accounts else [])
    return " -> ".join(parts)


def call_model(client, ledger: Ledger, step: str, model: str, *, system: str, messages: list,
               max_tokens: int, effort: str, schema: dict | None = None, tools: list | None = None,
               searches: int = 0, fallbacks: bool = False):
    search = searches if tools else 0
    if tools and any(t.get("name") != "web_search" for t in tools):
        raise ValueError(f"{step}: only the web_search tool has a subscription equivalent")
    if os.environ.get("FAQ_BACKEND") == "cli":
        return call_model_cli(ledger, step, model, system=system, messages=messages, effort=effort,
                              schema=schema, searches=search)
    prompt_tokens = est_tokens(system + json.dumps(messages, ensure_ascii=False, default=str))
    worst = worst_case(model, prompt_tokens, max_tokens, searches)
    try:
        ledger.reserve(worst, step)
    except BudgetExceeded as e:
        # The daily API cap is reached (not a locked ledger): the subscription costs nothing extra. Only
        # daily: for audit/fix/week batches the cap is the stop signal, not a reason to go on (Fable).
        if (ledger.mode == "daily" and "would exceed" in str(e)
                and switch_to_subscription(step, f"API budget reached: {e}")):
            return call_model_cli(ledger, step, model, system=system, messages=messages, effort=effort,
                                  schema=schema, searches=search)
        raise
    output_config: dict = {"effort": effort}
    if schema:
        output_config["format"] = {"type": "json_schema", "schema": schema}
    kwargs = dict(model=model, max_tokens=max_tokens, system=system, messages=messages,
                  output_config=output_config)
    if fallbacks:
        kwargs.update(betas=BETAS, fallbacks="default")
    if tools:
        kwargs["tools"] = tools
    try:
        if max_tokens > 20_000:  # long outputs must stream or the SDK refuses / times out
            with client.beta.messages.stream(**kwargs) as stream:
                resp = stream.get_final_message()
        else:
            resp = client.beta.messages.create(**kwargs)
    except anthropic.APIStatusError as e:
        ledger.record(step, model, None, ok=False, note=redact(f"{e.status_code}: {e.message}"))
        _note_call(step, "api", False, f"{e.status_code}: {e.message}")
        if api_unusable(e) and switch_to_subscription(step, f"API {e.status_code}: {e.message}"):
            return call_model_cli(ledger, step, model, system=system, messages=messages, effort=effort,
                                  schema=schema, searches=search)
        raise
    except anthropic.APIError as e:
        # Timeout / dropped connection / broken stream: we cannot know what was billed,
        # so book the whole reservation.
        ledger.record(step, model, None, ok=False, note=f"{type(e).__name__}: booked worst case",
                      usd_override=worst)
        _note_call(step, "api", False, type(e).__name__)
        raise
    served = resp.model or model
    billed = served if price_of(served)[0] >= price_of(model)[0] else model
    ledger.record(step, billed, resp.usage, ok=resp.stop_reason not in ("refusal", "max_tokens"),
                  note=f"stop={resp.stop_reason} served_by={served}")
    _note_call(step, "api", True)
    return resp


def last_json(resp) -> dict:
    texts = [b.text for b in resp.content if getattr(b, "type", "") == "text"]
    if not texts:
        raise ValueError(f"no text block (stop_reason={resp.stop_reason})")
    raw = texts[-1].strip()
    m = re.search(r"\{.*\}", raw, re.S)
    return json.loads(m.group(0) if m else raw)


# ================================================================ articles on disk

def load_articles() -> list[dict]:
    out = []
    for p in sorted(ARTICLES.glob("*.md")):
        meta = frontmatter.load(p).metadata
        pub = meta.get("publishedAt")
        if isinstance(pub, datetime):
            pub = pub.date()
        elif isinstance(pub, str):
            pub = date.fromisoformat(pub[:10])
        out.append({
            "slug": p.stem, "title": meta.get("title", ""), "lang": meta.get("lang", "en"),
            "tags": meta.get("tags", []) or [], "date": pub, "category": meta.get("category"),
            "sources": [s.get("url", "") for s in meta.get("sources", []) or []],
        })
    return out


def recent_en(articles: list[dict], n: int) -> list[dict]:
    en = [a for a in articles if a["lang"] == "en" and a["date"]]
    return sorted(en, key=lambda a: (a["date"], a["slug"]), reverse=True)[:n]


def write_pair(d: dict, sources: list[dict], *, slug_base: str, published: datetime, kind: str,
               articles: list[dict], head_note_en: str = "", head_note_zh: str = "",
               title_prefix_en: str = "", title_prefix_zh: str = "", overwrite: bool = False) -> list[Path]:
    texts = render_pair(d, sources, published=published, kind=kind, articles=articles, head_note_en=head_note_en,
                        head_note_zh=head_note_zh, title_prefix_en=title_prefix_en, title_prefix_zh=title_prefix_zh)
    paths = []
    for lang, text in texts.items():
        path = ARTICLES / f"{slug_base}-{lang}.md"
        if path.exists() and not overwrite:
            raise FileExistsError(path)
        path.write_text(text, "utf-8")
        paths.append(path)
    return paths


def render_pair(d: dict, sources: list[dict], *, published: datetime, kind: str, articles: list[dict],
                head_note_en: str = "", head_note_zh: str = "", title_prefix_en: str = "",
                title_prefix_zh: str = "") -> dict[str, str]:
    slugs = {a["slug"] for a in articles}
    out = {}
    for lang in ("en", "zh"):
        related = []
        for s in d.get("related_slugs", [])[:3]:
            cand = re.sub(r"-en$", f"-{lang}", s)
            if cand in slugs:
                related.append(cand)
        fm = {
            "title": ((title_prefix_en if lang == "en" else title_prefix_zh)
                      + G.strip_tags(d[f"title_{lang}"])),
            "summary": G.strip_tags(d[f"summary_{lang}"]),
            "category": d["category"],
            "publishedAt": published.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "lang": lang,
            "type": kind,
            "featured": False,
            "trending": False,
            "sources": [{"name": s["site"] or urlparse(s["url"]).netloc.removeprefix("www."), "url": s["url"]}
                        for s in sources],
            "tags": d["tags"],
            "relatedSlugs": related,
        }
        if len(fm["title"]) > 120:  # the gate allows for the prefix; never truncate checked text
            raise RuntimeError(f"title over 120 characters after prefix: {fm['title']!r}")
        note = head_note_en if lang == "en" else head_note_zh
        body = ((note + "\n\n" if note else "") + G.strip_tags(d[f"body_{lang}"]).strip()
                + (AI_NOTE_EN if lang == "en" else AI_NOTE_ZH))
        out[lang] = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n\n" + body
    return out


def assert_unedited(spec: dict, sources: list[dict], articles: list[dict]) -> None:
    """Patch and addday rebuild an article from the cached draft and overwrite it.
    If someone edited the published file by hand since, that edit would be lost,
    so refuse instead (Fable, Codex review)."""
    expected = render_pair(spec["draft"], sources, published=datetime.fromisoformat(spec["published"]),
                           kind=spec["kind"], articles=articles, head_note_en=spec.get("head_note_en", ""),
                           head_note_zh=spec.get("head_note_zh", ""), title_prefix_en=spec.get("title_prefix_en", ""),
                           title_prefix_zh=spec.get("title_prefix_zh", ""))
    for lang, text in expected.items():
        path = ARTICLES / f"{spec['slug_base']}-{lang}.md"
        if path.exists() and path.read_text("utf-8") != text:
            raise RuntimeError(f"{path.name} was changed outside the pipeline; not overwriting it")


# ================================================================ schemas

CAT_ENUM = sorted(G.CATEGORIES)

RESEARCH_DAILY_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["candidates"],
    "properties": {"candidates": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "required": ["headline", "category", "why", "entities", "source_urls"],
        "properties": {
            "headline": {"type": "string"}, "category": {"type": "string", "enum": CAT_ENUM},
            "why": {"type": "string"}, "entities": {"type": "array", "items": {"type": "string"}},
            "source_urls": {"type": "array", "items": {"type": "string"}},
        }}}},
}

RESEARCH_WEEK_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["days"],
    "properties": {"days": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["date", "items"],
        "properties": {
            "date": {"type": "string"},
            "items": {"type": "array", "items": {
                "type": "object", "additionalProperties": False,
                "required": ["event_date", "headline", "category", "source_urls"],
                "properties": {
                    "event_date": {"type": "string"}, "headline": {"type": "string"},
                    "category": {"type": "string", "enum": CAT_ENUM},
                    "source_urls": {"type": "array", "items": {"type": "string"}},
                }}},
        }}}},
}

RESEARCH_DAY_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["items"],
    "properties": {"items": RESEARCH_WEEK_SCHEMA["properties"]["days"]["items"]["properties"]["items"]},
}

WRITE_SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["title_en", "summary_en", "body_en", "title_zh", "summary_zh", "body_zh",
                 "category", "tags", "slug", "related_slugs", "zh_quotes"],
    "properties": {
        "title_en": {"type": "string"}, "summary_en": {"type": "string"}, "body_en": {"type": "string"},
        "title_zh": {"type": "string"}, "summary_zh": {"type": "string"}, "body_zh": {"type": "string"},
        "category": {"type": "string", "enum": CAT_ENUM},
        "tags": {"type": "array", "items": {"type": "string"}},
        "slug": {"type": "string"},
        "related_slugs": {"type": "array", "items": {"type": "string"}},
        "zh_quotes": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["zh", "original"],
            "properties": {"zh": {"type": "string"}, "original": {"type": "string"}}}},
    },
}

VERIFY_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["verdicts"],
    "properties": {"verdicts": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["id", "verdict", "problem"],
        "properties": {"id": {"type": "integer"},
                       "verdict": {"type": "string", "enum": ["supported", "opinion", "unsupported", "distorted"]},
                       "problem": {"type": "string"}}}}},
}


# ================================================================ steps

def research(client, ledger: Ledger, log: dict, user: str, schema: dict, max_uses: int,
             complaint=None, model: str = RESEARCH_MODEL, tool: str = SEARCH_TOOL,
             step: str = "research") -> tuple[dict, dict]:
    """Returns (parsed JSON, allowlist {normalized url: {url,title,page_age}}).

    `complaint(data, allow) -> str | None` inspects a finished answer; if it
    returns text, the model is asked once, in the same conversation, to search
    more and answer again."""
    system = (PROMPTS / "api_research.md").read_text("utf-8")
    tools = [{"type": tool, "name": "web_search", "max_uses": max_uses}]
    messages = [{"role": "user", "content": user}]
    allow: dict[str, dict] = {}
    queries: list[str] = []
    block_types: dict[str, int] = {}
    use_schema: dict | None = schema
    resp = None
    data: dict | None = None
    followed_up = False
    for turn in range(6):
        try:
            resp = call_model(client, ledger, f"{step}#{turn}", model, system=system,
                              messages=messages, max_tokens=12_000, effort="medium", schema=use_schema,
                              tools=tools, searches=max_uses)
        except anthropic.BadRequestError as e:
            if use_schema is None or "format" not in str(e).lower():
                raise
            # Structured output not accepted together with web search: ask for JSON in text instead.
            log.setdefault("notes", []).append(f"research: schema rejected with search ({redact(e.message)[:160]})")
            use_schema = None
            messages[0]["content"] = user + "\n\nReturn the JSON object matching this schema:\n" + json.dumps(schema)
            continue
        for b in resp.content:
            t = getattr(b, "type", "?")
            block_types[t] = block_types.get(t, 0) + 1
            if t == "server_tool_use" and isinstance(getattr(b, "input", None), dict):
                if b.input.get("query"):
                    queries.append(b.input["query"])
            if t == "web_search_tool_result" and isinstance(getattr(b, "content", None), list):
                for r in b.content:
                    url = getattr(r, "url", None)
                    if url:
                        allow[_normalize_url(url)] = {"url": url, "title": getattr(r, "title", ""),
                                                      "page_age": getattr(r, "page_age", None)}
        if resp.stop_reason == "pause_turn":
            messages = messages + [{"role": "assistant", "content": resp.content}]
            continue
        if resp.stop_reason != "end_turn":
            break
        data = last_json(resp)
        problem = complaint(data, allow) if complaint else None
        if problem and not followed_up:
            followed_up = True
            log.setdefault("notes", []).append(f"research follow-up: {problem}")
            messages = messages + [{"role": "assistant", "content": resp.content},
                                   {"role": "user", "content": problem + " Search more, then return the "
                                    "complete JSON object again."}]
            continue
        break
    log["research"] = {"queries": queries, "results": len(allow), "block_types": block_types,
                       "stop_reason": resp.stop_reason if resp else None}
    if data is None:
        raise RuntimeError(f"research did not finish (stop_reason={resp.stop_reason if resp else None})")
    if not allow:
        raise RuntimeError("research returned no web_search_tool_result URLs; cannot build the allowlist "
                           f"(block types seen: {block_types})")
    return data, allow


def daily_complaint(data: dict, allow: dict) -> str | None:
    usable = 0
    notes = []
    for c in data.get("candidates", []):
        urls = [u for u in c.get("source_urls", []) if _normalize_url(u) in allow]
        domains = {urlparse(u).netloc.lower().removeprefix("www.") for u in urls}
        if len(domains) >= 2:
            usable += 1
        else:
            notes.append(f"\"{c.get('headline', '?')}\" has {len(domains)} outlet(s) from your search results")
    if usable >= 3:
        return None
    return (f"Only {usable} of your candidates have source URLs from two different outlets that appeared in "
            f"your search results; I need 3. " + "; ".join(notes) + ".")


def day_complaint(day: date):
    def check(data: dict, allow: dict) -> str | None:
        items = data.get("items", [])
        if not items:
            return (f"You returned nothing for {day.isoformat()}. Search once more with different wording and the "
                    f"date (e.g. \"{day:%B} {day.day} {day.year} AI announcement\"); return an empty list only if "
                    "there is really nothing.")
        thin = [it.get("headline", "?") for it in items
                if len({urlparse(u).netloc for u in it.get("source_urls", []) if _normalize_url(u) in allow}) < 2]
        if thin:
            return ("These items need source URLs from at least two different outlets that appeared in your "
                    "search results: " + "; ".join(thin) + ".")
        return None
    return check


def week_complaint(days: list[date]):
    def check(data: dict, allow: dict) -> str | None:
        got = {x.get("date") for x in data.get("days", [])}
        missing = [d.isoformat() for d in days if d.isoformat() not in got]
        empty = [x.get("date") for x in data.get("days", []) if not x.get("items")]
        missing += [f"{e} (returned empty — search that date specifically)" for e in empty]
        thin = []
        for x in data.get("days", []):
            for it in x.get("items", []):
                urls = [u for u in it.get("source_urls", []) if _normalize_url(u) in allow]
                if len({urlparse(u).netloc for u in urls}) < 2:
                    thin.append(f"{x.get('date')}: \"{it.get('headline', '?')}\"")
        if not missing and not thin:
            return None
        msg = []
        if missing:
            msg.append("These days have no items yet: " + ", ".join(missing) + ". Run a search for each of "
                       "them with the date in the query; weekends can stay empty if nothing solid turns up.")
        if thin:
            msg.append("These items lack two outlets from your search results: " + "; ".join(thin) + ".")
        return " ".join(msg)
    return check


def source_block(i: int, s: dict) -> str:
    when = s["date"].isoformat() if s["date"] else "date unknown"
    text = s["text"][:SOURCE_CHARS]
    return f"[S{i}] {s['site'] or urlparse(s['url']).netloc} — {s['title']} — published {when} — {s['url']}\n{text}"


def with_sources(sources: list[dict], rest: str) -> list[dict]:
    """A user message whose first block is the source texts, marked for prompt
    caching. Fix rounds and verify rounds resend the same sources with the same
    system prompt, so every round after the first reads them at cache price."""
    return [{"role": "user", "content": [
        {"type": "text", "text": "SOURCES:\n\n" + "\n\n".join(source_block(i + 1, s) for i, s in enumerate(sources)),
         "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": rest},
    ]}]


def write(client, ledger: Ledger, step: str, brief: str, sources: list[dict],
          previous: dict | None = None, failures: list[str] | None = None,
          max_tokens: int = 20_000) -> dict:
    system = (PROMPTS / "api_write.md").read_text("utf-8")
    parts = [brief]
    if previous is not None:
        parts.append("YOUR PREVIOUS DRAFT (JSON):\n" + json.dumps(previous, ensure_ascii=False))
        parts.append("It was rejected for these reasons. Fix every one of them — remove or correct the "
                     "offending text; do not argue with the check — keep everything else, and return the "
                     "full JSON again:\n- " + "\n- ".join(failures or []))
    resp = call_model(client, ledger, step, WRITE_MODEL, system=system,
                      messages=with_sources(sources, "\n\n".join(parts)),
                      max_tokens=max_tokens, effort="high", schema=WRITE_SCHEMA)
    if resp.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"{step}: writer stopped with {resp.stop_reason}")
    return last_json(resp)


TEXT_FIELDS = ["title_en", "summary_en", "body_en", "title_zh", "summary_zh", "body_zh"]

FIX_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["edits"],
    "properties": {"edits": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["field", "old", "new"],
        "properties": {"field": {"type": "string", "enum": TEXT_FIELDS},
                       "old": {"type": "string"}, "new": {"type": "string"}}}}},
}


def fix(client, ledger: Ledger, step: str, d: dict, sources: list[dict], failures: list[str]) -> list[dict]:
    system = (PROMPTS / "api_write.md").read_text("utf-8")
    article = {k: d[k] for k in TEXT_FIELDS}
    user = ("ARTICLE (JSON):\n" + json.dumps(article, ensure_ascii=False)
            + "\n\nA checker rejected these parts of the article:\n- " + "\n- ".join(failures)
            + "\n\nReturn edits that fix every problem and change nothing else. Each edit names a field, "
              "`old` = an exact substring copied character-for-character from that field (normally the whole "
              "offending sentence; it must occur exactly once), and `new` = the corrected sentence using only "
              "facts the sources state, or an empty string to delete it. Fix the English and the Chinese "
              "versions of the same claim. Prefer deleting the sentence, or replacing it with a fact a source "
              "states plainly, written in your own words (never 12 or more consecutive words copied from a "
              "source); never replace it with a new interpretation, cause or characterisation. Keep "
              "[S#] source markers on every factual sentence you write, pointing at the source that says it. "
              "Do not touch anything that was not flagged.")
    resp = call_model(client, ledger, step, WRITE_MODEL, system=system,
                      messages=with_sources(sources, user),
                      max_tokens=16_000, effort="medium", schema=FIX_SCHEMA)
    if resp.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"{step}: fixer stopped with {resp.stop_reason}")
    return last_json(resp)["edits"]


def verify(client, ledger: Ledger, step: str, d: dict, sources: list[dict]) -> list[str]:
    """Sentence-by-sentence check: the checker must return a verdict for every
    numbered unit; a unit it skips counts as a failure, so it cannot skim."""
    system = (PROMPTS / "api_verify.md").read_text("utf-8")
    units = G.sentences_for_review(d)
    quotes = json.dumps(d.get("zh_quotes", []), ensure_ascii=False)
    head = (f"CHINESE QUOTATIONS AND THEIR ORIGINALS: {quotes}"
            + "\n\nUNITS TO CHECK (id, language, section heading it sits under, sources it cites, text):\n")
    verdicts: dict[int, dict] = {}
    for round_no in (1, 2):  # second round only for units the first answer skipped
        todo = [u for u in units if u["id"] not in verdicts]
        if not todo:
            break
        user = head + "\n".join(f"{u['id']}. [{u['lang']}] [{u['where']}] [sources: {u['sources']}] {u['text']}"
                                for u in todo)
        resp = call_model(client, ledger, f"{step}.{round_no}", VERIFY_MODEL, system=system,
                          messages=with_sources(sources, user),
                          max_tokens=32_000, effort="high", schema=VERIFY_SCHEMA)
        if resp.stop_reason in ("refusal", "max_tokens"):
            raise RuntimeError(f"{step}: verifier stopped with {resp.stop_reason}")
        asked = {u["id"] for u in todo}
        verdicts.update({v["id"]: v for v in last_json(resp)["verdicts"] if v["id"] in asked})
    fails = []
    for u in units:
        v = verdicts.get(u["id"])
        if v is None:
            fails.append(f"fact-check ({u['lang']}): unit {u['id']} was not checked: \"{u['text'][:160]}\"")
        elif v["verdict"] in ("unsupported", "distorted"):
            fails.append(f"fact-check ({u['lang']}, {v['verdict']}): \"{u['text']}\" — {v['problem']}")
    return fails


def gates(d: dict, sources: list[dict], extra_pool: list[str], articles: list[dict], run_date: date,
          mode: str, en_words: tuple[int, int], zh_chars: tuple[int, int]) -> list[str]:
    src = [s["text"] for s in sources]
    pool = src + extra_pool
    en_all = "\n".join([d["title_en"], d["summary_en"], d["body_en"]])
    zh_all = "\n".join([d["title_zh"], d["summary_zh"], d["body_zh"]])
    en_prose = "\n".join([d["summary_en"], d["body_en"]])  # titles are Title Case: skip the name check
    related_ok = {a["slug"] for a in articles if a["lang"] == "en"}
    max_title = (88, 100) if mode == "week" else (120, 120)  # week titles get a date prefix
    fails = G.check_format(d, en_words, zh_chars, related_ok, max_title)
    fails += G.check_citations(d["body_en"], len(sources), "en")
    fails += G.check_citations(d["body_zh"], len(sources), "zh")
    fails += G.check_numbers(en_all, pool, "en")
    fails += G.check_numbers(zh_all, pool + [en_all], "zh")
    fails += G.check_quotes_en(en_all, src, "en")
    fails += G.check_quotes_zh(zh_all, d.get("zh_quotes", []), src)
    fails += G.check_names(en_prose, pool + [s["site"] for s in sources] + [s["title"] for s in sources])
    fails += G.check_copy_en(en_all, src, "en")
    fails += G.check_copy_zh(zh_all, src)
    urls = [s["url"] for s in sources]
    if mode == "daily":
        fails += G.check_duplicate(d["title_en"], d["title_zh"], d["tags"], urls, articles, run_date)
    else:
        used = {_normalize_url(u) for a in articles for u in a["sources"]}
        fails += [f"duplicate: source {u} already used by an earlier article" for u in urls
                  if _normalize_url(u) in used]
    return fails


def date_words(days: list[date]) -> list[str]:
    """Calendar facts the article may state without a source saying them (the
    run date, the recap's days, the sources' own publication dates)."""
    out = []
    for d in days:
        out.append(f"{d.isoformat()} {d:%B} {d.day}, {d.year} {d.month}月{d.day}日 {d.month}/{d.day} {d:%A}")
    return out


def draft_until_clean(client, ledger, log, brief, sources, extra_pool, articles, run_date, mode,
                      en_words, zh_chars, tag: str, start: dict | None = None) -> dict | None:
    cache = log.setdefault("_cache", {"sources": {}, "drafts": []})
    for s in sources:
        cache["sources"][s["url"]] = {k: s[k] for k in ("url", "final_url", "site", "title", "date", "text")}
    write_tokens = 48_000 if mode == "week" else 24_000
    d = start if start is not None else write(client, ledger, f"write:{tag}#1", brief, sources,
                                              max_tokens=write_tokens)
    for attempt in (1, 2, 3, 4):
        fails = gates(d, sources, extra_pool, articles, run_date, mode, en_words, zh_chars)
        if not fails:
            fails = verify(client, ledger, f"verify:{tag}#{attempt}", d, sources)
        log.setdefault("attempts", []).append({"candidate": tag, "attempt": attempt, "failures": fails,
                                               "title_en": d.get("title_en")})
        cache["drafts"].append({"candidate": tag, "attempt": attempt, "draft": d, "failures": fails})
        if not fails:
            return d
        if attempt == 4:
            break
        if any(f.startswith(("format:", "duplicate:")) for f in fails):
            d = write(client, ledger, f"write:{tag}#{attempt + 1}", brief, sources, previous=d, failures=fails,
                      max_tokens=write_tokens)
        else:
            # Sentence-level problems: patch only the named sentences, so a rewrite
            # cannot introduce fresh errors elsewhere.
            edits = fix(client, ledger, f"fix:{tag}#{attempt}", d, sources, fails)
            d, edit_errors = G.apply_edits(d, edits)
            cache["drafts"][-1]["edits"] = edits
            if edit_errors:
                log.setdefault("notes", []).append(f"{tag}: {edit_errors}")
    return None


# ================================================================ modes

def run_daily(client, fetcher: Fetcher, ledger: Ledger, log: dict, run_date: date) -> list[Path]:
    articles = load_articles()
    recent = recent_en(articles, 60)
    covered = "\n".join(f"- {a['date']} {a['title']} [tags: {', '.join(a['tags'][:6])}]" for a in recent)
    hints_path = ROOT / "data" / "analytics" / "hints.json"
    hints = hints_path.read_text("utf-8") if hints_path.exists() else ""
    user = (f"Today is {run_date.isoformat()} (Asia/Taipei). Find stories from {run_date - timedelta(days=2)} "
            f"to {run_date}. Return exactly 3 candidates, best first, each with 2–4 source URLs from different "
            f"outlets.\n\nAlready covered (most recent first):\n{covered}\n")
    if hints:
        user += ("\nWhat readers searched for recently (from Search Console / Bing / GA4). When two "
                 "stories are equally newsworthy, prefer the one these readers would look for:\n" + hints)
    data, allow = research(client, ledger, log, user, RESEARCH_DAILY_SCHEMA, max_uses=10,
                           complaint=daily_complaint)
    log["candidates"] = data.get("candidates", [])
    related = "\n".join(f"- {a['slug']}: {a['title']}" for a in recent[:40])

    for idx, cand in enumerate(data.get("candidates", [])[:3], start=1):
        tag = f"c{idx}"
        urls = [u for u in cand["source_urls"] if _normalize_url(u) in allow]
        dropped = [u for u in cand["source_urls"] if _normalize_url(u) not in allow]
        clog = {"candidate": tag, "headline": cand["headline"], "not_in_search_results": dropped}
        log.setdefault("candidate_checks", []).append(clog)
        # Cheap pre-check before spending on fetch/write: same sources, same headline or same entities lately.
        early = G.check_duplicate(cand["headline"], "", cand.get("entities", []), urls, articles, run_date)
        if early:
            clog["skipped"] = early
            continue
        fetched = [fetcher.fetch(u) for u in urls]
        clog["fetch"] = [{"url": f["url"], "ok": f["ok"], "reason": f["reason"], "words": f["words"],
                          "date": f["date"].isoformat() if f["date"] else None} for f in fetched]
        good = [f for f in fetched if f["ok"]]
        pre = (G.check_sources(good, set(allow), min_total_words=900)
               + G.fresh_daily([f["date"] for f in good], run_date))
        if pre:
            clog["skipped"] = pre
            continue
        brief = (f"ARTICLE TYPE: daily news commentary for {run_date.isoformat()}.\n"
                 f"STORY: {cand['headline']}\nWHY IT MATTERS (researcher's note, not a source): {cand['why']}\n"
                 f"LENGTH: English 450–1,100 words; Chinese 700–2,400 characters.\n"
                 f"CATEGORY: one of {', '.join(CAT_ENUM)}.\n"
                 "TAGS: 3–8 short tags; put the main companies/products first.\n"
                 "SLUG: 2–8 lowercase English words joined by hyphens, no date.\n"
                 "RELATED: pick up to 3 slugs from this list that a reader of this story would want next, "
                 f"or none:\n{related}\n"
                 "Return JSON with: title_en, summary_en (one sentence), body_en (Markdown), title_zh, "
                 "summary_zh, body_zh, category, tags, slug, related_slugs, zh_quotes.")
        extra = date_words([run_date] + [f["date"] for f in good if f["date"]])
        d = draft_until_clean(client, ledger, log, brief, good, extra, articles, run_date, "daily",
                              (450, 1100), (700, 2400), tag)
        if d is None:
            clog["skipped"] = ["failed gates after one rewrite"]
            continue
        published = datetime.now(timezone.utc).replace(microsecond=0)
        spec = {"mode": "daily", "slug_base": f"{run_date.isoformat()}-{d['slug']}", "kind": "news",
                "published": published.isoformat(), "run_date": run_date.isoformat(),
                "en_words": [450, 1100], "zh_chars": [700, 2400], "extra_pool": extra,
                "source_urls": [s["url"] for s in good], "draft": d}
        log["_cache"]["publish"] = spec
        paths = publish_spec(spec, good, articles)
        log["published"] = [p.name for p in paths]
        return paths
    raise RuntimeError("no candidate passed the checks today; nothing published")


# Orders recaps written on the same day by the week they cover (5 minutes apart). The Monday of the
# first 2026 week, so the January–March recaps also land after midnight of the day they were written.
GAP_START = date(2025, 12, 29)


class CachedFetcher:
    """Replays the source texts a failed recap run fetched, so resuming it keeps the
    same [S#] numbering and asks no site again. URLs that run did not use come back
    as not fetched, which leaves their items out exactly as before."""

    def __init__(self, cached: dict):
        self.cached = cached

    def fetch(self, url: str) -> dict:
        s = self.cached.get(url)
        if s is None:
            return {"url": url, "final_url": url, "ok": False, "reason": "not used by the resumed run",
                    "text": "", "words": 0, "date": None, "title": "", "site": ""}
        return {**s, "ok": True, "reason": "", "words": len(s["text"].split()),
                "date": date.fromisoformat(s["date"]) if s.get("date") else None}


def run_week(client, fetcher: Fetcher, ledger: Ledger, log: dict, week_start: date, until: date,
             write_date: date, resume: dict | None = None) -> list[Path]:
    """`resume`: the cache of an earlier run of this week that failed its checks;
    its sources are replayed and its last draft is fixed instead of rewritten."""
    if resume is not None:
        fetcher = CachedFetcher(resume["sources"])
    articles = load_articles()
    days = [week_start + timedelta(days=i) for i in range((until - week_start).days + 1)]
    # One cheap research call per day (a single call for the whole week returned
    # anywhere from 3 to 8 items). Each day's result is cached, so a rerun after a
    # gate or prompt fix does not pay for the searches again.
    data: dict = {"days": []}
    allow: dict = {}
    queries: list[str] = []
    for day in days:
        rcache = CACHE_DIR / f"research-day-{day.isoformat()}.json"
        if rcache.exists():
            saved = json.loads(rcache.read_text("utf-8"))
        else:
            user = (f"Find the 1–2 most important AI and technology news items first reported on "
                    f"{day:%A}, {day:%B} {day.day}, {day.year} ({day.isoformat()}). Put the date in your search "
                    "queries. For each item give the day it happened, a one-line headline, a category and 2–4 "
                    "source URLs from different outlets that appeared in your search results; include the "
                    "company's or agency's own announcement page whenever one exists. If nothing solid was "
                    "reported that day, return an empty list.")
            dlog: dict = {}
            day_data, day_allow = research(client, ledger, dlog, user, RESEARCH_DAY_SCHEMA, max_uses=4,
                                           complaint=day_complaint(day), model=DAY_RESEARCH_MODEL,
                                           tool=DAY_SEARCH_TOOL, step=f"research:{day.isoformat()}")
            saved = {"data": day_data, "allow": day_allow, "queries": dlog["research"]["queries"]}
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            rcache.write_text(json.dumps(saved, ensure_ascii=False, default=str), "utf-8")
        data["days"].append({"date": day.isoformat(), "items": saved["data"].get("items", [])})
        allow.update(saved["allow"])
        queries += saved["queries"]
    log["research"] = {"queries": queries, "results": len(allow)}

    kept: list[dict] = []
    seen_urls: set[str] = set()
    # A source an earlier article already cites fails the duplicate gate and no rewrite can drop it, so it is
    # left out here (2026-11-15: four Jan–Mar weeks failed four times on one such source each).
    used = {_normalize_url(u) for a in articles for u in a["sources"]}
    for entry in data.get("days", []):
        for it in entry.get("items", [])[:2]:
            try:
                ev = date.fromisoformat(it["event_date"][:10])
            except ValueError:
                continue
            urls = [u for u in it["source_urls"] if _normalize_url(u) in allow and u not in seen_urls
                    and _normalize_url(u) not in used][:3]
            fetched = [fetcher.fetch(u) for u in urls]
            good = [f for f in fetched if f["ok"]]
            fresh = G.item_fresh(ev, [f["date"] for f in good], week_start, until)
            in_week = sorted(f["date"] for f in good if f["date"] and week_start <= f["date"] <= until)
            log.setdefault("items", []).append({
                "listed_under": entry.get("date"), "event_date": ev.isoformat(), "headline": it["headline"],
                "fresh": fresh, "fetch": [{"url": f["url"], "ok": f["ok"], "reason": f["reason"],
                                           "date": f["date"].isoformat() if f["date"] else None} for f in fetched]})
            if good and fresh and in_week:
                seen_urls.update(f["url"] for f in good)
                # File the item under its event date only when a source's text states that
                # date; otherwise under the day its sources first reported it. The model's
                # own "event date" is not evidence by itself.
                stated = week_start <= ev <= until and any(
                    G.source_states_day(f["text"], f["date"], ev) for f in good)
                # Only a source-stated day gets a day heading; anything else goes under
                # "also this week" with the day it was reported.
                kept.append({"day": ev if stated else None, "reported": in_week[0], "headline": it["headline"],
                             "category": it["category"], "sources": good})
    per_day: dict[str, int] = {}
    for it in kept:
        key = (it["day"] or it["reported"]).isoformat()
        per_day[key] = per_day.get(key, 0) + 1
    log["day_status"] = {
        d.isoformat(): (f"{per_day[d.isoformat()]} item(s)" if d.isoformat() in per_day else
                        ("searched, 0 items" if any(G.query_mentions_day(q, d) for q in queries) else "not searched"))
        for d in days}
    if len(kept) < 3:
        raise RuntimeError(f"only {len(kept)} dated, sourced items for {week_start}–{until}; not writing a recap")

    sources: list[dict] = []
    seen = set()
    for it in kept:
        for s in it["sources"]:
            if s["url"] not in seen:
                seen.add(s["url"])
                sources.append(s)
    if resume is not None and [s["url"] for s in sources] != list(resume["sources"]):
        raise RuntimeError("resume: the replayed sources differ from the failed run's; its [S#] markers "
                           "would point at the wrong texts")
    index = {s["url"]: i + 1 for i, s in enumerate(sources)}
    dated, also = [], []
    for it in sorted(kept, key=lambda x: (x["day"] or x["reported"])):
        refs = "".join(f"[S{index[s['url']]}]" for s in it["sources"])
        if it["day"]:
            dated.append(f"- {it['day'].isoformat()} ({it['day']:%A}): {it['headline']} {refs}")
        else:
            also.append(f"- reported {it['reported'].isoformat()}: {it['headline']} {refs}")
    brief = ("ARTICLE TYPE: weekly recap covering "
             f"{week_start.isoformat()} to {until.isoformat()}, written on {write_date.isoformat()}.\n"
             "STRUCTURE: a short opening (2–3 sentences on the week's thread); then one ## section per day for "
             "the DATED ITEMS, in date order, headed like \"## Tuesday, August 4\" (中文：\"## 8 月 4 日（週二）\"); "
             "then, if there are any, \"## Also this week\" (中文：\"## 本週其他消息\") for the OTHER ITEMS, each "
             "saying which day it was reported (\"reported on November 5\"); then \"## What to Watch\" / "
             "\"## 值得關注\". Only cover the items below, only with facts from their sources.\n"
             "DATES: under a day heading, describe only what the sources place on that day. If a source gives "
             "a related development on another day, state that day explicitly (\"On November 6, Google Cloud "
             "...\"), never \"a day later\". Do not invent a day for anything.\n"
             "STYLE: this is a neutral record, not commentary. Report what happened and keep every qualifier "
             "and condition the source gives. Keep opinion to the What to Watch section.\n"
             "DATED ITEMS:\n" + ("\n".join(dated) or "(none)") + "\n"
             "OTHER ITEMS:\n" + ("\n".join(also) or "(none)") + "\n"
             "LENGTH: English 700–2,200 words; Chinese 1,000–3,600 characters.\n"
             "TITLE: a short hook about the week only (the site adds the date range in front).\n"
             f"CATEGORY: one of {', '.join(CAT_ENUM)} (usually ai-ml).\n"
             "TAGS: 3–8 tags, the main companies/products of the week.\n"
             "SLUG: return \"ai-week\" (the site adds the dates).\n"
             "RELATED: return an empty list.\n"
             "Return JSON with: title_en, summary_en (one sentence), body_en, title_zh, summary_zh, body_zh, "
             "category, tags, slug, related_slugs, zh_quotes.")
    extra = date_words(days + [s["date"] for s in sources if s["date"]])
    d = draft_until_clean(client, ledger, log, brief, sources, extra, articles, write_date, "week",
                          (700, 2200), (1000, 3600), f"week-{week_start.isoformat()}",
                          start=resume["drafts"][-1]["draft"] if resume is not None else None)
    if d is None:
        raise RuntimeError("weekly recap failed the checks after 4 attempts")

    rng_en = f"{week_start:%b} {week_start.day}–" + (f"{until.day}" if until.month == week_start.month
                                                      else f"{until:%b} {until.day}") + f", {until.year}"
    rng_zh = f"{week_start.month}/{week_start.day}–{until.month}/{until.day}"
    order = (week_start - GAP_START).days // 7
    published = datetime(write_date.year, write_date.month, write_date.day, tzinfo=timezone.utc) + timedelta(minutes=5 * order)
    spec = {
        "mode": "week", "slug_base": f"{write_date.isoformat()}-ai-week-{week_start.isoformat()}", "kind": "analysis",
        "published": published.isoformat(), "run_date": write_date.isoformat(),
        "en_words": [700, 2200], "zh_chars": [1000, 3600], "extra_pool": extra,
        "source_urls": [s["url"] for s in sources], "draft": d,
        "title_prefix_en": f"AI Week, {rng_en}: ", "title_prefix_zh": f"AI 週報 {rng_zh}：",
        "head_note_en": f"*Written on {write_date:%B} {write_date.day}, {write_date.year}, covering news from {rng_en}.*",
        "head_note_zh": f"*本文於 {write_date.year} 年 {write_date.month} 月 {write_date.day} 日補寫，整理 {rng_zh} 的新聞。*",
    }
    log["_cache"]["publish"] = spec
    paths = publish_spec(spec, sources, articles)
    log["published"] = [p.name for p in paths]
    return paths


def publish_spec(spec: dict, sources: list[dict], articles: list[dict], overwrite: bool = False) -> list[Path]:
    return write_pair(
        spec["draft"], sources, slug_base=spec["slug_base"],
        published=datetime.fromisoformat(spec["published"]), kind=spec["kind"], articles=articles,
        head_note_en=spec.get("head_note_en", ""), head_note_zh=spec.get("head_note_zh", ""),
        title_prefix_en=spec.get("title_prefix_en", ""), title_prefix_zh=spec.get("title_prefix_zh", ""),
        overwrite=overwrite)


def run_patch(client, ledger: Ledger, log: dict, src_run: str, failures: list[str]) -> list[Path]:
    """Fix the sentences an outside checker (e.g. Codex) flagged in an article
    this pipeline already wrote, re-run every gate and the fact check, and
    overwrite the article only if all of it passes."""
    cache_path = CACHE_DIR / f"{src_run}.json"
    cache = json.loads(cache_path.read_text("utf-8"))
    spec = cache["publish"]
    sources = []
    for u in spec["source_urls"]:
        s = dict(cache["sources"][u])
        s["date"] = date.fromisoformat(s["date"]) if s.get("date") else None
        sources.append(s)
    own = {f"{spec['slug_base']}-en", f"{spec['slug_base']}-zh"}
    articles = [a for a in load_articles() if a["slug"] not in own]
    assert_unedited(spec, sources, articles)
    d = spec["draft"]
    for round_no in (1, 2):
        edits = fix(client, ledger, f"patch:fix#{round_no}", d, sources, failures)
        before = d
        d, problems = G.apply_edits(d, edits)
        if d == before:
            raise RuntimeError(f"patch round {round_no}: no edit could be applied ({problems[:3]}); "
                               "the outside checker's findings are still in the article")
        failures = problems + gates(d, sources, spec["extra_pool"], articles, date.fromisoformat(spec["run_date"]),
                                    spec["mode"], tuple(spec["en_words"]), tuple(spec["zh_chars"]))
        if not failures:
            failures = verify(client, ledger, f"patch:verify#{round_no}", d, sources)
        log.setdefault("patch_rounds", []).append({"round": round_no, "edits": edits, "failures": failures})
        if not failures:
            break
    if failures:
        raise RuntimeError(f"patch did not pass after 2 rounds: {failures[:3]}")
    spec["draft"] = d
    cache.setdefault("patches", []).append({"run": log["run"], "draft": d})
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1, default=str), "utf-8")
    # Our own gates and fact check pass, but only the outside checker can say its
    # findings are gone: whoever runs patch must re-run it before publishing.
    log["outside_recheck_required"] = True
    paths = publish_spec(spec, sources, articles, overwrite=True)
    log["published"] = [p.name for p in paths]
    return paths


ADDDAY_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["section_en", "section_zh", "zh_quotes"],
    "properties": {"section_en": {"type": "string"}, "section_zh": {"type": "string"},
                   "zh_quotes": WRITE_SCHEMA["properties"]["zh_quotes"]},
}


def run_addday(client, fetcher: Fetcher, ledger: Ledger, log: dict, src_run: str, day: date) -> list[Path]:
    """Fill a day a published recap left empty: research that day again (Sonnet,
    more searches), and if a source states something happened that day, write only
    that day's section and insert it in date order. Existing sentences are changed
    only if a check flags them. Same source rules as the recap itself."""
    cache_path = CACHE_DIR / f"{src_run}.json"
    cache = json.loads(cache_path.read_text("utf-8"))
    spec = cache["publish"]
    week_start = date.fromisoformat(spec["slug_base"].rsplit("-ai-week-", 1)[1])
    until = min(week_start + timedelta(days=6), date(2026, 11, 12))
    if not week_start <= day <= until:
        raise ValueError(f"{day} is not in the week of {week_start}")
    sources = []
    for u in spec["source_urls"]:
        s = dict(cache["sources"][u])
        s["date"] = date.fromisoformat(s["date"]) if s.get("date") else None
        sources.append(s)
    own = {f"{spec['slug_base']}-en", f"{spec['slug_base']}-zh"}
    articles = [a for a in load_articles() if a["slug"] not in own]
    assert_unedited(spec, sources, articles)
    used = {_normalize_url(a_url) for a in articles for a_url in a["sources"]} | {_normalize_url(s["url"]) for s in sources}

    rcache = CACHE_DIR / f"research-day-sonnet-{day.isoformat()}.json"
    if rcache.exists():
        saved = json.loads(rcache.read_text("utf-8"))
    else:
        covered = "; ".join(s["title"] for s in sources if s.get("title"))
        user = (f"Find the 1–2 most important AI and technology news items first reported on {day:%A}, "
                f"{day:%B} {day.day}, {day.year} ({day.isoformat()}). Put the date in your search queries. For "
                "each item give the day it happened, a one-line headline, a category and 2–4 source URLs from "
                "different outlets that appeared in your search results. Prefer pages anyone can read without a "
                "subscription, and include the company's or agency's own announcement page whenever one exists. "
                f"Skip these stories, they are already covered: {covered}. If nothing solid was reported that "
                "day, return an empty list.")
        dlog: dict = {}
        day_data, day_allow = research(client, ledger, dlog, user, RESEARCH_DAY_SCHEMA, max_uses=8,
                                       complaint=day_complaint(day), step=f"addday-research:{day.isoformat()}")
        saved = {"data": day_data, "allow": day_allow, "queries": dlog["research"]["queries"]}
        rcache.write_text(json.dumps(saved, ensure_ascii=False, default=str), "utf-8")
    log["research"] = {"queries": saved["queries"], "results": len(saved["allow"])}

    kept: list[dict] = []
    for it in saved["data"].get("items", [])[:2]:
        try:
            ev = date.fromisoformat(it["event_date"][:10])
        except ValueError:
            continue
        urls = [u for u in it["source_urls"] if _normalize_url(u) in saved["allow"] and _normalize_url(u) not in used][:3]
        fetched = [fetcher.fetch(u) for u in urls]
        good = [f for f in fetched if f["ok"]]
        fresh = G.item_fresh(ev, [f["date"] for f in good], week_start, until)
        stated = ev == day and any(G.source_states_day(f["text"], f["date"], ev) for f in good)
        reported = any(f["date"] == day for f in good)
        log.setdefault("items", []).append({"event_date": ev.isoformat(), "headline": it["headline"],
                                            "fresh": fresh, "stated": stated, "reported_that_day": reported,
                                            "fetch": [{"url": f["url"], "ok": f["ok"], "reason": f["reason"]} for f in fetched]})
        if good and fresh and (stated or reported):
            used.update(_normalize_url(f["url"]) for f in good)
            kept.append({"headline": it["headline"], "sources": good, "stated": stated})
    if not kept:
        log["day_result"] = "searched, 0 items"
        return []
    # Same rule as the recap: a day heading only for what a source places on that day;
    # a story that was merely reported that day goes under "Also this week".
    as_day = any(it["stated"] for it in kept)
    kept = [it for it in kept if it["stated"]] if as_day else kept

    new_sources = [s for it in kept for s in it["sources"]]
    index = {s["url"]: i + 1 for i, s in enumerate(new_sources)}
    items = "\n".join(f"- {it['headline']} " + "".join(f"[S{index[s['url']]}]" for s in it["sources"]) for it in kept)
    if as_day:
        shape = (f"ONE new day section. HEADINGS: English exactly \"{G.day_heading(day, 'en')}\", Chinese exactly "
                 f"\"{G.day_heading(day, 'zh')}\". Return section_en and section_zh each starting with its heading.\n"
                 f"DATES: describe only what the sources place on {day:%B} {day.day}. If a source gives a related "
                 "development on another day, state that day explicitly. Do not invent a day for anything.\n")
    else:
        shape = ("ONE short paragraph per item for the recap's \"Also this week\" section. No heading. Begin "
                 f"each English paragraph with \"Reported on {day:%B} {day.day}:\" and each Chinese paragraph "
                 f"with \"{day.month} 月 {day.day} 日報導：\". The sources were published that day but do not say "
                 "which day the event itself happened, so never name a day for the event.\n")
    brief = (f"ARTICLE TYPE: an addition to an existing weekly recap of {week_start.isoformat()} to "
             f"{until.isoformat()}: {shape}"
             "This is not an article: no opening, no title, no summary, no What to Watch.\n"
             "STYLE: a neutral record, not commentary; keep every qualifier and condition the source gives; "
             "[S#] markers on every factual sentence, pointing at the sources given here.\n"
             f"ITEMS:\n{items}\n"
             "LENGTH: English 60–250 words; Chinese 120–450 characters.\n"
             "Return JSON with section_en, section_zh and zh_quotes.")
    resp = call_model(client, ledger, f"addday-write:{day.isoformat()}", WRITE_MODEL,
                      system=(PROMPTS / "api_write.md").read_text("utf-8"),
                      messages=with_sources(new_sources, brief), max_tokens=12_000, effort="high",
                      schema=ADDDAY_SCHEMA)
    if resp.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"addday writer stopped with {resp.stop_reason}")
    part = last_json(resp)
    n = len(sources)
    d = dict(spec["draft"])
    if as_day:
        d["body_en"] = G.insert_day_section(d["body_en"], G.shift_markers(part["section_en"], n), day)
        d["body_zh"] = G.insert_day_section(d["body_zh"], G.shift_markers(part["section_zh"], n), day)
    else:
        d["body_en"] = G.insert_also_paragraph(d["body_en"], G.shift_markers(part["section_en"], n), "en")
        d["body_zh"] = G.insert_also_paragraph(d["body_zh"], G.shift_markers(part["section_zh"], n), "zh")
    d["zh_quotes"] = list(d.get("zh_quotes", [])) + list(part.get("zh_quotes", []))
    all_sources = sources + new_sources
    extra = list(spec["extra_pool"]) + date_words([day] + [s["date"] for s in new_sources if s["date"]])
    # The recap grows by one section; its length limits grow by that section's limits.
    en_words = (spec["en_words"][0], spec["en_words"][1] + 250)
    zh_chars = (spec["zh_chars"][0], spec["zh_chars"][1] + 450)
    run_date = date.fromisoformat(spec["run_date"])
    failures = gates(d, all_sources, extra, articles, run_date, "week", en_words, zh_chars)
    if not failures:
        failures = verify(client, ledger, "addday-verify#0", d, all_sources)
    for round_no in (1, 2, 3):
        if not failures:
            break
        edits = fix(client, ledger, f"addday-fix#{round_no}", d, all_sources, failures)
        d, problems = G.apply_edits(d, edits)
        failures = problems + gates(d, all_sources, extra, articles, run_date, "week", en_words, zh_chars)
        if not failures:
            failures = verify(client, ledger, f"addday-verify#{round_no}", d, all_sources)
        log.setdefault("fix_rounds", []).append({"round": round_no, "edits": edits, "failures": failures})
    if failures:
        log["day_result"] = "written but failed the checks; not published"
        raise RuntimeError(f"addday did not pass after 3 fix rounds: {failures[:3]}")
    for s in new_sources:
        cache["sources"][s["url"]] = {k: s[k] for k in ("url", "final_url", "site", "title", "date", "text")}
    spec.update(draft=d, source_urls=[s["url"] for s in all_sources], extra_pool=extra,
                en_words=list(en_words), zh_chars=list(zh_chars))
    cache.setdefault("patches", []).append({"run": log["run"], "added_day": day.isoformat(), "draft": d})
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1, default=str), "utf-8")
    log["day_result"] = f"{len(kept)} item(s) added " + ("as a day section" if as_day else "under Also this week")
    log["outside_recheck_required"] = True
    paths = publish_spec(spec, all_sources, articles, overwrite=True)
    log["published"] = [p.name for p in paths]
    return paths


# ================================================================ main

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mode", choices=["daily", "week", "patch", "addday"], required=True)
    ap.add_argument("--run", help="patch/addday: the run id whose article to change")
    ap.add_argument("--day", help="addday: the empty day to fill")
    ap.add_argument("--failures", help="patch: JSON file with a list of problem strings")
    ap.add_argument("--date", help="daily: the news day (default: today in Asia/Taipei)")
    ap.add_argument("--week-start", help="week: first day covered")
    ap.add_argument("--until", help="week: last day covered (default week-start + 6)")
    ap.add_argument("--trial", action="store_true", help="local trial: skip the daily_until expiry check")
    ap.add_argument("--resume", help="week: id of a failed run of the same week to continue from its last draft")
    a = ap.parse_args(argv)
    if a.mode in ("patch", "addday") and not a.run:
        ap.error(f"--mode {a.mode} needs --run")
    if a.mode == "addday" and not a.day:
        ap.error("--mode addday needs --day")
    if a.mode == "patch" and not a.failures:
        ap.error("--mode patch needs --failures")

    today = datetime.now(TPE).date()
    if a.mode == "daily" and not a.trial:
        cfg = json.loads(CONFIG.read_text("utf-8")) if CONFIG.exists() else {}
        until = cfg.get("daily_until")
        if not until or today > date.fromisoformat(until):
            print(f"daily runs are not enabled (daily_until={until!r}); the owner must renew after "
                  "reviewing Search Console / Bing data", file=sys.stderr)
            return 3

    run_id = f"{today.isoformat()}-{a.mode}-{uuid.uuid4().hex[:6]}"
    budget_mode = a.mode
    if a.mode in ("patch", "addday"):
        budget_mode = json.loads((CACHE_DIR / f"{a.run}.json").read_text("utf-8"))["publish"]["mode"]
    ledger = Ledger(LEDGER, budget_mode, run_id, today)
    log: dict = {"run": run_id, "mode": a.mode, "started": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    client = anthropic.Anthropic(max_retries=0)  # a silent SDK retry would spend outside the reservation
    fetcher = Fetcher()
    code = 0
    if (os.environ.get("FAQ_BACKEND") != "cli" and not os.environ.get("ANTHROPIC_API_KEY")
            and not os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        switch_to_subscription("start", "no API key in the environment")
    try:
        if a.mode == "daily":
            run_daily(client, fetcher, ledger, log, date.fromisoformat(a.date) if a.date else today)
        elif a.mode == "patch":
            run_patch(client, ledger, log, a.run, json.loads(Path(a.failures).read_text("utf-8")))
        elif a.mode == "addday":
            log["src_run"], log["day"] = a.run, a.day
            run_addday(client, fetcher, ledger, log, a.run, date.fromisoformat(a.day))
        else:
            ws = date.fromisoformat(a.week_start)
            until = date.fromisoformat(a.until) if a.until else ws + timedelta(days=6)
            resume = None
            if a.resume:
                resume = json.loads((CACHE_DIR / f"{a.resume}.json").read_text("utf-8"))
                if not resume.get("drafts") or resume["drafts"][-1]["candidate"] != f"week-{ws.isoformat()}":
                    raise ValueError(f"--resume {a.resume} is not a failed run of the week starting {ws}")
                log["resumed_from"] = a.resume
            run_week(client, fetcher, ledger, log, ws, until, today, resume)
    except (BudgetExceeded, RuntimeError, ValueError, FileExistsError, anthropic.APIError) as e:
        log["error"] = redact(f"{type(e).__name__}: {e}")
        print(log["error"], file=sys.stderr)
        code = 1
    finally:
        log["source"] = run_source()
        if FALLBACK:
            log["fallback"] = dict(FALLBACK)
        log["model_calls"] = list(CALLS)
        log["usd_this_run"] = round(ledger.run_spent(), 4)
        log["usd_month_daily"] = round(ledger.month_spent(), 4)
        log["usd_weeks_total"] = round(ledger.week_spent(), 4)
        cache = log.pop("_cache", None)
        if cache:
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            (CACHE_DIR / f"{run_id}.json").write_text(json.dumps(cache, ensure_ascii=False, indent=1, default=str), "utf-8")
        RUNS.mkdir(parents=True, exist_ok=True)
        # The whole log is masked once more on its way out, whichever path put text into it (Codex)
        (RUNS / f"{run_id}.json").write_text(redact(json.dumps(log, ensure_ascii=False, indent=1, default=str)),
                                             "utf-8")
        print(redact(json.dumps({k: log.get(k) for k in ("run", "published", "day_result", "error", "source",
                                                         "usd_this_run")}, ensure_ascii=False)))
    return code


if __name__ == "__main__":
    sys.exit(main())

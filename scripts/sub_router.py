"""Subscription-first LLM router for the synapse-news pipeline.

Replaces anthropic.Anthropic() with a shim whose messages.create() calls
logged-in subscription CLIs in order, failing over on error/quota:
  claude (Claude Code) -> codex -> grok -> cursor agent -> gemini CLI
Paid APIs (DeepSeek / Gemini API / Anthropic API) are used ONLY when
ROUTER_API_DAILY_BUDGET_USD > 0 is set AND the key exists in the environment;
otherwise they are logged as "skipped: not approved".
Every call is appended to logs/router-YYYY-MM-DD.jsonl (no secrets logged).
"""
from __future__ import annotations
import json, os, shutil, subprocess, tempfile, time
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs"
STATE = LOG_DIR / "router-state.json"
HOME = Path.home()
TIMEOUT = int(os.environ.get("ROUTER_CLI_TIMEOUT", "600"))
COOLDOWN = int(os.environ.get("ROUTER_COOLDOWN_SEC", "3600"))
QUOTA_HINTS = ("usage limit", "rate limit", "quota", "expired", "authenticate",
               "login", "upgrade required", "outdated", "429", "426", "401")
STATS = {"calls": 0, "ok": 0, "failed": 0, "by_provider": {}}


def _which(*names):
    for n in names:
        p = shutil.which(n) or (str(HOME / ".local/bin" / n) if (HOME / ".local/bin" / n).exists() else None)
        if p:
            return p
    return None


def _log(rec: dict):
    LOG_DIR.mkdir(exist_ok=True)
    rec["ts"] = datetime.now().isoformat(timespec="seconds")
    with open(LOG_DIR / f"router-{datetime.now():%Y-%m-%d}.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _state():
    try:
        return json.loads(STATE.read_text())
    except Exception:
        return {}


def _cool(name, reason):
    s = _state(); s[name] = {"until": time.time() + COOLDOWN, "reason": reason[:300]}
    STATE.write_text(json.dumps(s, indent=1))


def _run(cmd, prompt=None, cwd=None):
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                       timeout=TIMEOUT, cwd=cwd or tempfile.gettempdir())
    return r.returncode, r.stdout, r.stderr


# ---- adapters: each returns text or raises RuntimeError(reason) ----
def cli_claude(prompt):
    exe = _which("claude")
    if not exe: raise RuntimeError("not installed")
    # call the binary directly (not the zsh function); headless, no tools
    rc, out, err = _run([exe, "-p", "--output-format", "text"], prompt)
    if rc or not out.strip(): raise RuntimeError((err or out).strip()[-400:] or f"rc={rc}")
    return out.strip()


def cli_codex(prompt):
    exe = _which("codex") or ("/Applications/Codex.app/Contents/Resources/codex"
                              if Path("/Applications/Codex.app/Contents/Resources/codex").exists() else None)
    if not exe: raise RuntimeError("not installed")
    with tempfile.NamedTemporaryFile("r", suffix=".txt", delete=False) as t:
        outf = t.name
    rc, out, err = _run([exe, "exec", "--skip-git-repo-check", "-s", "read-only", "-o", outf, "-"], prompt)
    text = Path(outf).read_text() if Path(outf).exists() else ""
    Path(outf).unlink(missing_ok=True)
    if rc or not text.strip(): raise RuntimeError((err + out).strip()[-400:] or f"rc={rc}")
    return text.strip()


def cli_grok(prompt):
    exe = _which("grok")
    if not exe: raise RuntimeError("not installed")
    rc, out, err = _run([exe, "-p", prompt])
    if rc or not out.strip() or "Internal error" in out: raise RuntimeError((err + out).strip()[-400:])
    return out.strip()


def cli_cursor(prompt):
    exe = _which("cursor-agent", "agent")
    if not exe: raise RuntimeError("not installed")
    rc, out, err = _run([exe, "-p", "--output-format", "text", prompt])
    if rc or not out.strip(): raise RuntimeError((err + out).strip()[-400:])
    return out.strip()


def cli_gemini(prompt):
    exe = _which("gemini")
    if not exe: raise RuntimeError("not installed (Gemini CLI)")
    rc, out, err = _run([exe, "-p", prompt])
    if rc or not out.strip(): raise RuntimeError((err + out).strip()[-400:])
    return out.strip()


def _budget_ok(name):
    budget = float(os.environ.get("ROUTER_API_DAILY_BUDGET_USD", "0") or 0)
    if budget <= 0:
        raise RuntimeError("skipped: paid API not approved (ROUTER_API_DAILY_BUDGET_USD unset)")
    s = _state(); day = f"{datetime.now():%Y-%m-%d}"
    spent = s.get("api_spend", {}).get(day, 0.0)
    if spent >= budget: raise RuntimeError(f"skipped: daily budget {budget} reached")


def _bill(usd):
    s = _state(); day = f"{datetime.now():%Y-%m-%d}"
    s.setdefault("api_spend", {})[day] = s.get("api_spend", {}).get(day, 0.0) + usd
    STATE.write_text(json.dumps(s, indent=1))


def _openai_compat(url, key_env, model, prompt, max_tokens, usd_per_call):
    _budget_ok(key_env)
    key = os.environ.get(key_env)
    if not key: raise RuntimeError(f"skipped: {key_env} not in environment")
    import httpx
    r = httpx.post(url, headers={"Authorization": f"Bearer {key}"}, timeout=TIMEOUT,
                   json={"model": model, "max_tokens": max_tokens,
                         "messages": [{"role": "user", "content": prompt}]})
    if r.status_code != 200: raise RuntimeError(f"http {r.status_code}")
    _bill(usd_per_call)
    return r.json()["choices"][0]["message"]["content"].strip()


def api_deepseek(prompt, max_tokens=8192):
    return _openai_compat("https://api.deepseek.com/chat/completions", "DEEPSEEK_API_KEY",
                          "deepseek-chat", prompt, max_tokens, 0.01)


def api_gemini(prompt, max_tokens=8192):
    return _openai_compat("https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
                          "GEMINI_API_KEY", "gemini-2.5-flash", prompt, max_tokens, 0.01)


def api_anthropic(prompt, max_tokens=8192, model="claude-sonnet-4-6"):
    _budget_ok("ANTHROPIC_API_KEY")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("skipped: ANTHROPIC_API_KEY not in environment")
    import anthropic
    r = _REAL_ANTHROPIC().messages.create(model=model, max_tokens=max_tokens,
                                          messages=[{"role": "user", "content": prompt}])
    _bill(0.05)
    return r.content[0].text.strip()


CLI_ORDER = [("claude-code", cli_claude), ("codex", cli_codex), ("grok", cli_grok),
             ("cursor", cli_cursor), ("gemini-cli", cli_gemini)]
API_ORDER = [("deepseek-api", api_deepseek), ("gemini-api", api_gemini), ("anthropic-api", api_anthropic)]


def order():
    names = os.environ.get("ROUTER_ORDER")
    allp = CLI_ORDER + API_ORDER
    if names:
        m = dict(allp); return [(n, m[n]) for n in names.split(",") if n in m]
    return allp


def complete(prompt: str, purpose: str = "") -> tuple[str, str]:
    STATS["calls"] += 1
    attempts = []
    st = _state()
    for name, fn in order():
        cd = st.get(name)
        if cd and cd.get("until", 0) > time.time():
            attempts.append({"provider": name, "result": "cooldown", "reason": cd.get("reason")}); continue
        t0 = time.time()
        try:
            text = fn(prompt)
            attempts.append({"provider": name, "result": "ok", "sec": round(time.time() - t0, 1)})
            _log({"purpose": purpose, "provider": name, "status": "ok", "attempts": attempts})
            STATS["ok"] += 1; STATS["by_provider"][name] = STATS["by_provider"].get(name, 0) + 1
            return text, name
        except subprocess.TimeoutExpired:
            reason = "timeout"
        except Exception as e:
            reason = str(e)[:400]
        attempts.append({"provider": name, "result": "fail", "reason": reason})
        if not reason.startswith("skipped") and any(h in reason.lower() for h in QUOTA_HINTS):
            _cool(name, reason)
    STATS["failed"] += 1
    _log({"purpose": purpose, "provider": None, "status": "all_failed", "attempts": attempts})
    raise RuntimeError("all providers failed: " + json.dumps(attempts, ensure_ascii=False)[:1500])


def probe() -> dict:
    """Cheap liveness probe of each provider (ignores cooldowns)."""
    res = {}
    for name, fn in order():
        try:
            out = fn("Reply with exactly: OK")
            res[name] = "ok" if out else "empty"
        except subprocess.TimeoutExpired:
            res[name] = "timeout"
        except Exception as e:
            res[name] = "fail: " + str(e)[:200]
    _log({"purpose": "probe", "probe": res})
    return res


# ---- anthropic shim ----
_REAL_ANTHROPIC = None


def _flatten(system, messages):
    parts = []
    if system:
        parts.append(system if isinstance(system, str) else "\n".join(b.get("text", "") for b in system))
    for m in messages:
        c = m["content"]
        if not isinstance(c, str):
            c = "\n".join(b.get("text", "") for b in c if isinstance(b, dict))
        parts.append(c if m["role"] == "user" else f"[assistant]\n{c}")
    parts.append("\n(Respond with the final answer only. Do not use tools, do not edit files.)")
    return "\n\n".join(parts)


class _Messages:
    def create(self, model=None, max_tokens=None, messages=(), system=None, **kw):
        import anthropic, httpx
        try:
            text, prov = complete(_flatten(system, messages), purpose=f"model={model}")
        except RuntimeError as e:
            raise anthropic.APIConnectionError(message=str(e)[:500],
                                               request=httpx.Request("POST", "http://router.local"))
        return SimpleNamespace(content=[SimpleNamespace(type="text", text=text)],
                               model=f"router:{prov}", stop_reason="end_turn",
                               usage=SimpleNamespace(input_tokens=0, output_tokens=0))


class RouterClient:
    def __init__(self, *a, **kw):
        self.messages = _Messages()


def install():
    global _REAL_ANTHROPIC
    import anthropic
    if anthropic.Anthropic is not RouterClient:
        _REAL_ANTHROPIC = anthropic.Anthropic
        anthropic.Anthropic = RouterClient

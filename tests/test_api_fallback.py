"""The API -> subscription fallback in pipeline/api_daily.py, with the API and `claude -p` simulated.

No test here calls the real API or the real CLI; tests/../scratchpad live runs cover those."""
from datetime import date
import json
import sys
import time
from types import SimpleNamespace

import anthropic
import httpx
import pytest

from pipeline import api_daily as D


@pytest.fixture(autouse=True)
def clean_state(monkeypatch, tmp_path):
    monkeypatch.setattr(D, "CALLS", [])
    monkeypatch.setattr(D, "FALLBACK", {})
    monkeypatch.setattr(D, "_SPENT_ACCOUNTS", set())
    monkeypatch.setenv("FAQ_BACKEND", "api")        # restored to the real value after each test
    monkeypatch.setenv("FAQ_AUTO_FALLBACK", "1")
    monkeypatch.setenv("FAQ_CLI_ACCOUNTS", D.CLI_ACCOUNTS)
    home = tmp_path / "home"
    for n in (2, 3, 4, 5):
        (home / f".claude-acct{n}").mkdir(parents=True)
    monkeypatch.setattr(D.Path, "home", staticmethod(lambda: home))
    # The GitHub runner that runs these tests has no Claude Code CLI; pretend this machine does.
    real_which = D.shutil.which
    monkeypatch.setattr(D.shutil, "which", lambda n, *a, **k: "claude" if n == "claude" else real_which(n, *a, **k))


def api_error(status: int, message: str, body: dict | None = None):
    req = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    cls = {400: anthropic.BadRequestError, 401: anthropic.AuthenticationError, 403: anthropic.PermissionDeniedError,
           429: anthropic.RateLimitError, 500: anthropic.InternalServerError}.get(status, anthropic.APIStatusError)
    return cls(message, response=httpx.Response(status, request=req),
               body=body or {"type": "error", "error": {"type": "x", "message": message}})


class FakeClient:
    """An API client whose every request fails with `exc`."""
    def __init__(self, exc):
        self.exc, self.calls = exc, 0
        self.beta = SimpleNamespace(messages=SimpleNamespace(create=self._fail, stream=self._fail))

    def _fail(self, **kw):
        self.calls += 1
        raise self.exc


class FakeCli:
    """Stands in for cli_events: per account, a list of event lists (one per session)."""
    def __init__(self, sessions: dict[str, list[list[dict]]]):
        self.sessions, self.runs = sessions, []

    def __call__(self, args, prompt, env, timeout):
        cfg = env.get("CLAUDE_CONFIG_DIR")
        name = "claude" if not cfg else "claude" + cfg.rsplit("acct", 1)[1]
        self.runs.append({"account": name, "args": args, "prompt": prompt, "env": env})
        script = self.sessions[name].pop(0) if len(self.sessions[name]) > 1 else self.sessions[name][0]
        yield from script


def ok(structured: dict) -> list[dict]:
    return [{"type": "system", "subtype": "init"},
            {"type": "result", "subtype": "success", "is_error": False, "result": "", "structured_output": structured}]


LIMITED = [{"type": "system", "subtype": "init"},
           {"type": "rate_limit_event", "rate_limit_info": {"status": "rejected", "rateLimitType": "five_hour",
                                                            "resetsAt": 1795000000, "isUsingOverage": False}}]
LOGGED_OUT = [{"type": "assistant", "error": "authentication_failed",
               "message": {"content": [{"type": "text", "text": "Not logged in · Please run /login"}]}},
              {"type": "result", "subtype": "success", "is_error": True, "result": "Not logged in · Please run /login"}]
SCHEMA = {"type": "object", "properties": {"x": {"type": "integer"}}}


def ask(client, ledger, step="write", **kw):
    return D.call_model(client, ledger, step, "claude-opus-5-5", system="sys",
                        messages=[{"role": "user", "content": [{"type": "text", "text": "SOURCES: s"},
                                                               {"type": "text", "text": "write it"}]}],
                        max_tokens=1000, effort="high", schema=SCHEMA, **kw)


def rows(path):
    return json.loads(path.read_text("utf-8"))


# ------------------------------------------------------------ when to switch

@pytest.mark.parametrize("status,message", [
    (429, "Number of request tokens has exceeded your per-minute rate limit"),
    (400, "Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing."),
    (400, "You have reached your specified API usage limits. You will regain access on 2026-12-01 at 00:00 UTC."),
    (401, "invalid x-api-key"),
    (402, "billing_error"),
    (400, "Insufficient balance"),
    (403, "Your organization has been disabled."),
])
def test_quota_and_key_errors_move_the_run_to_the_subscription(monkeypatch, tmp_path, status, message):
    cli = FakeCli({"claude": [ok({"x": 1})]})
    monkeypatch.setattr(D, "cli_events", cli)
    client = FakeClient(api_error(status, message))
    led = D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18))
    resp = ask(client, led)
    assert D.last_json(resp) == {"x": 1}
    assert D.os.environ["FAQ_BACKEND"] == "cli"
    assert D.FALLBACK["step"] == "write" and str(status) in D.FALLBACK["reason"]
    api_row, cli_row = rows(tmp_path / "l.json")
    assert (api_row["source"], api_row["ok"]) == ("api", False)
    assert (cli_row["source"], cli_row["ok"], cli_row["usd"]) == ("subscription:claude", True, 0.0)
    # The rest of the run stays on the subscription: the API is not asked again.
    ask(client, led, step="verify")
    assert client.calls == 1 and len(cli.runs) == 2
    assert D.run_source() == "subscription(claude)"


def test_spend_limit_named_only_in_the_body(monkeypatch, tmp_path):
    monkeypatch.setattr(D, "cli_events", FakeCli({"claude": [ok({"x": 1})]}))
    err = api_error(400, "Bad request", body={"type": "error", "error": {"type": "enforced_spend_limit_reached"}})
    ask(FakeClient(err), D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    assert D.run_source() == "subscription(claude)"


@pytest.mark.parametrize("status,message", [(500, "Internal server error"), (529, "Overloaded"),
                                            (400, "messages: text content blocks must be non-empty")])
def test_server_and_request_errors_do_not_switch(monkeypatch, tmp_path, status, message):
    cli = FakeCli({"claude": [ok({"x": 1})]})
    monkeypatch.setattr(D, "cli_events", cli)
    with pytest.raises(anthropic.APIStatusError):
        ask(FakeClient(api_error(status, message)), D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    assert D.os.environ["FAQ_BACKEND"] == "api" and not cli.runs and not D.FALLBACK


def test_a_rate_limit_error_inside_a_200_stream_switches(monkeypatch, tmp_path):
    monkeypatch.setattr(D, "cli_events", FakeCli({"claude": [ok({"x": 1})]}))
    err = api_error(200, "rate limited", body={"type": "error", "error": {"type": "rate_limit_error", "message": "x"}})
    ask(FakeClient(err), D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    assert D.run_source() == "subscription(claude)"


def test_no_cli_on_this_machine_keeps_the_original_error(monkeypatch, tmp_path):
    monkeypatch.setattr(D.shutil, "which", lambda n, *a, **k: None)
    cli = FakeCli({"claude": [ok({"x": 1})]})
    monkeypatch.setattr(D, "cli_events", cli)
    with pytest.raises(anthropic.RateLimitError):
        ask(FakeClient(api_error(429, "rate limited")), D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    assert not cli.runs and D.os.environ["FAQ_BACKEND"] == "api"


def test_a_key_echoed_in_an_error_never_reaches_the_logs(monkeypatch, tmp_path, capsys):
    fake_key = "sk-ant-api03-" + "Z" * 40
    monkeypatch.setenv("ANTHROPIC_API_KEY", fake_key)
    monkeypatch.setattr(D, "cli_events", FakeCli({"claude": [ok({"x": 1})]}))
    ask(FakeClient(api_error(401, f"invalid x-api-key: {fake_key}")),
        D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    seen = json.dumps(D.FALLBACK) + json.dumps(D.CALLS) + (tmp_path / "l.json").read_text("utf-8")
    seen += capsys.readouterr().err
    assert fake_key not in seen and "Z" * 40 not in seen and "sk-ant-***" in seen


def test_fallback_can_be_turned_off(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_AUTO_FALLBACK", "0")
    cli = FakeCli({"claude": [ok({"x": 1})]})
    monkeypatch.setattr(D, "cli_events", cli)
    with pytest.raises(anthropic.RateLimitError):
        ask(FakeClient(api_error(429, "rate limited")), D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    assert not cli.runs


def test_our_own_budget_cap_also_switches_without_calling_the_api(monkeypatch, tmp_path):
    (tmp_path / "l.json").write_text(json.dumps(
        [{"ts": "2026-11-02T00:00:00+00:00", "run": "old", "mode": "daily", "usd": D.CAPS["daily_month"]}]))
    monkeypatch.setattr(D, "cli_events", FakeCli({"claude": [ok({"x": 1})]}))
    client = FakeClient(AssertionError("the API must not be called"))
    ask(client, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    assert client.calls == 0 and "budget" in D.FALLBACK["reason"]


def test_batch_caps_still_stop_the_batch(monkeypatch, tmp_path):
    (tmp_path / "l.json").write_text(json.dumps(
        [{"ts": "2026-11-02T00:00:00+00:00", "run": "old", "mode": "audit", "usd": D.CAPS["audit_total"]}]))
    cli = FakeCli({"claude": [ok({"x": 1})]})
    monkeypatch.setattr(D, "cli_events", cli)
    with pytest.raises(D.BudgetExceeded):
        ask(FakeClient(AssertionError("no API call")), D.Ledger(tmp_path / "l.json", "audit", "r1", date(2026, 11, 18)))
    assert not cli.runs and not D.FALLBACK


# ------------------------------------------------------------ claude -> claude5

def test_accounts_rotate_and_a_spent_account_is_not_retried(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    cli = FakeCli({"claude": [LIMITED], "claude2": [LOGGED_OUT], "claude3": [ok({"x": 3})]})
    monkeypatch.setattr(D, "cli_events", cli)
    led = D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18))
    assert D.last_json(ask(None, led)) == {"x": 3}
    assert [r["account"] for r in cli.runs] == ["claude", "claude2", "claude3"]
    assert "CLAUDE_CONFIG_DIR" not in cli.runs[0]["env"]
    assert cli.runs[2]["env"]["CLAUDE_CONFIG_DIR"].endswith(".claude-acct3")
    ask(None, led, step="verify")
    assert [r["account"] for r in cli.runs][3:] == ["claude3"]
    notes = [(r["source"], r["ok"]) for r in rows(tmp_path / "l.json")]
    assert notes == [("subscription:claude", False), ("subscription:claude2", False),
                     ("subscription:claude3", True), ("subscription:claude3", True)]
    assert "usage limit (five_hour)" in rows(tmp_path / "l.json")[0]["note"]
    assert D.run_source() == "subscription(claude3)"


def test_every_account_spent_is_a_clear_failure(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    monkeypatch.setattr(D, "cli_events", FakeCli({n: [LIMITED] for n in ("claude", "claude2", "claude3",
                                                                          "claude4", "claude5")}))
    with pytest.raises(RuntimeError, match="no subscription account is available.*claude5: usage limit"):
        ask(None, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))


def test_a_429_retry_inside_the_cli_counts_as_the_account_being_limited(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    retry = [{"type": "system", "subtype": "api_retry", "error_status": 429, "attempt": 1}]
    cli = FakeCli({"claude": [retry], "claude2": [ok({"x": 2})]})
    monkeypatch.setattr(D, "cli_events", cli)
    assert D.last_json(ask(None, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))) == {"x": 2}


def test_an_ordinary_cli_error_does_not_burn_the_other_accounts(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    bad = [{"type": "result", "subtype": "error_max_structured_output_retries", "is_error": True, "result": ""}]
    cli = FakeCli({"claude": [bad], "claude2": [ok({"x": 2})]})
    monkeypatch.setattr(D, "cli_events", cli)
    with pytest.raises(RuntimeError, match=r"claude -p \(claude\) failed"):
        ask(None, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)))
    assert len(cli.runs) == 1


@pytest.mark.parametrize("result", ["prompt is too long: 214290 tokens > 200000 maximum", ""])
def test_numbers_and_empty_answers_are_not_account_limits(monkeypatch, tmp_path, result):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    session = [{"type": "result", "subtype": "success", "is_error": bool(result), "result": result}]
    cli = FakeCli({"claude": [session], "claude2": [ok({"x": 2})]})
    monkeypatch.setattr(D, "cli_events", cli)
    with pytest.raises(RuntimeError, match=r"claude -p \(claude\) failed"):
        D.call_model(None, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)), "write",
                     "claude-opus-5-5", system="s", messages=[{"role": "user", "content": "x"}],
                     max_tokens=10, effort="low")
    assert len(cli.runs) == 1 and [c["ok"] for c in D.CALLS] == [False]


def test_account_order_and_missing_config_dirs(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_CLI_ACCOUNTS", "claude4, claude, claude9")
    names = [n for n, _ in D.cli_accounts()]
    assert names == ["claude4", "claude"]          # claude9 has no ~/.claude-acct9
    monkeypatch.setenv("FAQ_CLI_ACCOUNTS", "codex")
    with pytest.raises(ValueError):
        D.cli_accounts()


def test_child_env_never_carries_the_api_key(monkeypatch, tmp_path):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-not-a-real-key")
    monkeypatch.setenv("ANTHROPIC_AUTH_TOKEN", "test-not-a-real-token")
    monkeypatch.setenv("ANTHROPIC_BASE_URL", "http://127.0.0.1:9")
    monkeypatch.setenv("CLAUDE_CONFIG_DIR", "C:/somewhere/else")
    env = D.cli_env(None)
    assert not {"ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL", "CLAUDE_CONFIG_DIR"} & set(env)
    assert D.cli_env("C:/x/.claude-acct2")["CLAUDE_CONFIG_DIR"] == "C:/x/.claude-acct2"


# ------------------------------------------------------------ research on the subscription

def search_event(query, links):
    return {"type": "user", "tool_use_result": {
        "query": query, "searchCount": 1, "durationSeconds": 1.0,
        "results": [{"tool_use_id": "srvtoolu_1", "content": [{"title": t, "url": u} for t, u in links]},
                    "The search tool's own prose summary, which is not a source."]}}


def research_answer(urls):
    return {"candidates": [{"headline": "H", "category": "ai-ml", "why": "w", "entities": [], "source_urls": urls}]}


def test_research_allowlist_comes_only_from_the_search_tool(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    session = [search_event("ai news nov 18", [("A", "https://a.com/x"), ("B", "https://b.com/y")]),
               *ok(research_answer(["https://a.com/x", "https://b.com/y", "https://made-up.com/z"]))]
    cli = FakeCli({"claude": [session]})
    monkeypatch.setattr(D, "cli_events", cli)
    log: dict = {}
    data, allow = D.research(None, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)), log,
                             "find stories", D.RESEARCH_DAILY_SCHEMA, max_uses=10)
    assert data["candidates"][0]["source_urls"][-1] == "https://made-up.com/z"
    assert {v["url"] for v in allow.values()} == {"https://a.com/x", "https://b.com/y"}
    assert log["research"]["queries"] == ["ai news nov 18"]
    args = cli.runs[0]["args"]
    assert args[args.index("--tools") + 1] == "WebSearch" and "WebFetch" not in " ".join(args)
    assert "at most 10 web searches" in cli.runs[0]["prompt"]


def test_research_follow_up_keeps_the_urls_found_earlier(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    first = [search_event("q1", [("A", "https://a.com/x")]), *ok(research_answer(["https://a.com/x"]))]
    second = [search_event("q2", [("C", "https://c.com/w")]),
              *ok(research_answer(["https://a.com/x", "https://c.com/w"]))]
    cli = FakeCli({"claude": [first, second]})
    monkeypatch.setattr(D, "cli_events", cli)
    data, allow = D.research(None, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)), {},
                             "find stories", D.RESEARCH_DAILY_SCHEMA, max_uses=10,
                             complaint=lambda d, a: None if len(a) >= 2 else "Need a second outlet.")
    assert {v["url"] for v in allow.values()} == {"https://a.com/x", "https://c.com/w"}
    follow_up = cli.runs[1]["prompt"]
    assert "Search results you already found" in follow_up and "https://a.com/x" in follow_up
    assert "Need a second outlet." in follow_up


def test_runaway_searching_is_stopped(monkeypatch, tmp_path):
    monkeypatch.setenv("FAQ_BACKEND", "cli")
    session = [search_event(f"q{i}", [("A", f"https://a.com/{i}")]) for i in range(7)] + ok(research_answer([]))
    monkeypatch.setattr(D, "cli_events", FakeCli({"claude": [session]}))
    with pytest.raises(RuntimeError, match="searched 7 times"):
        D.research(None, D.Ledger(tmp_path / "l.json", "daily", "r1", date(2026, 11, 18)), {},
                   "find", D.RESEARCH_DAILY_SCHEMA, max_uses=3)


# ------------------------------------------------------------ a real child process

FAKE_CLAUDE = r'''
import json, sys, time
sys.stdin.read()
mode = sys.argv[1]
print(json.dumps({"type": "system", "subtype": "init"}), flush=True)
if mode == "limited":
    print(json.dumps({"type": "rate_limit_event", "rate_limit_info": {"status": "rejected", "rateLimitType": "seven_day",
                      "resetsAt": 1795000000, "isUsingOverage": False}}), flush=True)
    time.sleep(60)   # the real CLI would sit in its retry loop here
if mode == "grandchild":  # a child that keeps the stdout pipe open after the CLI itself is gone
    import subprocess
    subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
    time.sleep(60)
print(json.dumps({"type": "result", "subtype": "success", "is_error": False, "result": "hello from the fake"}), flush=True)
'''


def test_child_process_is_killed_as_soon_as_the_account_is_limited(tmp_path):
    script = tmp_path / "fake_claude.py"
    script.write_text(FAKE_CLAUDE)
    t0 = time.monotonic()
    with pytest.raises(D.AccountUnavailable, match="seven_day"):
        D.cli_once([sys.executable, str(script), "limited"], "prompt" * 50_000, D.cli_env(None), None, 0)
    assert time.monotonic() - t0 < 20
    text, results, queries = D.cli_once([sys.executable, str(script), "ok"], "prompt", D.cli_env(None), None, 0)
    assert text == "hello from the fake" and results == [] and queries == []


def test_timeout_kills_the_whole_process_tree(monkeypatch, tmp_path):
    script = tmp_path / "fake_claude.py"
    script.write_text(FAKE_CLAUDE)
    monkeypatch.setattr(D, "CLI_TIMEOUT", 2)
    t0 = time.monotonic()
    with pytest.raises(D.subprocess.TimeoutExpired):
        D.cli_once([sys.executable, str(script), "grandchild"], "p", D.cli_env(None), None, 0)
    assert time.monotonic() - t0 < 15


# ------------------------------------------------------------ the run log says which source was used

def run_main(monkeypatch, tmp_path, client):
    monkeypatch.setattr(D, "RUNS", tmp_path / "runs")
    monkeypatch.setattr(D, "LEDGER", tmp_path / "runs" / "ledger.json")
    monkeypatch.setattr(D, "CACHE_DIR", tmp_path / "cache")
    monkeypatch.setattr(D.anthropic, "Anthropic", lambda **kw: client)
    monkeypatch.setattr(D, "Fetcher", lambda: None)

    def fake_daily(client, fetcher, ledger, log, run_date):
        D.call_model(client, ledger, "research#0", D.RESEARCH_MODEL, system="s",
                     messages=[{"role": "user", "content": "find"}], max_tokens=100, effort="medium")
        D.call_model(client, ledger, "write", D.WRITE_MODEL, system="s",
                     messages=[{"role": "user", "content": "write"}], max_tokens=100, effort="high")
    monkeypatch.setattr(D, "run_daily", fake_daily)
    assert D.main(["--mode", "daily", "--trial"]) == 0
    (log_path,) = [p for p in (tmp_path / "runs").glob("*.json") if p.name != "ledger.json"]
    return json.loads(log_path.read_text("utf-8"))


def text_result(text):
    return [{"type": "result", "subtype": "success", "is_error": False, "result": text}]


def test_run_log_records_the_switch(monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-not-a-real-key")
    cli = FakeCli({"claude": [LIMITED], "claude2": [text_result("{}")]})
    monkeypatch.setattr(D, "cli_events", cli)
    log = run_main(monkeypatch, tmp_path, FakeClient(api_error(429, "rate limited")))
    assert log["source"] == "subscription(claude2)"
    assert log["fallback"]["step"] == "research#0" and "429" in log["fallback"]["reason"]
    assert [(c["step"], c["source"], c["ok"]) for c in log["model_calls"]] == [
        ("research#0", "api", False), ("research#0", "subscription:claude", False),
        ("research#0", "subscription:claude2", True), ("write", "subscription:claude2", True)]
    assert '"source": "subscription(claude2)"' in capsys.readouterr().out
    assert "test-not-a-real-key" not in json.dumps(log) + (tmp_path / "runs" / "ledger.json").read_text("utf-8")


def test_no_api_key_starts_on_the_subscription(monkeypatch, tmp_path):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)
    monkeypatch.setattr(D, "cli_events", FakeCli({"claude": [text_result("{}")]}))
    client = FakeClient(AssertionError("the API must not be called"))
    log = run_main(monkeypatch, tmp_path, client)
    assert client.calls == 0
    assert log["source"] == "subscription(claude)" and log["fallback"]["step"] == "start"

"""Read-only audit of the articles published before the API pipeline (2026-04-03..08-03).

    python -m pipeline.api_audit sample [--n 120] [--seed 20261113]
    python -m pipeline.api_audit run [--limit N]
    python -m pipeline.api_audit report

    python -m pipeline.api_audit census                      # every old article, not a sample
    python -m pipeline.api_audit run --census [--shard 1/3]  # shards can run side by side
    python -m pipeline.api_audit report --census

Nothing here edits an article. Sources are fetched with the pipeline's Fetcher
(robots on every hop, 403/429 final, size cap). Every API call is reserved in the
shared ledger under its own cap, CAPS["audit_total"].

The model only says whether a fact is in the readable sources; the program decides
what a missing fact means. If every listed source was read it is "unsupported";
if some could not be read it is "undetermined", never an error.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
import uuid
from datetime import date, datetime
from pathlib import Path

import anthropic
import frontmatter

from pipeline import api_gates as G
from pipeline.api_daily import (ARTICLES, CACHE_DIR, LEDGER, PROMPTS, ROOT, TPE, VERIFY_MODEL, BudgetExceeded,
                                Ledger, call_model, last_json, with_sources)
from pipeline.api_fetch import Fetcher

AUDIT_DIR = ROOT / "data" / "audit"
SAMPLE = AUDIT_DIR / "sample.json"
CENSUS = AUDIT_DIR / "census.json"
RESULTS = AUDIT_DIR / "articles"  # one file per article, shared by the sample and the census
CLIFF = date(2026, 7, 17)     # Google clicks fell to 0 from this day
LAST_OLD = date(2026, 8, 3)   # last article of the old cloud schedule
MIN_WORDS = 120               # a fetched page shorter than this cannot carry an article's facts

AUDIT_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["verdicts"],
    "properties": {"verdicts": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["id", "verdict", "evidence"],
        "properties": {"id": {"type": "integer"},
                       "verdict": {"type": "string",
                                   "enum": ["supported", "opinion", "contradicted", "not_in_sources"]},
                       "evidence": {"type": "string"}}}}},
}


def _pub_date(v) -> date:
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    return date.fromisoformat(str(v)[:10])


def old_en_articles() -> list[dict]:
    out = []
    for p in sorted(ARTICLES.glob("*-en.md")):
        if "-ai-week-" in p.stem:
            continue
        post = frontmatter.load(p)
        m = post.metadata
        d = _pub_date(m.get("publishedAt"))
        if d > LAST_OLD:
            continue
        out.append({"slug": p.stem, "date": d, "title": m.get("title", ""), "summary": m.get("summary", ""),
                    "category": m.get("category"), "body": post.content,
                    "sources": [s for s in (m.get("sources") or []) if s.get("url")]})
    return out


def draw_sample(articles: list[dict], n: int, seed: int) -> list[dict]:
    """Half from before the cliff (stratified by month), half from after it, in a
    shuffled order so the first rows of a pilot cover both halves."""
    rng = random.Random(seed)
    before = [a for a in articles if a["date"] < CLIFF]
    after = [a for a in articles if a["date"] >= CLIFF]
    picked_after = rng.sample(after, min(n // 2, len(after)))
    k = n - len(picked_after)
    by_month: dict[str, list[dict]] = {}
    for a in before:
        by_month.setdefault(a["date"].strftime("%Y-%m"), []).append(a)
    months = sorted(by_month)
    quotas = {m: int(k * len(by_month[m]) / len(before)) for m in months}
    for m in sorted(months, key=lambda m: -len(by_month[m]))[: k - sum(quotas.values())]:
        quotas[m] += 1
    picked_before = [a for m in months for a in rng.sample(by_month[m], quotas[m])]
    rows = [_row(a) for a in picked_before + picked_after]
    rng.shuffle(rows)
    return rows


def _row(a: dict) -> dict:
    return {"slug": a["slug"], "date": a["date"].isoformat(),
            "stratum": "after-7/17" if a["date"] >= CLIFF else a["date"].strftime("%Y-%m")}


def shard(rows: list[dict], spec: str) -> list[dict]:
    """'2/3' -> the second of three interleaved slices; '' -> all rows."""
    if not spec:
        return rows
    i, n = (int(x) for x in spec.split("/"))
    if not 1 <= i <= n:
        raise ValueError(f"bad shard {spec}")
    return rows[i - 1::n]


def audit_units(a: dict) -> list[dict]:
    units = [{"id": 1, "where": "title", "text": a["title"]}, {"id": 2, "where": "summary", "text": a["summary"]}]
    heading = ""
    for line in a["body"].splitlines():
        s = line.strip()
        if not s or s == "---":
            continue
        if G._HEADING.match(s):
            heading = s.lstrip("# ").strip()
            units.append({"id": len(units) + 1, "where": "heading", "text": heading})
            continue
        for sent, _ in G.tagged_sentences(s):
            units.append({"id": len(units) + 1, "where": heading or "intro", "text": sent})
    return units


def classify(verdict: str, all_read: bool) -> str:
    if verdict == "contradicted":
        return "hard_error"
    if verdict == "not_in_sources":
        return "unsupported" if all_read else "undetermined"
    return verdict


def readable_now(f: dict, article_date: date) -> bool:
    """A page dated after the article is a later version (or a different page) of
    what the writer read, so it cannot show the article was wrong at the time."""
    if not (f["ok"] and f["words"] >= MIN_WORDS):
        return False
    if f["date"] and f["date"] > article_date:
        f["reason"] = f"page dated {f['date']}, after the article"
        return False
    return True


def audit_one(client, ledger: Ledger, fetcher: Fetcher, a: dict) -> dict:
    fetched = [fetcher.fetch(s["url"]) for s in a["sources"]]
    readable = [f for f in fetched if readable_now(f, a["date"])]
    unread = [f for f in fetched if f not in readable]
    res = {"slug": a["slug"], "date": a["date"].isoformat(), "category": a["category"],
           "n_sources": len(fetched), "n_readable": len(readable),
           "sources": [{"url": f["url"], "ok": f["ok"], "reason": f["reason"], "words": f["words"]} for f in fetched]}
    if not readable:
        res["status"] = "not_checked"
        return res
    cache = CACHE_DIR / "audit"
    cache.mkdir(parents=True, exist_ok=True)
    (cache / f"{a['slug']}.json").write_text(json.dumps(
        [{k: f[k] for k in ("url", "final_url", "site", "title", "date", "text")} for f in readable],
        ensure_ascii=False, default=str), "utf-8")

    units = audit_units(a)
    system = (PROMPTS / "api_audit.md").read_text("utf-8")
    note = f"THE ARTICLE WAS PUBLISHED ON {a['date'].isoformat()}.\n" + "LISTED SOURCES THAT COULD NOT BE READ: " + (
        "; ".join(f"{f['url']} ({f['reason'] or 'page too short'})" for f in unread) or "none")
    verdicts: dict[int, dict] = {}
    for round_no in (1, 2):  # the second round only asks for units the first answer skipped
        todo = [u for u in units if u["id"] not in verdicts]
        if not todo:
            break
        user = note + "\n\nUNITS TO CHECK (id, where it sits, text):\n" + "\n".join(
            f"{u['id']}. [{u['where']}] {u['text']}" for u in todo)
        resp = call_model(client, ledger, f"audit:{a['slug']}.{round_no}", VERIFY_MODEL, system=system,
                          messages=with_sources(readable, user), max_tokens=32_000, effort="high",
                          schema=AUDIT_SCHEMA)
        if resp.stop_reason in ("refusal", "max_tokens"):
            raise RuntimeError(f"auditor stopped with {resp.stop_reason}")
        asked = {u["id"] for u in todo}
        verdicts.update({v["id"]: v for v in last_json(resp)["verdicts"] if v["id"] in asked})
    all_read = not unread
    for u in units:
        v = verdicts.get(u["id"])
        u["verdict"] = "unchecked" if v is None else classify(v["verdict"], all_read)
        u["evidence"] = "" if v is None else v.get("evidence", "")
    res.update(status="checked", all_read=all_read, units=units)
    return res


def cmd_sample(n: int, seed: int) -> int:
    if SAMPLE.exists():
        print(f"{SAMPLE} already exists; delete it yourself to draw a new sample", file=sys.stderr)
        return 1
    rows = draw_sample(old_en_articles(), n, seed)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    SAMPLE.write_text(json.dumps({"n": n, "seed": seed, "rows": rows}, ensure_ascii=False, indent=1), "utf-8")
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["stratum"]] = counts.get(r["stratum"], 0) + 1
    print(f"sample of {len(rows)}: {counts}")
    return 0


def cmd_census() -> int:
    if CENSUS.exists():
        print(f"{CENSUS} already exists", file=sys.stderr)
        return 1
    rows = [_row(a) for a in old_en_articles()]
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    CENSUS.write_text(json.dumps({"rows": rows}, ensure_ascii=False, indent=1), "utf-8")
    done = sum((RESULTS / f"{r['slug']}.json").exists() for r in rows)
    print(f"census of {len(rows)} articles; {done} already audited by the sample")
    return 0


def cmd_run(limit: int, census: bool = False, shard_spec: str = "") -> int:
    rows = shard(json.loads((CENSUS if census else SAMPLE).read_text("utf-8"))["rows"], shard_spec)
    articles = {a["slug"]: a for a in old_en_articles()}
    today = datetime.now(TPE).date()
    run_id = f"{today.isoformat()}-audit-{uuid.uuid4().hex[:6]}"
    ledger = Ledger(LEDGER, "audit", run_id, today)
    client = anthropic.Anthropic(max_retries=0)
    fetcher = Fetcher()
    RESULTS.mkdir(parents=True, exist_ok=True)
    done = 0
    for row in rows:
        out = RESULTS / f"{row['slug']}.json"
        if out.exists():
            continue
        if limit and done >= limit:
            break
        try:
            res = audit_one(client, ledger, fetcher, articles[row["slug"]])
        except BudgetExceeded as e:
            print(f"stop: {e}", file=sys.stderr)
            break
        except (RuntimeError, ValueError, anthropic.APIError) as e:
            print(f"{row['slug']}: error {type(e).__name__}: {e}", file=sys.stderr)
            continue  # no result file, so the next run tries it again
        res["stratum"] = row["stratum"]
        out.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), "utf-8")
        done += 1
        tally = {}
        for u in res.get("units", []):
            tally[u["verdict"]] = tally.get(u["verdict"], 0) + 1
        print(f"{row['slug']}: {res['status']} readable {res['n_readable']}/{res['n_sources']} {tally}")
    print(f"run {run_id}: {done} articles, US${ledger.run_spent():.2f}; audits total US${ledger.audit_spent():.2f}")
    return 0


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def is_checked(r: dict) -> bool:
    """Checked = the model returned verdicts; an answer with none counts as not checked, not as clean."""
    return r["status"] == "checked" and any(u["verdict"] != "unchecked" for u in r.get("units", []))


def has_error(r: dict, kinds: tuple[str, ...]) -> bool:
    return any(u["verdict"] in kinds for u in r["units"])


HARD = ("hard_error",)
HARD_OR_UNSUPPORTED = ("hard_error", "unsupported")


def summarize(results: list[dict]) -> dict:
    checked = [r for r in results if is_checked(r)]
    units = [u for r in checked for u in r["units"] if u["verdict"] not in ("opinion", "unchecked")]
    def count(v: str) -> int:
        return sum(1 for u in units if u["verdict"] == v)
    hard = sum(has_error(r, HARD) for r in checked)
    either = sum(has_error(r, HARD_OR_UNSUPPORTED) for r in checked)
    return {
        "articles": len(results), "checked": len(checked), "not_checked": len(results) - len(checked),
        "articles_with_hard_error": hard, "article_ci": wilson(hard, len(checked)),
        "articles_with_any_error": either, "any_ci": wilson(either, len(checked)),
        "factual_units": len(units), "hard_error": count("hard_error"), "unsupported": count("unsupported"),
        "undetermined": count("undetermined"), "supported": count("supported"),
        "unit_ci": wilson(count("hard_error"), len(units)),
    }


def weighted(results: list[dict], kinds: tuple[str, ...], population: dict[str, int]) -> tuple[float, float, float]:
    """Share of all old articles with an error, weighting the before/after strata by
    their real size (the sample is half after 7/17, the population is not).
    Normal approximation with stratified variance; returns (estimate, low, high)."""
    total = sum(population.values())
    est = var = 0.0
    for name, size in population.items():
        rs = [r for r in results if is_checked(r) and (r["stratum"] == "after-7/17") == (name == "after")]
        if not rs:
            # A stratum nobody checked cannot be assumed clean (Codex): no estimate at all.
            return float("nan"), 0.0, 1.0
        n, k = len(rs), sum(has_error(r, kinds) for r in rs)
        w = size / total
        est += w * k / n
        # Agresti-Coull adjusted share for the variance, so an all-0 or all-1 stratum
        # still has width instead of a 0%-0% interval (Codex).
        pa = (k + 2) / (n + 4)
        var += w * w * pa * (1 - pa) / (n + 4)
    half = 1.96 * math.sqrt(var)
    return est, max(0.0, est - half), min(1.0, est + half)


def decision(lo: float, hi: float, checked: int) -> str:
    if checked == 0 or (lo, hi) == (0.0, 1.0):
        return "no estimate: an article stratum was not checked"
    if lo >= 0.20:
        return "≥20% of the old articles have a hard error (95% lower bound): list them for a noindex/removal plan"
    if hi < 0.05:
        return "<5% (95% upper bound): factual errors are not the main problem; look at duplication and AI tone next"
    return "between the thresholds: report only, no action recommended"


def load_results(rows_file: Path) -> list[dict]:
    """Results of the articles listed in one rows file (sample or census), skipping ones not yet audited."""
    slugs = [r["slug"] for r in json.loads(rows_file.read_text("utf-8"))["rows"]]
    return [json.loads((RESULTS / f"{s}.json").read_text("utf-8"))
            for s in sorted(slugs) if (RESULTS / f"{s}.json").exists()]


def cmd_census_report() -> int:
    """Every old article was audited, so these are counts, not estimates. They still carry the
    auditor's own error: Codex agreed with 77% of Sonnet's hard-error articles (data/audit/calibration.md)."""
    rows = json.loads(CENSUS.read_text("utf-8"))["rows"]
    results = load_results(CENSUS)
    groups: dict[str, list[dict]] = {"all": results}
    for r in results:
        groups.setdefault(r["stratum"], []).append(r)
        if is_checked(r):  # Fable: an article with unread sources can only show unsupported facts as undetermined
            groups.setdefault("all sources read" if r.get("all_read") else "some sources unread", []).append(r)
    missing = sorted({r["slug"] for r in rows} - {r["slug"] for r in results})
    lines = ["# Census audit of every old article (read-only)", "",
             f"{len(results)} of {len(rows)} old English articles audited"
             + (f"; **{len(missing)} NOT audited yet** (API error or budget stop; rerun `run --census`)" if missing else "")
             + ". Same verdicts as report.md; percentages are of checked articles. Not checked = no listed source "
             "could be read.", "",
             "| group | audited | checked | not checked | ≥1 hard error | % | ≥1 hard error or unsupported | % | "
             "factual sentences | hard errors | unsupported | undetermined |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for name in ["all"] + sorted(k for k in groups if k != "all"):
        s = summarize(groups[name])
        def pct(k: int) -> str:  # no checked article = no rate, not 0%
            return f"{k / s['checked']:.0%}" if s["checked"] else "—"
        lines.append(f"| {name} | {s['articles']} | {s['checked']} | {s['not_checked']} | "
                     f"{s['articles_with_hard_error']} | {pct(s['articles_with_hard_error'])} | "
                     f"{s['articles_with_any_error']} | {pct(s['articles_with_any_error'])} | "
                     f"{s['factual_units']} | {s['hard_error']} | {s['unsupported']} | {s['undetermined']} |")
    flagged = []
    for r in results:
        bad = [u for u in r.get("units", []) if u["verdict"] in HARD_OR_UNSUPPORTED]
        if bad:
            flagged.append({"slug": r["slug"], "date": r["date"], "all_read": r.get("all_read"),
                            "n_readable": r["n_readable"], "n_sources": r["n_sources"],
                            "units": [{k: u[k] for k in ("id", "where", "text", "verdict", "evidence")} for u in bad]})
    (AUDIT_DIR / "census-flagged.json").write_text(json.dumps(flagged, ensure_ascii=False, indent=1), "utf-8")
    lines += ["", f"{len(flagged)} articles with a hard error or unsupported sentence are listed in "
              "census-flagged.json (input for the correction plan)."]
    (AUDIT_DIR / "census.md").write_text("\n".join(lines) + "\n", "utf-8")
    print("\n".join(lines))
    return 1 if missing else 0


def cmd_report() -> int:
    results = load_results(SAMPLE)
    old = old_en_articles()
    population = {"before": sum(a["date"] < CLIFF for a in old), "after": sum(a["date"] >= CLIFF for a in old)}
    groups: dict[str, list[dict]] = {"all (unweighted)": results}
    for r in results:
        groups.setdefault("before 7/17" if r["stratum"] != "after-7/17" else "after 7/17", []).append(r)
        if is_checked(r):
            groups.setdefault("all sources read" if r["all_read"] else "some sources unread", []).append(r)
    lines = ["# Audit of the old articles (read-only)", "",
             "Hard error = a readable source says something different. Unsupported = every listed source was "
             "read and none states it. Undetermined = not in the readable sources while some listed source could "
             "not be read (not counted as an error). Sentence-level intervals treat sentences as independent, so "
             "they are narrower than the truth.", "",
             "| group | articles | checked | not checked | ≥1 hard error | 95% CI | ≥1 hard error or unsupported | "
             "95% CI | factual sentences | hard errors | unsupported | undetermined |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for name, rs in groups.items():
        s = summarize(rs)
        lo, hi = s["article_ci"]
        alo, ahi = s["any_ci"]
        lines.append(f"| {name} | {s['articles']} | {s['checked']} | {s['not_checked']} | "
                     f"{s['articles_with_hard_error']} | {lo:.0%}–{hi:.0%} | {s['articles_with_any_error']} | "
                     f"{alo:.0%}–{ahi:.0%} | {s['factual_units']} | {s['hard_error']} | {s['unsupported']} | "
                     f"{s['undetermined']} |")
    e, lo, hi = weighted(results, HARD, population)
    e2, lo2, hi2 = weighted(results, HARD_OR_UNSUPPORTED, population)
    lines += ["", f"Population: {population['before']} articles before 7/17, {population['after']} from 7/17 on.",
              f"**Weighted share of old articles with ≥1 hard error: {e:.0%} (95% CI {lo:.0%}–{hi:.0%}).**",
              f"Weighted share with ≥1 hard error or unsupported sentence: {e2:.0%} (95% CI {lo2:.0%}–{hi2:.0%}).",
              f"**Decision rule:** {decision(lo, hi, summarize(results)['checked'])}", "", "## Hard errors", ""]
    for r in results:
        for u in r.get("units", []):
            if u["verdict"] == "hard_error":
                lines.append(f"- `{r['slug']}` [{u['where']}] {u['text']} — {u['evidence']}")
    (AUDIT_DIR / "report.md").write_text("\n".join(lines) + "\n", "utf-8")
    print("\n".join(lines[:len(groups) + 12]))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sp = sub.add_parser("sample")
    sp.add_argument("--n", type=int, default=120)
    sp.add_argument("--seed", type=int, default=20261113)
    sub.add_parser("census")
    rp = sub.add_parser("run")
    rp.add_argument("--limit", type=int, default=0)
    rp.add_argument("--census", action="store_true")
    rp.add_argument("--shard", default="", help="i/n: run every n-th row starting at row i")
    rep = sub.add_parser("report")
    rep.add_argument("--census", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "sample":
        return cmd_sample(a.n, a.seed)
    if a.cmd == "census":
        return cmd_census()
    if a.cmd == "run":
        return cmd_run(a.limit, a.census, a.shard)
    return cmd_census_report() if a.census else cmd_report()


if __name__ == "__main__":
    sys.exit(main())

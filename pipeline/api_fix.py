"""Correct the sentences the census audit flagged in the old FAQ articles (local files only).

    python -m pipeline.api_fix run [--shard i/n] [--limit N] [--slugs a,b]
    python -m pipeline.api_fix report

Plan 2026-11-15 「FAQ 舊文照來源逐句修正」. For each article with a hard_error or unsupported sentence:
1. fix    — Sonnet rewrites or deletes each flagged sentence from the cached source texts, and may name
            knock-on sentences that a correction made wrong (`extra`).
2. verify — the audit prompt re-checks every sentence that stays; failures get one more fix round, then
            body sentences are deleted and title/summary/headings kept (the article is marked for a human).
3. zh     — matching edits in the Chinese version (exact, unique fragments only), then a check that it
            agrees with every English change; one retry, then the article is marked for a human.
4. write  — the new texts and the original files' hashes go to data/audit/fixes/<slug>.json as "writing"
            before the articles are touched, then the record becomes "done".
Only flagged and knock-on sentences change; every other byte of both files stays the same. Sentences the
audit could not settle ("undetermined") are never touched.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import uuid
from datetime import date, datetime
from pathlib import Path

import anthropic

from pipeline import api_gates as G
from pipeline.api_audit import AUDIT_DIR, AUDIT_SCHEMA, CENSUS, RESULTS, shard
from pipeline.api_daily import (ARTICLES, CACHE_DIR, LEDGER, PROMPTS, TPE, VERIFY_MODEL, BudgetExceeded, Ledger,
                                call_model, last_json, with_sources)

FIXES = AUDIT_DIR / "fixes"
FIX_DAY = date(2026, 11, 15)
FLAGGED = ("hard_error", "unsupported")
KEEP_OK = ("supported", "opinion")
TITLE_MAX = 120
MAX_DELETED_SHARE = 0.30  # more than this is no longer a correction; the article goes to a human instead
FM_RE = re.compile(r"\A---\n(.*?\n)---\n", re.S)
MARK_EN = "*Correction ("
MARK_ZH = "*更正（"

FIX_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["fixes", "extra"],
    "properties": {
        "fixes": {"type": "array", "items": {"type": "object", "additionalProperties": False,
                                             "required": ["id", "new_text"],
                                             "properties": {"id": {"type": "integer"}, "new_text": {"type": "string"}}}},
        "extra": {"type": "array", "items": {"type": "object", "additionalProperties": False,
                                             "required": ["old", "new_text", "why"],
                                             "properties": {"old": {"type": "string"}, "new_text": {"type": "string"},
                                                            "why": {"type": "string"}}}},
    },
}
ZH_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["edits"],
    "properties": {"edits": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["change", "old", "new"],
        "properties": {"change": {"type": "integer"}, "old": {"type": "string"}, "new": {"type": "string"}}}}},
}
ZH_CHECK_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["checks"],
    "properties": {"checks": {"type": "array", "items": {
        "type": "object", "additionalProperties": False, "required": ["change", "status", "evidence"],
        "properties": {"change": {"type": "integer"},
                       "status": {"type": "string", "enum": ["consistent", "still_old", "differs"]},
                       "evidence": {"type": "string"}}}}},
}


class Skip(Exception):
    """This change (or article) cannot be applied safely; it is recorded, not forced."""


# ---------- text surgery (pure) ----------

def read_raw(p: Path) -> str:
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def write_raw(p: Path, text: str) -> None:
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_doc(raw: str) -> tuple[str, str]:
    m = FM_RE.match(raw)
    if not m:
        raise Skip("no frontmatter block")
    return raw[:m.end()], raw[m.end():]


def fm_get(fm: str, key: str) -> str | None:
    m = re.search(r'(?m)^' + key + r': "((?:[^"\\]|\\.)*)"$', fm)
    if not m:
        return None
    try:
        return json.loads('"' + m.group(1) + '"')
    except json.JSONDecodeError:
        return None


def fm_set(fm: str, key: str, value: str) -> str:
    enc = json.dumps(value, ensure_ascii=False)
    new, n = re.subn(r'(?m)^' + key + r': ".*"$', lambda m: f"{key}: {enc}", fm, count=1)
    if n != 1:
        raise Skip(f"no {key} line")
    return new


def fm_modified(fm: str, day: date) -> str:
    stamp = f"modifiedAt: {day.isoformat()}T00:00:00Z"
    if re.search(r"(?m)^modifiedAt:", fm):
        return re.sub(r"(?m)^modifiedAt:.*$", lambda m: stamp, fm, count=1)
    new, n = re.subn(r"(?m)^(publishedAt:.*)$", lambda m: m.group(1) + "\n" + stamp, fm, count=1)
    if n != 1:
        raise Skip("no publishedAt line")
    return new


def delete_span(text: str, i: int, j: int) -> str:
    """Remove text[i:j] with one neighbouring space; drop the line if nothing (or only a list marker) is left."""
    before, after = text[:i], text[j:]
    if after.startswith(" "):
        after = after[1:]
    elif before.endswith(" "):
        before = before[:-1]
    ls = before.rfind("\n") + 1
    le = after.find("\n")
    le = len(after) if le < 0 else le
    if re.fullmatch(r"[ \t]*(?:[-*+]|\d+\.)?[ \t]*", before[ls:] + after[:le]):
        before, after = before[:ls], after[le + 1:]
        while before.endswith("\n\n") and after.startswith("\n"):
            after = after[1:]
    return before + after


def replace_once(text: str, old: str, new: str) -> str:
    n = text.count(old) if old else 0
    if n != 1:
        raise Skip(f"found {n} times")
    i = text.index(old)
    return text[:i] + new + text[i + len(old):] if new else delete_span(text, i, i + len(old))


def replace_heading(body: str, old: str, new: str) -> str:
    ms = list(re.finditer(r"(?m)^(#{1,6}[ \t]+)" + re.escape(old) + r"[ \t]*$", body))
    if len(ms) != 1:
        raise Skip(f"heading found {len(ms)} times")
    m = ms[0]
    return body[:m.start()] + m.group(1) + new + body[m.end():]


def apply_en(raw: str, changes: list[dict], strict: bool = True) -> tuple[str, str]:
    """changes: {kind: title|summary|heading|body, old, new}. strict: raise Skip if any cannot be placed;
    otherwise skip that change (e.g. a knock-on sentence overlapping a flagged one) and mark it `unplaced`."""
    fm, body = split_doc(raw)
    spans: list[tuple[int, int, dict]] = []  # located in the ORIGINAL body, so no change can land in another's output
    for c in changes:
        try:
            if c["kind"] in ("title", "summary"):
                if fm_get(fm, c["kind"]) != c["old"] or not c["new"]:
                    raise Skip(f"{c['kind']} does not match or would be empty")
                fm = fm_set(fm, c["kind"], c["new"])
                continue
            if c["kind"] == "heading":
                if not c["new"]:
                    raise Skip("a heading cannot be deleted")
                ms = list(re.finditer(r"(?m)^#{1,6}[ \t]+(" + re.escape(c["old"]) + r")[ \t]*$", body))
                if len(ms) != 1:
                    raise Skip(f"heading found {len(ms)} times")
                i, j = ms[0].start(1), ms[0].end(1)
            else:
                n = body.count(c["old"]) if c["old"] else 0
                if n != 1:
                    raise Skip(f"found {n} times")
                i = body.index(c["old"])
                j = i + len(c["old"])
            if any(i < b and a < j for a, b, _ in spans):
                raise Skip("overlaps another change")
            spans.append((i, j, c))
        except Skip as s:
            if strict:
                raise
            c["unplaced"] = str(s)
    for i, j, c in sorted(spans, key=lambda t: -t[0]):  # from the end, so earlier offsets stay valid
        body = body[:i] + c["new"] + body[j:] if c["new"] else delete_span(body, i, j)
    return fm, body


def finish(fm: str, body: str, note: str) -> str:
    return fm_modified(fm, FIX_DAY) + body.rstrip("\n") + "\n\n" + note + "\n"


def note_en(n: int) -> str:
    d = FIX_DAY
    return (f"*Correction ({d:%B} {d.day}, {d.year}): {n} {'sentence was' if n == 1 else 'sentences were'} "
            "corrected or removed to match the sources listed on this page.*")


def note_zh(n: int) -> str:
    d = FIX_DAY
    return f"*更正（{d.year} 年 {d.month} 月 {d.day} 日）：已依本頁列出的來源更正或刪除 {n} 處。*"


def apply_zh(raw: str, edits: list[dict]) -> tuple[str, str, list[str]]:
    """Apply {old, new} edits to the Chinese file; each `old` must occur exactly once. Returns (fm, body, problems)."""
    fm, body = split_doc(raw)
    problems = []
    for e in edits:
        old, new = e["old"], e["new"]
        try:
            # unique in the ORIGINAL file, so an earlier edit cannot redirect this one to another copy
            if not old or raw.count(old) != 1:
                raise Skip(f"found {raw.count(old) if old else 0} times in the original")
            if fm.count(old) == 1 and body.count(old) == 0:
                line = next((l for l in fm.splitlines() if old in l), "")
                if not re.match(r'^(title|summary): "', line) or not new:
                    raise Skip("frontmatter edit outside title/summary, or empty")
                fm = fm.replace(old, json.dumps(new, ensure_ascii=False)[1:-1], 1)
            else:
                if fm.count(old):
                    raise Skip("fragment occurs in the frontmatter and the body")
                body = replace_once(body, old, new)
        except Skip as s:
            problems.append(f"change {e.get('change')}: {s}")
    return fm, body, problems


# ---------- model steps ----------

def load_sources(slug: str) -> list[dict]:
    p = CACHE_DIR / "audit" / f"{slug}.json"
    out = []
    for s in json.loads(p.read_text("utf-8")):
        d = s.get("date")
        s["date"] = date.fromisoformat(str(d)[:10]) if d else None
        out.append(s)
    return out


def article_text(raw: str) -> str:
    fm, body = split_doc(raw)
    return f"TITLE: {fm_get(fm, 'title')}\nSUMMARY: {fm_get(fm, 'summary')}\n\n{body}"


def ask_fix(client, ledger, slug, sources, raw, units: list[dict], round_no: int, all_read: bool) -> dict:
    lines = [f"{u['id']}. [{u['where']}] ({u['verdict']}) {u['text']}\n   checker: {u['evidence']}" for u in units]
    user = (("ALL LISTED SOURCES WERE READ." if all_read else "SOME LISTED SOURCES COULD NOT BE READ.")
            + "\n\nTHE ARTICLE (as published):\n" + article_text(raw) + "\n\nFLAGGED SENTENCES (id, where, verdict, "
            "text, checker's evidence):\n" + "\n".join(lines))
    resp = call_model(client, ledger, f"fix:{slug}.{round_no}", VERIFY_MODEL,
                      system=(PROMPTS / "api_fix.md").read_text("utf-8"), messages=with_sources(sources, user),
                      max_tokens=16_000, effort="medium", schema=FIX_SCHEMA)
    if resp.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"fixer stopped with {resp.stop_reason}")
    return last_json(resp)


def ask_verify(client, ledger, slug, sources, article_date: str, items: list[dict]) -> dict[int, dict]:
    """items: {id, where, text}. Returns id -> {verdict, evidence} from the audit prompt."""
    user = (f"THE ARTICLE WAS PUBLISHED ON {article_date}.\nLISTED SOURCES THAT COULD NOT BE READ: not relevant here."
            "\n\nUNITS TO CHECK (id, where it sits, text):\n" + "\n".join(f"{i['id']}. [{i['where']}] {i['text']}" for i in items))
    resp = call_model(client, ledger, f"fixverify:{slug}", VERIFY_MODEL,
                      system=(PROMPTS / "api_audit.md").read_text("utf-8"), messages=with_sources(sources, user),
                      max_tokens=32_000, effort="high", schema=AUDIT_SCHEMA)
    if resp.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"verifier stopped with {resp.stop_reason}")
    return {v["id"]: v for v in last_json(resp)["verdicts"]}


def changes_text(changes: list[dict]) -> str:
    return "\n".join(f"{n}. OLD: {c['old']}\n   NEW: {c['new'] or 'DELETED'}" for n, c in enumerate(changes, 1))


def ask_zh(client, ledger, slug, zh_raw, changes, feedback: list[str] | None, round_no: int) -> list[dict]:
    user = "THE CHINESE ARTICLE:\n" + zh_raw + "\n\nENGLISH CHANGES:\n" + changes_text(changes)
    if feedback:
        user += "\n\nYOUR PREVIOUS EDITS LEFT THESE PROBLEMS; fix them:\n- " + "\n- ".join(feedback)
    resp = call_model(client, ledger, f"fixzh:{slug}.{round_no}", VERIFY_MODEL,
                      system=(PROMPTS / "api_fix_zh.md").read_text("utf-8"),
                      messages=[{"role": "user", "content": user}], max_tokens=12_000, effort="medium", schema=ZH_SCHEMA)
    if resp.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"zh editor stopped with {resp.stop_reason}")
    return last_json(resp)["edits"]


def ask_zh_check(client, ledger, slug, zh_text, changes) -> list[dict]:
    user = "THE CHINESE ARTICLE (after edits):\n" + zh_text + "\n\nENGLISH CHANGES:\n" + changes_text(changes)
    resp = call_model(client, ledger, f"fixzhcheck:{slug}", VERIFY_MODEL,
                      system=(PROMPTS / "api_fix_zh_check.md").read_text("utf-8"),
                      messages=[{"role": "user", "content": user}], max_tokens=12_000, effort="medium",
                      schema=ZH_CHECK_SCHEMA)
    if resp.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"zh checker stopped with {resp.stop_reason}")
    return last_json(resp)["checks"]


# ---------- one article ----------

def kind_of(where: str) -> str:
    return where if where in ("title", "summary", "heading") else "body"


def shape_problem(kind: str, new: str) -> str | None:
    if kind in ("title", "summary", "heading") and not new.strip():
        return f"the {kind} cannot be empty"
    if kind == "title" and len(new) > TITLE_MAX:
        return f"the title is longer than {TITLE_MAX} characters"
    return None


def fix_one(client, ledger: Ledger, slug: str) -> dict:
    rec_path = FIXES / f"{slug}.json"
    en_path, zh_path = ARTICLES / f"{slug}.md", ARTICLES / f"{slug[:-3]}-zh.md"
    audit = json.loads((RESULTS / f"{slug}.json").read_text("utf-8"))
    rec: dict = {"slug": slug, "status": "", "skipped": [], "needs_human": [], "changes": [], "zh": {}}
    # Some articles are stored with CRLF line ends: work on LF, write back with the file's own line ends.
    en_orig = read_raw(en_path)
    en_crlf = "\r\n" in en_orig
    en_raw = en_orig.replace("\r\n", "\n")
    if MARK_EN in en_raw:
        rec["status"] = "already-corrected"
        return rec
    fm, body = split_doc(en_raw)
    flagged = [u for u in audit.get("units", []) if u["verdict"] in FLAGGED]
    units = []
    for u in flagged:  # only units that sit verbatim, once, where the audit says
        k = kind_of(u["where"])
        try:
            if k in ("title", "summary"):
                if fm_get(fm, k) != u["text"]:
                    raise Skip(f"{k} differs from the audited text")
            elif k == "heading":
                replace_heading(body, u["text"], u["text"])
            elif body.count(u["text"]) != 1:
                raise Skip(f"found {body.count(u['text'])} times")
            units.append({**u, "kind": k})
        except Skip as s:
            rec["skipped"].append({"id": u["id"], "text": u["text"], "why": str(s)})
    if not units:
        rec["status"] = "nothing-to-fix"
        return rec
    sources = load_sources(slug)
    pool = [s["text"] for s in sources]
    all_read = bool(audit.get("all_read"))

    # 1. fix (+ knock-on sentences)
    out = ask_fix(client, ledger, slug, sources, en_raw, units, 1, all_read)
    new = {f["id"]: f["new_text"].strip() for f in out["fixes"]}
    items = {u["id"]: {"id": u["id"], "kind": u["kind"], "where": u["where"], "old": u["text"],
                       "new": new.get(u["id"], u["text"]), "verdict": u["verdict"], "evidence": u["evidence"],
                       "source": "flagged"} for u in units}
    next_id = max(u["id"] for u in audit["units"]) + 1
    taken = {u["text"] for u in units}
    for x in out.get("extra", []):
        old = x["old"].strip()
        kind = next((k for k in ("title", "summary") if fm_get(fm, k) == old), "body")
        if kind == "body" and old and re.search(r"(?m)^#{1,6}[ \t]+" + re.escape(old) + r"[ \t]*$", body):
            kind = "heading"
        if not old or old in taken or (kind == "body" and (
                body.count(old) != 1 or not any(old in s for s, _ in G.tagged_sentences(body)))):
            rec["skipped"].append({"extra": old, "why": "knock-on sentence not found once in the article"})
            continue
        taken.add(old)
        items[next_id] = {"id": next_id, "kind": kind, "where": kind if kind != "body" else "knock-on", "old": old,
                          "new": x["new_text"].strip(), "verdict": "knock-on", "evidence": x.get("why", ""),
                          "source": "extra"}
        next_id += 1

    # 2. verify every sentence that stays (numbers by program, facts by the audit prompt); one more round
    for round_no in (1, 2):
        problems: dict[int, str] = {}
        for it in items.values():
            p = shape_problem(it["kind"], it["new"])
            if p:
                problems[it["id"]] = p
            elif it["new"]:
                nums = G.check_numbers(it["new"], pool, "fix")
                if nums:
                    problems[it["id"]] = "; ".join(nums)
        check = [it for it in items.values() if it["new"] and it["id"] not in problems]
        if check:
            verdicts = ask_verify(client, ledger, slug, sources, audit["date"],
                                  [{"id": it["id"], "where": it["where"], "text": it["new"]} for it in check])
            for it in check:
                v = verdicts.get(it["id"])
                it["check"] = v["verdict"] if v else "unchecked"
                # An unchanged sentence the readable sources merely do not mention, in an article with unread
                # sources, is undetermined, not wrong: it stays (Fable: do not touch undetermined sentences).
                undetermined = (v and v["verdict"] == "not_in_sources" and not all_read and it["new"] == it["old"])
                if undetermined:
                    it["outcome"] = "kept: undetermined (some sources unread)"
                elif not v or v["verdict"] not in KEEP_OK:
                    problems[it["id"]] = (v or {}).get("evidence") or "not checked"
        if not problems:
            break
        if round_no == 1:
            redo = [{"id": i, "where": items[i]["where"], "verdict": "rejected", "text": items[i]["new"] or items[i]["old"],
                     "evidence": f"your correction was rejected: {reason}. Original sentence: {items[i]['old']}"}
                    for i, reason in problems.items()]
            again = ask_fix(client, ledger, slug, sources, en_raw, redo, 2, all_read)
            for f in again["fixes"]:
                if f["id"] in problems:
                    items[f["id"]]["new"] = f["new_text"].strip()
            continue
        # Titles and summaries are often framing ("the crisis nobody talks about"); a third try asks for a plain
        # factual one and is checked once more. Body sentences that failed twice are deleted.
        heads = [i for i in problems if items[i]["kind"] in ("title", "summary", "heading")]
        if heads:
            plain = [{"id": i, "where": items[i]["where"], "verdict": "rejected", "text": items[i]["new"] or items[i]["old"],
                      "evidence": f"rejected twice: {problems[i]}. Write a PLAIN, strictly factual {items[i]['kind']} "
                                  "using only facts the sources state (who did what, when, how much); no framing, no "
                                  "causes or judgements, no 'first/only/biggest'."} for i in heads]
            third = {f["id"]: f["new_text"].strip() for f in ask_fix(client, ledger, slug, sources, en_raw, plain, 3,
                                                                      all_read)["fixes"] if f["id"] in heads}
            ok_ids = [i for i in heads if third.get(i) and not shape_problem(items[i]["kind"], third[i])
                      and not G.check_numbers(third[i], pool, "fix")]
            if ok_ids:
                v3 = ask_verify(client, ledger, slug, sources, audit["date"],
                                [{"id": i, "where": items[i]["where"], "text": third[i]} for i in ok_ids])
                for i in ok_ids:
                    if (v3.get(i) or {}).get("verdict") in KEEP_OK:
                        items[i]["new"], items[i]["check"] = third[i], v3[i]["verdict"]
                        items[i]["outcome"] = "plain rewrite on the third try"
                        del problems[i]
        for i, why in problems.items():  # still failing: delete body sentences, keep the rest for a human
            it = items[i]
            if it["kind"] == "body":
                it["new"], it["outcome"] = "", f"deleted after two failed corrections ({why[:200]})"
            else:
                it["new"], it["outcome"] = it["old"], f"kept; correction failed three times ({why[:200]})"
                rec["needs_human"].append(f"en {it['kind']}: {it['old'][:120]}")

    changes = [it for it in items.values() if it["new"] != it["old"]]
    rec["changes"] = [{k: it.get(k) for k in ("id", "kind", "where", "source", "verdict", "evidence", "old", "new",
                                              "check", "outcome")} for it in changes]
    if not changes:
        rec["status"] = "no-change"
        return rec
    # The premise lives in the title and summary: if either could not be corrected, a "corrected" note would
    # mislead, so the article is left as it is for a human (noindex/removal decision) — Fable.
    if any(h.startswith(("en title", "en summary")) for h in rec["needs_human"]):
        rec["status"] = "not-written: title or summary could not be corrected"
        return rec
    n_body = len(G.tagged_sentences(body))
    n_deleted = sum(1 for c in changes if c["kind"] == "body" and not c["new"])
    if n_body and n_deleted / n_body > MAX_DELETED_SHARE:
        rec["status"] = f"not-written: would delete {n_deleted} of {n_body} body sentences"
        rec["needs_human"].append(f"en: too much to delete ({n_deleted}/{n_body}); consider noindex instead")
        return rec
    plan = [{"id": c["id"], "kind": c["kind"], "old": c["old"], "new": c["new"]} for c in changes]
    fm2, body2 = apply_en(en_raw, plan, strict=False)
    unplaced = {p["id"]: p for p in plan if "unplaced" in p}
    if any(p["kind"] in ("title", "summary") for p in unplaced.values()):
        rec["status"] = "not-written: title or summary change could not be placed"
        return rec
    rec["unplaced"] = [{"old": p["old"], "why": p["unplaced"]} for p in unplaced.values()]
    changes = [c for c in changes if c["id"] not in unplaced]
    rec["changes"] = [c for c in rec["changes"] if c["id"] not in unplaced]
    if not changes:
        rec["status"] = "no-change"
        return rec
    en_new = finish(fm2, body2, note_en(len(changes)))
    if en_crlf:
        en_new = en_new.replace("\n", "\r\n")

    # 3. Chinese: edits, program checks, model check, one retry
    zh_new = None
    if zh_path.exists():
        zh_orig = read_raw(zh_path)
        zh_crlf = "\r\n" in zh_orig
        zh_raw = zh_orig.replace("\r\n", "\n")
        en_pool = [article_text(en_new.replace("\r\n", "\n"))]
        feedback: list[str] | None = None
        for round_no in (1, 2):
            edits = ask_zh(client, ledger, slug, zh_raw, changes, feedback, round_no)
            good = []
            feedback = []
            for e in edits:
                bad = G.check_numbers(e["new"], en_pool, "zh") if e["new"] else []
                (feedback.append(f"change {e['change']}: {'; '.join(bad)}") if bad else good.append(e))
            zfm, zbody, problems = apply_zh(zh_raw, good)
            feedback += problems
            checks = ask_zh_check(client, ledger, slug, article_text(zfm + zbody), changes)
            feedback += [f"change {c['change']}: {c['status']} — {c['evidence']}" for c in checks
                         if c["status"] != "consistent"]
            missing = set(range(1, len(changes) + 1)) - {c["change"] for c in checks}
            feedback += [f"change {n}: not checked" for n in sorted(missing)]
            rec["zh"] = {"round": round_no, "edits": good, "problems": feedback}
            if not feedback:
                break
        n_zh = len(rec["zh"]["edits"])
        if feedback:
            rec["needs_human"].append("zh: " + " | ".join(feedback)[:600])
        if n_zh:
            zh_new = finish(zfm, zbody, note_zh(n_zh))
            if zh_crlf:
                zh_new = zh_new.replace("\n", "\r\n")
    else:
        rec["needs_human"].append("zh: no Chinese file")

    # 4. journal first, then the articles
    rec.update(status="writing", en_sha=sha(en_orig), en_new=en_new)
    if zh_new is not None:
        rec.update(zh_sha=sha(zh_orig), zh_new=zh_new)
    FIXES.mkdir(parents=True, exist_ok=True)
    rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), "utf-8")
    commit(rec)
    return rec


def commit(rec: dict) -> None:
    """Write the journalled texts if the originals are unchanged, then mark the record done."""
    slug = rec["slug"]
    en_path, zh_path = ARTICLES / f"{slug}.md", ARTICLES / f"{slug[:-3]}-zh.md"
    targets = [(en_path, rec["en_sha"], rec["en_new"])]
    if "zh_new" in rec:
        targets.append((zh_path, rec["zh_sha"], rec["zh_new"]))
    for path, old_sha, text in targets:
        cur = read_raw(path)
        if cur == text:
            continue
        if sha(cur) != old_sha:
            raise RuntimeError(f"{path.name} changed since the correction was planned; not overwriting")
        write_raw(path, text)
    rec["status"] = "done"
    (FIXES / f"{slug}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), "utf-8")


ZH_NOTE_RE = re.compile(r"\n\n\*更正（[^\n]*）：已依本頁列出的來源更正或刪除 (\d+) 處。\*\n?\Z")


def zh_problem_count(rec: dict) -> int:
    return sum(len(h[4:].split(" | ")) for h in rec["needs_human"] if h.startswith("zh:"))


def zh_only(client, ledger: Ledger, slug: str) -> str:
    """Second pass on the Chinese version of an article whose English is already corrected: start from the
    current Chinese text and the problems the first pass left, two more rounds, and write only if the number
    of problems went down. The English file is not touched."""
    rec_path = FIXES / f"{slug}.json"
    rec = json.loads(rec_path.read_text("utf-8"))
    before = zh_problem_count(rec)
    if rec["status"] != "done" or not before or rec.get("zh_pass2"):
        return "skip"
    zh_path, en_path = ARTICLES / f"{slug[:-3]}-zh.md", ARTICLES / f"{slug}.md"
    zh_orig = read_raw(zh_path)
    crlf = "\r\n" in zh_orig
    zh_cur = zh_orig.replace("\r\n", "\n")
    m = ZH_NOTE_RE.search(zh_cur)
    prev_n = int(m.group(1)) if m else 0
    zh_base = zh_cur[:m.start()] + "\n" if m else zh_cur
    en_pool = [article_text(read_raw(en_path).replace("\r\n", "\n"))]
    changes = [{"old": c["old"], "new": c["new"]} for c in rec["changes"]]
    feedback = [h[4:] for h in rec["needs_human"] if h.startswith("zh:")]
    best = None
    for round_no in (1, 2):
        edits = ask_zh(client, ledger, slug, zh_base, changes, feedback, 10 + round_no)
        good, feedback = [], []
        for e in edits:
            bad = G.check_numbers(e["new"], en_pool, "zh") if e["new"] else []
            (feedback.append(f"change {e['change']}: {'; '.join(bad)}") if bad else good.append(e))
        zfm, zbody, problems = apply_zh(zh_base, good)
        feedback += problems
        checks = ask_zh_check(client, ledger, slug, article_text(zfm + zbody), changes)
        feedback += [f"change {c['change']}: {c['status']} — {c['evidence']}" for c in checks if c["status"] != "consistent"]
        feedback += [f"change {n}: not checked" for n in sorted(set(range(1, len(changes) + 1)) - {c["change"] for c in checks})]
        if best is None or len(feedback) < len(best[3]):
            best = (zfm, zbody, good, list(feedback))
        if not feedback:
            break
    zfm, zbody, good, left = best
    if len(left) >= before or not good:
        rec["zh_pass2"] = {"written": False, "problems_before": before, "problems_after": len(left)}
        rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), "utf-8")
        return "not-better"
    new = finish(zfm, zbody, note_zh(prev_n + len(good)))
    if crlf:
        new = new.replace("\n", "\r\n")
    if read_raw(zh_path) != zh_orig:
        raise RuntimeError(f"{zh_path.name} changed during the pass; not overwriting")
    write_raw(zh_path, new)
    rec["needs_human"] = [h for h in rec["needs_human"] if not h.startswith("zh:")] + (
        ["zh: " + " | ".join(left)[:600]] if left else [])
    rec["zh_pass2"] = {"written": True, "edits": good, "problems_before": before, "problems_after": len(left)}
    rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), "utf-8")
    return f"better {before}->{len(left)}"


def cmd_zh(shard_spec: str, slugs: list[str]) -> int:
    today = datetime.now(TPE).date()
    run_id = f"{today.isoformat()}-fixzh-{uuid.uuid4().hex[:6]}"
    ledger = Ledger(LEDGER, "fix", run_id, today)
    client = anthropic.Anthropic(max_retries=2)
    todo = slugs or [r["slug"] for r in shard([{"slug": p.stem} for p in sorted(FIXES.glob("*.json"))], shard_spec)]
    for slug in todo:
        try:
            out = zh_only(client, ledger, slug)
        except BudgetExceeded as e:
            print(f"stop: {e}", file=sys.stderr)
            break
        except (Skip, RuntimeError, ValueError, KeyError, anthropic.APIError) as e:
            print(f"{slug}: error {type(e).__name__}: {e}", file=sys.stderr)
            continue
        if out != "skip":
            print(f"{slug}: {out}", flush=True)
    print(f"run {run_id}: US${ledger.run_spent():.2f}")
    return 0


# ---------- commands ----------

def targets() -> list[str]:
    rows = json.loads(CENSUS.read_text("utf-8"))["rows"]
    out = []
    for r in rows:
        p = RESULTS / f"{r['slug']}.json"
        if not p.exists():
            continue
        res = json.loads(p.read_text("utf-8"))
        if res.get("status") == "checked" and any(u["verdict"] in FLAGGED for u in res.get("units", [])):
            out.append(r["slug"])
    return sorted(out)


def cmd_run(limit: int, shard_spec: str, slugs: list[str]) -> int:
    today = datetime.now(TPE).date()
    run_id = f"{today.isoformat()}-fix-{uuid.uuid4().hex[:6]}"
    ledger = Ledger(LEDGER, "fix", run_id, today)
    client = anthropic.Anthropic(max_retries=2)
    todo = slugs or [r["slug"] for r in shard([{"slug": s} for s in targets()], shard_spec)]
    done = 0
    for slug in todo:
        rec_path = FIXES / f"{slug}.json"
        if rec_path.exists():
            rec = json.loads(rec_path.read_text("utf-8"))
            if rec.get("status") == "writing":
                try:
                    commit(rec)
                    print(f"{slug}: finished an interrupted write")
                except RuntimeError as e:
                    print(f"{slug}: {e}", file=sys.stderr)
            continue
        if limit and done >= limit:
            break
        try:
            rec = fix_one(client, ledger, slug)
        except BudgetExceeded as e:
            print(f"stop: {e}", file=sys.stderr)
            break
        except (Skip, RuntimeError, ValueError, KeyError, anthropic.APIError) as e:
            print(f"{slug}: error {type(e).__name__}: {e}", file=sys.stderr)
            continue  # no record, so the next run tries it again
        if rec["status"] != "done":
            FIXES.mkdir(parents=True, exist_ok=True)
            rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), "utf-8")
        done += 1
        print(f"{slug}: {rec['status']} changes {len(rec['changes'])} skipped {len(rec['skipped'])} "
              f"human {len(rec['needs_human'])}", flush=True)
    spent = sum(e["usd"] for e in ledger.entries if e["mode"] == "fix")
    print(f"run {run_id}: {done} articles, US${ledger.run_spent():.2f}; corrections total US${spent:.2f}")
    return 0


def cmd_report() -> int:
    recs = [json.loads(p.read_text("utf-8")) for p in sorted(FIXES.glob("*.json"))]
    by: dict[str, int] = {}
    for r in recs:
        k = r["status"].split(":")[0]
        by[k] = by.get(k, 0) + 1
    ch = [c for r in recs if r["status"] == "done" for c in r["changes"]]
    lines = ["# Corrections of old articles (local only)", "",
             f"Targets: {len(targets())} articles with a hard error or unsupported sentence; records: {len(recs)}.",
             f"Status: {by}",
             f"English changes: {len(ch)} — rewritten {sum(1 for c in ch if c['new'])}, deleted "
             f"{sum(1 for c in ch if not c['new'])}, knock-on {sum(1 for c in ch if c['source'] == 'extra')}.",
             f"Skipped sentences: {sum(len(r['skipped']) for r in recs)}; articles needing a human: "
             f"{sum(1 for r in recs if r['needs_human'])}.", "", "## Needs a human", ""]
    for r in recs:
        for h in r["needs_human"]:
            lines.append(f"- `{r['slug']}` {h}")
    (AUDIT_DIR / "fixes.md").write_text("\n".join(lines) + "\n", "utf-8")
    print("\n".join(lines[:7]))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    rp = sub.add_parser("run")
    rp.add_argument("--limit", type=int, default=0)
    rp.add_argument("--shard", default="")
    rp.add_argument("--slugs", default="")
    sub.add_parser("report")
    zp = sub.add_parser("zh", help="second pass on the Chinese versions the first pass left inconsistent")
    zp.add_argument("--shard", default="")
    zp.add_argument("--slugs", default="")
    a = ap.parse_args(argv)
    if a.cmd == "zh":
        return cmd_zh(a.shard, [s.strip() for s in a.slugs.split(",") if s.strip()])
    if a.cmd == "run":
        return cmd_run(a.limit, a.shard, [s.strip() for s in a.slugs.split(",") if s.strip()])
    return cmd_report()


if __name__ == "__main__":
    sys.exit(main())

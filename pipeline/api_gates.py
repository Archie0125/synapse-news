"""Pure checks for API-written articles. Nothing here does I/O.

Every gate returns a list of human-readable failures; an empty list means pass.
The failure strings are fed back to the writer on a rewrite, so they quote the
offending text.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta
from urllib.parse import urlparse

from pipeline.ingest.dedup import _normalize_url

CATEGORIES = {"ai-ml", "startups", "products", "policy", "industry", "developer-tools", "hardware"}

# From prompts/generate_analysis.md STYLE RULES.
BANNED_EN = [
    "delve", "crucial", "robust", "comprehensive", "nuanced", "leverage",
    "cutting-edge", "game-changer", "paradigm shift",
    "in a world where", "in recent years", "it remains to be seen",
]

# ---------------------------------------------------------------- text prep

_MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_URL = re.compile(r"https?://\S+")
_LIST_ENUM = re.compile(r"^(\s*(?:#{1,6}\s*|[-*]\s*)?)\d+[.)]\s", re.M)


# "[S1]", "[S1][S2]" and "[S1, S2]" / "[S1,S3]" all count.
_TAG = re.compile(r"\s?\[S\d+(?:\s*[,，;、]\s*S?\d+)*\]")


def tag_numbers(text: str) -> set[int]:
    return {int(n) for t in _TAG.findall(text) for n in re.findall(r"\d+", t)}


def strip_tags(text: str) -> str:
    """Remove the writer's [S1] source markers (they are for checking, not readers)."""
    return re.sub(r"[ \t]+([.,;:!?。，；：！？」)])", r"\1", _TAG.sub("", text))


def strip_markup(text: str) -> str:
    """Drop source markers, link targets, bare URLs and leading list/heading enumerators."""
    text = strip_tags(text)
    text = _MD_LINK.sub(r"\1", text)
    text = _URL.sub(" ", text)
    text = _LIST_ENUM.sub(r"\1", text)
    return text


_END = r"[.!?。！？]"


def tagged_sentences(body: str) -> list[tuple[str, set[int]]]:
    """Split a Markdown body into (sentence, source numbers) pairs. Markers
    written after the full stop ("…in 1993. [S1]") are moved before it first,
    so they stay with the sentence they belong to. Headings are skipped."""
    out = []
    for line in body.splitlines():
        s = line.strip()
        if not s or _HEADING.match(s) or s == "---":
            continue
        s = re.sub(r"(" + _END + r"[\"'”」)]?)((?:" + _TAG.pattern + r")+)", r"\2\1", s)
        # Chinese full stops need no following space; Latin ones do (so "1.5" survives).
        parts = [p for p in re.split(r"(?:(?<=[。！？])[」”]?\s*|(?<=[.!?])[\"'”)]?\s+)", s) if p.strip()]
        merged: list[str] = []
        for p in parts:  # "U.S." / "Inc." / "Mr." end an abbreviation, not a sentence
            if merged and _ABBREV_END.search(merged[-1]):
                merged[-1] += " " + p
            else:
                merged.append(p)
        for sent in merged:
            out.append((sent.strip(), tag_numbers(sent)))
    return out


_HEADING = re.compile(r"^#{1,6}\s")

_ABBREV_END = re.compile(r"(?:\b(?:[A-Z]\.){2,}|\b(?:Mr|Mrs|Ms|Dr|Inc|Corp|Co|Ltd|vs|St|Jr|Sr|No|Gen|Sen|Rep|"
                         r"Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.)$")


def sentences_for_review(d: dict) -> list[dict]:
    """Every checkable unit of a draft, numbered: titles and summaries whole,
    bodies sentence by sentence with their [S#] markers and the heading they sit
    under (a recap's day heading is part of the claim)."""
    out = []
    for lang in ("en", "zh"):
        for field in ("title", "summary"):
            out.append({"id": len(out) + 1, "lang": lang, "where": field, "text": d[f"{field}_{lang}"],
                        "sources": "any"})
        heading = ""
        for line in d[f"body_{lang}"].splitlines():
            s = line.strip()
            if _HEADING.match(s):
                heading = s.lstrip("# ").strip()
                # Headings state facts too ("Nvidia fires its CFO"): check them against any source.
                out.append({"id": len(out) + 1, "lang": lang, "where": "heading", "text": heading,
                            "sources": "any"})
                continue
            for sent, tags in tagged_sentences(s):
                out.append({"id": len(out) + 1, "lang": lang, "where": heading or "intro", "text": sent,
                            "sources": sorted(tags) or "none"})
    return out


def _needs_source(sent: str, lang: str) -> bool:
    plain = strip_markup(sent)
    if re.search(r"\d", plain) or re.search(r"[\"“”「」]", plain):
        return True
    words = plain.split()
    if lang == "en":
        return sum(1 for w in words[1:] if w[:1].isupper()) >= 1
    return (re.search(r"[A-Z][A-Za-z]", plain) is not None
            or re.search(r"[零〇一二兩两三四五六七八九十百千萬万億亿]{2,}", plain) is not None)


def check_citations(body: str, n_sources: int, label: str) -> list[str]:
    """Every sentence stating a figure, a quote or a name must carry a valid
    [S#] marker; untagged sentences are left for opinion."""
    fails = []
    for sent, tags in tagged_sentences(body):
        bad = [t for t in tags if not 1 <= t <= n_sources]
        if bad:
            fails.append(f"{label}: marker S{bad[0]} does not match any source: \"{sent[:120]}\"")
        elif not tags and _needs_source(sent, label):
            fails.append(f"{label}: factual sentence has no [S#] source marker: \"{sent[:160]}\"")
    return fails


def norm_ws(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- quantities

@dataclass(frozen=True)
class Qty:
    raw: str
    kind: str          # number | percent | multiple | date | month | time
    mantissa: float    # the number as written
    decimals: int      # decimals as written (for rounding comparisons)
    scale: float       # multiplier applied by the unit word

    @property
    def value(self) -> float:
        return self.mantissa * self.scale


_SCALE = {
    "thousand": 1e3, "k": 1e3, "千": 1e3,
    "million": 1e6, "m": 1e6, "mn": 1e6,
    "billion": 1e9, "b": 1e9, "bn": 1e9,
    "trillion": 1e12, "t": 1e12,
    "萬": 1e4, "万": 1e4, "億": 1e8, "亿": 1e8, "兆": 1e12,
}
_PERCENT = {"%", "percent", "per cent", "個百分點", "百分點", "percentage point", "percentage points"}
_MULTIPLE = {"x", "×", "倍", "-fold", "fold", "times"}

_UNIT_RE = (
    r"(?:\s?(%|percent\b|per cent\b|percentage points?\b|個百分點|百分點|×|x\b|-fold\b|倍|成|"
    r"thousand\b|million\b|billion\b|trillion\b|bn\b|mn\b|[kKmMbBtT]\b|萬|万|億|亿|兆|千))?"
)
# Digits not glued to a preceding letter/digit/dot (so "2012" never yields "12",
# "Q3"/"H100"/"v1.2" are skipped) and not glued to a following ASCII word char
# (so "4o" is skipped); CJK after the number is fine.
# Numbers glued to (or followed by) a technical unit: "10GW", "64 GB", "2nm". Compared
# together with the unit, so "10GW" is not supported by "1GW".
_NUM_TECH_RE = re.compile(
    r"(?<![A-Za-z0-9_.])(\d+(?:\.\d+)?)\s?(GB|TB|MB|PB|GW|MW|kW|kWh|MWh|GWh|TWh|nm|mm|cm|km|ms|GHz|MHz|Hz|"
    r"mAh|fps|Gbps|Mbps|TOPS|TFLOPS|PFLOPS|EFLOPS|W)(?![A-Za-z0-9_])", re.I)

# Case-insensitive so Title Case headlines ("$20 Billion") keep their unit.
_NUM_RE = re.compile(
    r"(?<![A-Za-z0-9_.])(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)" + _UNIT_RE + r"(?![A-Za-z0-9_])", re.I
)

_MONTHS = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"])}
_MONTHS.update({m[:3]: v for m, v in list(_MONTHS.items())})
_MONTHS["sept"] = 9
_MON = r"(january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sept|sep|oct|nov|dec)\.?"
_DATE_EN_MD = re.compile(_MON + r"\s+(\d{1,2})(?:st|nd|rd|th)?\b", re.I)
_DATE_EN_DM = re.compile(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+" + _MON + r"\b", re.I)
# Capitalised full names only: lowercase "march"/"may" are usually verbs.
_MONTH_ONLY_EN = re.compile(r"\b(January|February|March|April|June|July|August|September|October|November|December)\b")
_DATE_ZH = re.compile(r"(\d{1,2})\s*月\s*(\d{1,2})\s*[日號号]")
_MONTH_ZH = re.compile(r"(?<![\d.])(\d{1,2})\s*月(?!\s*\d)")
_DATE_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_DATE_SLASH = re.compile(r"(?<![\d/])(\d{1,2})/(\d{1,2})(?![\d/])")
_TIME = re.compile(r"\b(\d{1,2}):(\d{2})\b")

_EN_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100, "a hundred": 100,
}
_EN_WORD_QTY = re.compile(
    r"\b(" + "|".join(sorted(_EN_WORDS, key=len, reverse=True)) + r")"
    r"(?:[\s-]+(one|two|three|four|five|six|seven|eight|nine))?"
    r"\s+(hundred|thousand|million|billion|trillion|percent|times|-fold|fold)\b",
    re.I,
)
_ZH_DIGIT = {"零": 0, "〇": 0, "一": 1, "二": 2, "兩": 2, "两": 2, "三": 3, "四": 4, "五": 5,
             "六": 6, "七": 7, "八": 8, "九": 9}
_ZH_SMALL_UNIT = {"十": 10, "百": 100, "千": 1000}
# 數十億 / 幾倍 are deliberately vague ("several billion"), not a figure to check.
_ZH_NUM_QTY = re.compile(r"(?<![數数幾几])(百分之)?([零〇一二兩两三四五六七八九十百千]+)(成|倍|萬|万|億|亿|兆)?")


def _zh_int(s: str) -> int | None:
    total, current = 0, 0
    for ch in s:
        if ch in _ZH_DIGIT:
            current = _ZH_DIGIT[ch]
        elif ch in _ZH_SMALL_UNIT:
            total += (current or 1) * _ZH_SMALL_UNIT[ch]
            current = 0
        else:
            return None
    return total + current


def _unit_to(kind_default: str, unit: str | None) -> tuple[str, float]:
    if not unit:
        return kind_default, 1.0
    u = unit.lower().strip()
    if u in _PERCENT:
        return "percent", 1.0
    if u in _MULTIPLE:
        return "multiple", 1.0
    if u == "成":
        return "percent", 10.0
    return kind_default, _SCALE.get(u, 1.0)


_EN_SMALL = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|"
                       r"fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|"
                       r"sixty|seventy|eighty|ninety)\b", re.I)
_ZH_SMALL = re.compile(r"(?<![零〇一二兩两三四五六七八九十百千萬万億亿])([一二兩两三四五六七八九十]{1,3})(?=[個家款項種位名年月天週次倍成%])")


def extract_quantities(text: str, pool: bool = False) -> list[Qty]:
    """Every checkable quantity in `text` (EN or ZH).

    pool=True is for source text: it also reads small spelled-out numbers
    ("three locks", 三家), so an article that writes "3 locks" is supported.
    Articles are not held to their own spelled-out small numbers."""
    out_pool: list[Qty] = []
    if pool:
        for m in _EN_SMALL.finditer(text):
            out_pool.append(Qty(m.group(0), "number", float(_EN_WORDS[m.group(1).lower()]), 0, 1))
        for m in _ZH_SMALL.finditer(text):
            n = _zh_int(m.group(1))
            if n is not None:
                out_pool.append(Qty(m.group(0), "number", float(n), 0, 1))
    return out_pool + _extract(text)


def _extract(text: str) -> list[Qty]:
    text = strip_markup(text)
    out: list[Qty] = []
    spans: list[tuple[int, int]] = []

    def taken(a: int, b: int) -> bool:
        return any(a < y and x < b for x, y in spans)

    def add(m: re.Match, q: Qty) -> None:
        spans.append(m.span())
        out.append(q)

    for m in _DATE_ISO.finditer(text):
        add(m, Qty(m.group(0), "date", int(m.group(2)) * 100 + int(m.group(3)), 0, 1))
        spans.append(m.span())
        out.append(Qty(m.group(1), "number", float(m.group(1)), 0, 1))
    for rx, mi, di in ((_DATE_EN_MD, 1, 2), (_DATE_EN_DM, 2, 1)):
        for m in rx.finditer(text):
            if taken(*m.span()):
                continue
            mon = _MONTHS[m.group(mi).lower().rstrip(".")]
            add(m, Qty(m.group(0), "date", mon * 100 + int(m.group(di)), 0, 1))
    for m in _DATE_ZH.finditer(text):
        if not taken(*m.span()):
            add(m, Qty(m.group(0), "date", int(m.group(1)) * 100 + int(m.group(2)), 0, 1))
    for m in _DATE_SLASH.finditer(text):
        if not taken(*m.span()) and 1 <= int(m.group(1)) <= 12 and 1 <= int(m.group(2)) <= 31:
            add(m, Qty(m.group(0), "date", int(m.group(1)) * 100 + int(m.group(2)), 0, 1))
    for m in _MONTH_ZH.finditer(text):
        if not taken(*m.span()) and 1 <= int(m.group(1)) <= 12:
            add(m, Qty(m.group(0), "month", int(m.group(1)), 0, 1))
    for m in _TIME.finditer(text):
        if not taken(*m.span()):
            add(m, Qty(m.group(0), "time", int(m.group(1)) * 100 + int(m.group(2)), 0, 1))
    for m in _NUM_TECH_RE.finditer(text):
        if not taken(*m.span()):
            add(m, Qty(m.group(0), "u:" + m.group(2).lower(), float(m.group(1)),
                       len(m.group(1).split(".")[1]) if "." in m.group(1) else 0, 1))
    for m in _NUM_RE.finditer(text):
        if taken(*m.span()):
            continue
        num = m.group(1).replace(",", "")
        decimals = len(num.split(".")[1]) if "." in num else 0
        kind, scale = _unit_to("number", m.group(2))
        add(m, Qty(m.group(0).strip(), kind, float(num), decimals, scale))
    for m in _EN_WORD_QTY.finditer(text):
        if taken(*m.span()):
            continue
        n = _EN_WORDS[m.group(1).lower()] + (_EN_WORDS[m.group(2).lower()] if m.group(2) else 0)
        unit = m.group(3).lower()
        if unit == "hundred":
            kind, scale = "number", 100.0
        else:
            kind, scale = _unit_to("number", unit)
        add(m, Qty(m.group(0), kind, float(n), 0, scale))
    for m in _ZH_NUM_QTY.finditer(text):
        if taken(*m.span()):
            continue
        pct, digits, unit = m.group(1), m.group(2), m.group(3)
        if not pct and not unit and len(digits) < 2:
            continue  # bare 一/三 etc. are words, not quantities ("一個", "三家")
        if m.group(0) in ("千萬", "万一", "萬一", "一一"):
            continue  # adverbs: 千萬 = "by all means", 萬一 = "in case"
        n = _zh_int(digits)
        if n is None:
            continue
        if pct:
            add(m, Qty(m.group(0), "percent", float(n), 0, 1))
        else:
            kind, scale = _unit_to("number", unit)
            add(m, Qty(m.group(0), kind, float(n), 0, scale))
    for m in _MONTH_ONLY_EN.finditer(text):
        if not taken(*m.span()):
            add(m, Qty(m.group(0), "month", _MONTHS[m.group(1).lower()], 0, 1))
    return out


def _supported(q: Qty, pool: list[Qty]) -> bool:
    for s in pool:
        if q.kind in ("date", "time"):
            if s.kind == q.kind and s.mantissa == q.mantissa:
                return True
            continue
        if q.kind == "month":
            if (s.kind == "month" and s.mantissa == q.mantissa) or (
                    s.kind == "date" and int(s.mantissa) // 100 == q.mantissa):
                return True
            continue
        if s.kind != q.kind:
            continue
        if s.value == q.value:
            return True
        # Allow the article to round the source figure to the precision it wrote:
        # source 1.23 billion supports "1.2 billion" and "12 億".
        if q.scale and round(s.value / q.scale, q.decimals) == round(q.mantissa, q.decimals):
            # but never let rounding turn a non-zero into a different order of magnitude
            if q.mantissa != 0 and abs(s.value - q.value) <= abs(q.value) * 0.05:
                return True
    return False


def check_numbers(article: str, pool_texts: list[str], label: str) -> list[str]:
    pool = [q for t in pool_texts for q in extract_quantities(t, pool=True)]
    fails = []
    seen = set()
    for q in extract_quantities(article):
        if q.raw in seen:
            continue
        seen.add(q.raw)
        if not _supported(q, pool):
            fails.append(f"{label}: number「{q.raw}」not found in the sources")
    return fails


# ---------------------------------------------------------------- quotes

_EN_QUOTE = re.compile(r'"([^"\n]{3,600})"')
_ZH_QUOTE = re.compile(r"[「『]([^」』\n]{2,400})[」』]")


def _plain(s: str) -> str:
    s = norm_ws(s).lower()
    s = re.sub(r"[^\w\s']", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def en_quotes(text: str) -> list[str]:
    return [q for q in _EN_QUOTE.findall(norm_ws(strip_markup(text))) if len(q.split()) >= 4]


# 「」 also marks terms and UI labels (「Home 頁籤」); it is a quotation only when
# introduced by a speech verb or a colon just before it.
_ZH_SAID = re.compile(r"(說|表示|指出|寫道|強調|坦言|稱|提到|回應|透露|宣稱|直言|認為|形容|聲明|[：:])[，,]?\s*$")
_ZH_SAID_AFTER = re.compile(r"^[，,]?\s*\S{0,6}?(說|表示|指出|寫道|強調|坦言|稱|提到|回應|透露|宣稱|直言|聲明)")


def zh_quotes(text: str) -> list[str]:
    text = strip_markup(text)
    out = []
    for m in _ZH_QUOTE.finditer(text):
        before = text[max(0, m.start() - 8):m.start()].split("\n")[-1]
        after = text[m.end():m.end() + 10].split("\n")[0]
        if len(m.group(1)) >= 8 and (_ZH_SAID.search(before) or _ZH_SAID_AFTER.search(after)):
            out.append(m.group(1))
    return out


def check_quotes_en(article: str, sources: list[str], label: str) -> list[str]:
    src = " " + " ".join(_plain(s) for s in sources) + " "
    return [f"{label}: quote \"{q}\" does not appear word-for-word in any source"
            for q in en_quotes(article) if f" {_plain(q)} " not in src]


def check_quotes_zh(article_zh: str, quote_map: list[dict], sources: list[str]) -> list[str]:
    """A Chinese quotation must be either verbatim from a (Chinese) source, or
    declared in quote_map against an original that is verbatim in a source."""
    src_plain = " " + " ".join(_plain(s) for s in sources) + " "
    src_raw = "".join(re.sub(r"\s+", "", s) for s in sources)
    mapping = {re.sub(r"\s+", "", m.get("zh", "")): m.get("original", "") for m in quote_map}
    fails = []
    for q in zh_quotes(article_zh):
        key = re.sub(r"\s+", "", q)
        if key in src_raw:
            continue
        original = mapping.get(key)
        if original and f" {_plain(original)} " in src_plain:
            continue
        fails.append(f"zh: quote「{q}」is neither verbatim from a source nor mapped to a verbatim source quote")
    return fails


# ---------------------------------------------------------------- names

_NAME_STOP = {
    "the", "a", "an", "in", "on", "at", "but", "and", "or", "this", "that", "these", "those",
    "when", "for", "with", "after", "before", "while", "if", "as", "by", "from", "to", "its",
    "it", "why", "what", "how", "who", "here", "there", "still", "yet", "so", "also", "then",
    "now", "meanwhile", "however", "unlike", "like", "even", "only", "both", "each", "every",
    "neither", "nor", "not", "no", "our", "we", "they", "their", "his", "her", "one", "two",
    "if", "once", "until", "since", "because", "although", "though", "whether", "where",
}
_CALENDAR = set(_MONTHS) | {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
# A dot belongs to a word only inside it ("U.S", "Node.js"), so a sentence end
# breaks the sequence: "Android Police. Your" is two things, not one name.
_CAP_TOKEN = r"[A-Z](?:[\w&'-]|\.(?=\w))*"
_CAP_SEQ = re.compile(r"\b" + _CAP_TOKEN + r"(?:\s+(?:of|the|for|and|de|von|van|&)?\s*" + _CAP_TOKEN + r")+")


def check_names(article_en: str, sources: list[str]) -> list[str]:
    """Capitalised multi-word names must come from the sources: either the whole
    sequence appears, or every capitalised word in it appears as a word.
    `sources` should include the sources' site names and titles."""
    src = norm_ws(" ".join(sources))
    src_words = {w.rstrip(".") for w in re.findall(r"[\w&'.-]+", src)}
    fails = []
    body = norm_ws("\n".join(l for l in strip_markup(article_en).splitlines() if not l.lstrip().startswith("#")))
    for m in _CAP_SEQ.finditer(body):
        words = m.group(0).split()
        sentence_start = re.search(r"(^|[.!?:;]\s*[\"']?\s*)$", body[:m.start()]) is not None
        while words and words[0].lower().strip(".,") in _NAME_STOP:
            words = words[1:]
            sentence_start = False
        # A sentence's first word is capitalised anyway ("More Aliro locks…").
        if sentence_start and words and words[0] not in src_words:
            words = words[1:]
        caps = [w.strip(".,'") for w in words if w[:1].isupper()]
        caps = [w for w in caps if w.lower() not in _CALENDAR and w.lower() not in _NAME_STOP]
        if len(caps) < 2:
            continue
        seq = " ".join(words).strip(".,'")
        if seq in src:
            continue
        missing = [w for w in caps if w not in src_words and w.rstrip("'s") not in src_words]
        if missing:
            fails.append(f"en: name「{seq}」— {', '.join(missing)} not in any source")
    return fails


# ---------------------------------------------------------------- copying

def _strip_quotes(text: str) -> str:
    text = _EN_QUOTE.sub(" ", norm_ws(text))
    return _ZH_QUOTE.sub(" ", text)


def check_copy_en(article: str, sources: list[str], label: str, n: int = 12) -> list[str]:
    """Runs of n words shared with a source, ignoring quotations and runs that are
    mostly names or numbers (a list of product names is not copied prose)."""
    def words(t: str) -> list[str]:
        return re.findall(r"[\w']+", norm_ws(t).replace("’", "'"))

    def grams(ws: list[str]) -> set[tuple[str, ...]]:
        low = [w.lower() for w in ws]
        return {tuple(low[i:i + n]) for i in range(len(low) - n + 1)}
    src = set().union(*(grams(words(s)) for s in sources)) if sources else set()
    aw = words(_strip_quotes(strip_markup(article)))
    flagged = [False] * len(aw)
    for i in range(len(aw) - n + 1):
        run = aw[i:i + n]
        if tuple(w.lower() for w in run) not in src:
            continue
        if sum(1 for w in run if w[:1].isupper() or w[:1].isdigit()) >= n / 2:
            continue
        for j in range(i, i + n):
            flagged[j] = True
    # Merge overlapping windows into passages and list each one, so a fixer can find them.
    passages, start = [], None
    for i, f in enumerate(flagged + [False]):
        if f and start is None:
            start = i
        elif not f and start is not None:
            passages.append(" ".join(aw[start:i]))
            start = None
    return [f"{label}: copied from a source word for word, rephrase: \"{p}\"" for p in passages[:12]]


_CJK = re.compile(r"[㐀-鿿]")


def check_copy_zh(article_zh: str, sources: list[str], n: int = 20) -> list[str]:
    def squash(t: str) -> str:
        return re.sub(r"[^㐀-鿿0-9A-Za-z]", "", t)
    zh_sources = [squash(s) for s in sources if len(_CJK.findall(s)) > 200]
    if not zh_sources:
        return []
    joined = "\n".join(zh_sources)
    a = squash(_strip_quotes(strip_markup(article_zh)))
    for i in range(len(a) - n + 1):
        if a[i:i + n] in joined:
            return [f"zh: {n}+ characters copied from a source, e.g.「{a[i:i + n]}」"]
    return []


# ---------------------------------------------------------------- sources & freshness

def check_sources(used: list[dict], allowlist: set[str], min_count: int = 2,
                  min_total_words: int = 1200) -> list[str]:
    """`used`: [{url, final_url, words, ok}] for sources the article cites."""
    fails = []
    # Two search results that redirect to the same page are one source, not two outlets.
    good, seen = [], set()
    for s in used:
        final = _normalize_url(s.get("final_url") or s["url"])
        if s.get("ok") and final not in seen:
            seen.add(final)
            good.append(s)
    if len(good) < min_count:
        fails.append(f"sources: {len(good)} readable source(s), need {min_count}")
    domains = {urlparse(s.get("final_url") or s["url"]).netloc.lower().removeprefix("www.") for s in good}
    if len(domains) < min(2, min_count):
        fails.append("sources: all sources are from one domain")
    for s in used:
        if _normalize_url(s["url"]) not in allowlist:
            fails.append(f"sources: {s['url']} was not returned by this run's web search")
    total = sum(s.get("words", 0) for s in good)
    if total < min_total_words:
        fails.append(f"sources: only {total} words of source text, need {min_total_words}")
    return fails


def fresh_daily(source_dates: list[date | None], run_date: date, days: int = 2) -> list[str]:
    lo = run_date - timedelta(days=days)
    if any(d and lo <= d <= run_date for d in source_dates):
        return []
    shown = ", ".join(str(d) for d in source_dates if d) or "none"
    return [f"freshness: no source published between {lo} and {run_date} (dates found: {shown})"]


def item_fresh(event_date: date, source_dates: list[date | None], week_start: date,
               week_end: date) -> bool:
    """A weekly-recap item survives only if its own day is inside the week and at
    least one source's original date is within a day of it (and inside the week,
    so a Sunday story cannot be filed under the next Monday)."""
    if not (week_start <= event_date <= week_end):
        return False
    return any(d and abs((d - event_date).days) <= 1 and week_start - timedelta(days=1) <= d <= week_end
               for d in source_dates)


# ---------------------------------------------------------------- duplicates

def title_sim_en(a: str, b: str) -> float:
    wa, wb = set(_plain(a).split()), set(_plain(b).split())
    return len(wa & wb) / len(wa | wb) if wa and wb else 0.0


def title_sim_zh(a: str, b: str) -> float:
    def bi(s: str) -> set[str]:
        s = re.sub(r"\s+", "", s)
        return {s[i:i + 2] for i in range(len(s) - 1)}
    ba, bb = bi(a), bi(b)
    return len(ba & bb) / len(ba | bb) if ba and bb else 0.0


def check_duplicate(title_en: str, title_zh: str, tags: list[str], source_urls: list[str],
                    recent: list[dict], run_date: date) -> list[str]:
    """`recent`: [{title, lang, tags, sources:[url], date}] of existing articles."""
    fails = []
    mine = {_normalize_url(u) for u in source_urls}
    my_tags = {t.lower() for t in tags}
    for r in recent:
        used = {_normalize_url(u) for u in r.get("sources", [])}
        if mine & used:
            fails.append(f"duplicate: source already used by「{r['title']}」")
        if r["lang"] == "en" and title_sim_en(title_en, r["title"]) >= 0.6:
            fails.append(f"duplicate: title too close to「{r['title']}」")
        if r["lang"] == "zh" and title_sim_zh(title_zh, r["title"]) >= 0.6:
            fails.append(f"duplicate: title too close to「{r['title']}」")
        d = r.get("date")
        if d and (run_date - d).days <= 14 and my_tags:
            theirs = {t.lower() for t in r.get("tags", [])}
            if theirs and len(my_tags & theirs) / len(my_tags | theirs) >= 0.5:
                fails.append(f"duplicate: tags overlap heavily with「{r['title']}」({d})")
    return sorted(set(fails))


# ---------------------------------------------------------------- format

def count_en_words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][\w'-]*", strip_markup(text)))


def count_zh_chars(text: str) -> int:
    return len(_CJK.findall(text))


def check_format(d: dict, en_words: tuple[int, int], zh_chars: tuple[int, int],
                 related_ok: set[str], max_title: tuple[int, int] = (120, 120)) -> list[str]:
    """max_title leaves room for a prefix the site adds later (weekly recaps)."""
    fails = []
    for k, limit in (("title_en", max_title[0]), ("title_zh", max_title[1])):
        if not d.get(k) or len(d[k]) > limit:
            fails.append(f"format: {k} missing or over {limit} characters")
    for k in ("body_en", "body_zh", "summary_en", "summary_zh"):
        # Links are stripped before every gate, so a made-up URL would ship unchecked.
        if re.search(r"\]\(|https?://|www\.", d.get(k, "")):
            fails.append(f"format: {k} contains a link or URL; the site lists sources itself")
    for k in ("summary_en", "summary_zh"):
        if not d.get(k) or len(d[k]) > 400:
            fails.append(f"format: {k} missing or over 400 characters")
    if d.get("category") not in CATEGORIES:
        fails.append(f"format: category {d.get('category')!r} not allowed")
    if not 3 <= len(d.get("tags", [])) <= 8:
        fails.append("format: need 3–8 tags")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+){1,9}", d.get("slug", "")):
        fails.append("format: slug must be 2–10 lowercase ascii words joined by '-'")
    w = count_en_words(d.get("body_en", ""))
    if not en_words[0] <= w <= en_words[1]:
        fails.append(f"format: English body is {w} words, need {en_words[0]}–{en_words[1]}")
    c = count_zh_chars(d.get("body_zh", ""))
    if not zh_chars[0] <= c <= zh_chars[1]:
        fails.append(f"format: Chinese body is {c} characters, need {zh_chars[0]}–{zh_chars[1]}")
    if "what to watch" not in d.get("body_en", "").lower():
        fails.append("format: English body needs a 'What to Watch' section")
    if "值得關注" not in d.get("body_zh", ""):
        fails.append("format: Chinese body needs a「值得關注」section")
    low = " ".join([d.get("title_en", ""), d.get("summary_en", ""), d.get("body_en", "")]).lower()
    for b in BANNED_EN:
        if re.search(r"\b" + re.escape(b) + r"\b", low):
            fails.append(f"format: banned phrase「{b}」")
    for s in d.get("related_slugs", []):
        if s not in related_ok:
            fails.append(f"format: related slug {s!r} is not an existing article")
    return fails


def query_mentions_day(query: str, day: date) -> bool:
    q = query.lower()
    month = list(_MONTHS)[day.month - 1]
    pats = [
        day.isoformat(), f"{day.month}/{day.day}", f"{day.month}月{day.day}日",
        f"{month} {day.day}", f"{month[:3]} {day.day}", f"{day.day} {month}",
    ]
    return any(re.search(r"(?<!\d)" + re.escape(p) + r"(?!\d)", q) for p in pats)


def apply_edits(d: dict, edits: list[dict]) -> tuple[dict, list[str]]:
    """Apply {field, old, new} replacements; `old` must occur exactly once.
    Returns (new draft, problems). Unknown fields and missing/ambiguous text are
    reported, not guessed at."""
    out = dict(d)
    problems = []
    for e in edits:
        field, old, new = e.get("field"), e.get("old", ""), e.get("new", "")
        if field not in out or not isinstance(out[field], str):
            problems.append(f"edit: unknown field {field!r}")
            continue
        n = out[field].count(old) if old else 0
        if n != 1:
            problems.append(f"edit: text to replace occurs {n} times in {field}: {old[:80]!r}")
            continue
        out[field] = out[field].replace(old, new)
    for field in ("body_en", "body_zh", "summary_en", "summary_zh"):
        if isinstance(out.get(field), str):
            out[field] = re.sub(r"[ \t]+\n", "\n", re.sub(r"\n{3,}", "\n\n", out[field])).strip()
    return out, problems


def text_mentions_day(text: str, day: date) -> bool:
    """Does the text state this calendar day ("November 4", "Nov. 4", "4 November",
    "2026-11-04", "11月4日")?"""
    month = list(_MONTHS)[day.month - 1]
    pats = [
        rf"\b{month}\.?\s+{day.day}(?:st|nd|rd|th)?\b", rf"\b{month[:3]}\.?\s+{day.day}(?:st|nd|rd|th)?\b",
        rf"\b{day.day}(?:st|nd|rd|th)?\s+{month}\b", rf"\b{day.day}\s+{month[:3]}\b",
        re.escape(day.isoformat()), rf"(?<!\d){day.month}\s*月\s*{day.day}\s*日",
    ]
    return any(re.search(p, text, re.I) for p in pats)


_WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def source_states_day(text: str, published: date | None, day: date) -> bool:
    """Does a source place an event on `day`? Either it writes the date, or it is
    dated `day` and says "today", or it names that weekday and was published
    within the following six days (so "on Tuesday" can only mean that Tuesday)."""
    if text_mentions_day(text, day):
        return True
    if published is None:
        return False
    gap = (published - day).days
    if gap == 0 and re.search(r"\btoday\b|今天|今日", text, re.I):
        return True
    wd = _WEEKDAYS[day.weekday()]
    return 0 <= gap <= 6 and re.search(rf"\b(?:on|last|this)\s+{wd}\b", text, re.I) is not None

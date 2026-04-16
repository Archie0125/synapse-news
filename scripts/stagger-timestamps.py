"""Stagger article publishedAt timestamps by 5 minutes within each day.

Reads every markdown file in src/content/articles/, groups by (date, base_slug)
where base_slug strips the trailing -en/-zh. Within each date, pairs are ordered
alphabetically by base_slug and assigned timestamps starting from 09:00 UTC with
a 5-minute increment. EN and ZH of the same story share the same timestamp.

Idempotent: re-running produces identical output.

Usage:
    python scripts/stagger-timestamps.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "src" / "content" / "articles"
BASE_HOUR = 9
BASE_MINUTE = 0
STEP_MINUTES = 5

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
PUBLISHED_RE = re.compile(r"^publishedAt:\s*(.+)$", re.MULTILINE)
DATE_ONLY_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
DATETIME_RE = re.compile(
    r"^(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2}):(\d{2})(?:\.\d+)?(Z|[+-]\d{2}:?\d{2})?$"
)


def parse_published_value(raw: str) -> datetime:
    raw = raw.strip().strip('"').strip("'")
    if m := DATE_ONLY_RE.match(raw):
        y, mo, d = map(int, m.groups())
        return datetime(y, mo, d, tzinfo=timezone.utc)
    if m := DATETIME_RE.match(raw):
        y, mo, d, hh, mm, ss = (int(g) for g in m.groups()[:6])
        return datetime(y, mo, d, hh, mm, ss, tzinfo=timezone.utc)
    raise ValueError(f"Unrecognized publishedAt value: {raw!r}")


def base_slug_of(path: Path) -> str:
    name = path.stem
    for suffix in ("-en", "-zh"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def load_frontmatter(path: Path) -> tuple[str, str, str]:
    """Return (pre_fm, frontmatter_body, rest). pre_fm is always empty on valid files."""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError(f"No frontmatter found: {path}")
    return text[: m.start()], m.group(1), text[m.end():]


def write_frontmatter(path: Path, pre: str, body: str, rest: str) -> None:
    path.write_text(f"{pre}---\n{body}\n---\n{rest}", encoding="utf-8")


def replace_published(body: str, new_value: str) -> str:
    new_line = f"publishedAt: {new_value}"
    if not PUBLISHED_RE.search(body):
        raise ValueError("publishedAt field not found in frontmatter")
    return PUBLISHED_RE.sub(new_line, body, count=1)


def extract_published(body: str) -> str:
    m = PUBLISHED_RE.search(body)
    if not m:
        raise ValueError("publishedAt not found")
    return m.group(1).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing")
    args = parser.parse_args()

    if not ARTICLES_DIR.exists():
        print(f"Articles directory not found: {ARTICLES_DIR}", file=sys.stderr)
        return 1

    files = sorted(ARTICLES_DIR.glob("*.md"))
    if not files:
        print("No articles found", file=sys.stderr)
        return 1

    # Group by (date, base_slug) → list of file paths (EN + ZH pair)
    groups: dict[tuple[str, str], list[Path]] = defaultdict(list)
    loaded: dict[Path, tuple[str, str, str, str]] = {}

    for path in files:
        pre, body, rest = load_frontmatter(path)
        published_raw = extract_published(body)
        dt = parse_published_value(published_raw)
        date_key = dt.strftime("%Y-%m-%d")
        slug = base_slug_of(path)
        groups[(date_key, slug)].append(path)
        loaded[path] = (pre, body, rest, published_raw)

    # For each date, sort base_slugs alphabetically and assign staggered timestamps
    by_date: dict[str, list[str]] = defaultdict(list)
    for date_key, slug in groups:
        by_date[date_key].append(slug)
    for slugs in by_date.values():
        slugs.sort()

    changed = 0
    unchanged = 0
    per_day: dict[str, int] = {}

    for date_key in sorted(by_date):
        slugs = by_date[date_key]
        per_day[date_key] = len(slugs)
        base_date = datetime.strptime(date_key, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        for idx, slug in enumerate(slugs):
            offset = BASE_MINUTE + idx * STEP_MINUTES
            stamp_dt = base_date.replace(hour=BASE_HOUR) + timedelta(minutes=offset)
            new_value = stamp_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

            for path in groups[(date_key, slug)]:
                pre, body, rest, old_value = loaded[path]
                if old_value == new_value:
                    unchanged += 1
                    continue
                new_body = replace_published(body, new_value)
                if not args.dry_run:
                    write_frontmatter(path, pre, new_body, rest)
                changed += 1
                print(f"  {path.name}: {old_value}  ->  {new_value}")

    print()
    print(f"Articles: {len(files)}  Changed: {changed}  Unchanged: {unchanged}")
    print(f"Days: {len(per_day)}")
    for date_key in sorted(per_day):
        pairs = per_day[date_key]
        span = (pairs - 1) * STEP_MINUTES if pairs > 0 else 0
        last_time = (datetime.strptime(date_key, "%Y-%m-%d").replace(hour=BASE_HOUR) + timedelta(minutes=span)).strftime("%H:%M")
        print(f"  {date_key}: {pairs} pair(s), spans {BASE_HOUR:02d}:{BASE_MINUTE:02d}-{last_time}")

    if args.dry_run:
        print("\n(dry run — no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

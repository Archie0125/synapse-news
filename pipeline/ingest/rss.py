"""RSS feed fetcher with conditional GET support."""

import asyncio
import json
import logging
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from time import struct_time
from typing import Optional

import feedparser
import httpx
import yaml

logger = logging.getLogger(__name__)


@dataclass
class FeedItem:
    title: str
    url: str
    published: str  # ISO 8601
    summary: str
    source_slug: str
    source_name: str
    category: str

    def to_dict(self):
        return asdict(self)


@dataclass
class FeedConfig:
    name: str
    slug: str
    url: str
    category: str


def _parse_date(entry) -> str:
    """Extract and normalize publish date from feed entry."""
    for attr in ("published_parsed", "updated_parsed"):
        parsed = getattr(entry, attr, None)
        if parsed and isinstance(parsed, struct_time):
            dt = datetime(*parsed[:6], tzinfo=timezone.utc)
            return dt.isoformat()
    return datetime.now(timezone.utc).isoformat()


def _load_feeds_state(state_path: Path) -> dict:
    if state_path.exists():
        return json.loads(state_path.read_text(encoding="utf-8"))
    return {}


def _save_feeds_state(state_path: Path, state: dict):
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")


async def fetch_feed(
    client: httpx.AsyncClient,
    feed: FeedConfig,
    state: dict,
    max_items: int = 20,
) -> list[FeedItem]:
    """Fetch a single RSS feed, respecting ETag/Last-Modified."""
    headers = {}
    feed_state = state.get(feed.slug, {})
    if etag := feed_state.get("etag"):
        headers["If-None-Match"] = etag
    if modified := feed_state.get("last_modified"):
        headers["If-Modified-Since"] = modified

    try:
        resp = await client.get(feed.url, headers=headers, follow_redirects=True)
        if resp.status_code == 304:
            logger.info(f"[{feed.slug}] Not modified, skipping")
            return []
        resp.raise_for_status()
    except httpx.HTTPError as e:
        logger.warning(f"[{feed.slug}] Fetch failed: {e}")
        return []

    # Update state
    new_state = {}
    if etag_val := resp.headers.get("etag"):
        new_state["etag"] = etag_val
    if mod_val := resp.headers.get("last-modified"):
        new_state["last_modified"] = mod_val
    new_state["last_fetch"] = datetime.now(timezone.utc).isoformat()
    state[feed.slug] = new_state

    parsed = feedparser.parse(resp.text)
    items = []
    for entry in parsed.entries[:max_items]:
        title = getattr(entry, "title", "").strip()
        link = getattr(entry, "link", "").strip()
        summary = getattr(entry, "summary", "").strip()
        if not title or not link:
            continue
        # Strip HTML from summary
        if "<" in summary:
            from html import unescape
            import re
            summary = unescape(re.sub(r"<[^>]+>", "", summary))
        items.append(FeedItem(
            title=title,
            url=link,
            published=_parse_date(entry),
            summary=summary[:500],
            source_slug=feed.slug,
            source_name=feed.name,
            category=feed.category,
        ))

    logger.info(f"[{feed.slug}] Fetched {len(items)} items")
    return items


async def fetch_all_feeds(config_path: str = "config.yaml") -> list[FeedItem]:
    """Fetch all configured RSS feeds."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    feeds = [FeedConfig(**f) for f in config["feeds"]]
    max_items = config.get("pipeline", {}).get("max_articles_per_feed", 20)
    delay = config.get("pipeline", {}).get("fetch_delay_seconds", 1.0)

    state_path = Path(config["paths"]["raw"]) / "feeds_state.json"
    state = _load_feeds_state(state_path)

    all_items = []
    async with httpx.AsyncClient(timeout=30.0) as client:
        for feed in feeds:
            items = await fetch_feed(client, feed, state, max_items)
            all_items.extend(items)
            await asyncio.sleep(delay)

    _save_feeds_state(state_path, state)
    logger.info(f"Total fetched: {len(all_items)} items from {len(feeds)} feeds")
    return all_items

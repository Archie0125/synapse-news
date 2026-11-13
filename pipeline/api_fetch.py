"""Polite source fetching for the API pipeline.

- Only URLs the caller passes (the pipeline passes web-search results only).
- robots.txt is checked for every hop, redirects are followed by hand (max 3),
  http/https only.
- Bodies are streamed with a hard byte cap; 403/429 are final (no retry, no
  workaround).
- The publication date comes from page metadata only (htmldate without the
  extensive body scan), preferring the original date over "last modified".
"""

from __future__ import annotations

import time
import urllib.robotparser
from datetime import date, datetime
from urllib.parse import urljoin, urlparse

import httpx
import trafilatura

UA = "FAQ.com.tw-newsbot/1.0 (+https://faq.com.tw)"
MAX_BYTES = 2_000_000
ROBOTS_MAX_BYTES = 500_000
MAX_HOPS = 3
PER_HOST_DELAY = 2.0


class Fetcher:
    def __init__(self, client: httpx.Client | None = None, sleep=time.sleep):
        self.client = client or httpx.Client(timeout=20.0, headers={"User-Agent": UA})
        self.sleep = sleep
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}
        self._last_hit: dict[str, float] = {}

    # -- robots -------------------------------------------------------------

    def _read_capped(self, url: str, cap: int) -> tuple[int, bytes | None, str | None]:
        """GET without following redirects; returns (status, body or None, location)."""
        self._polite(url)
        with self.client.stream("GET", url, follow_redirects=False) as r:
            if r.is_redirect:
                return r.status_code, None, r.headers.get("location")
            if r.status_code != 200:
                return r.status_code, None, None
            buf = bytearray()
            for chunk in r.iter_bytes():
                buf += chunk
                if len(buf) > cap:
                    return -1, None, None
            return 200, bytes(buf), None

    def robots_allows(self, url: str) -> bool:
        p = urlparse(url)
        origin = f"{p.scheme}://{p.netloc}"
        if origin not in self._robots:
            rp = urllib.robotparser.RobotFileParser()
            status, body, robots_url = 0, None, origin + "/robots.txt"
            try:
                for _ in range(MAX_HOPS + 1):  # RFC 9309: follow robots.txt redirects
                    status, body, location = self._read_capped(robots_url, ROBOTS_MAX_BYTES)
                    if not location:
                        break
                    robots_url = urljoin(robots_url, location)
                    if urlparse(robots_url).scheme not in ("http", "https"):
                        status = 0
                        break
                else:
                    status = 0
            except httpx.HTTPError:
                status, body = 0, None
            if status == 200 and body is not None:
                rp.parse(body.decode("utf-8", "replace").splitlines())
            elif status in (401, 403):
                rp.disallow_all = True
            elif status == 429:
                rp.disallow_all = True
            elif 400 <= status < 500:
                rp.allow_all = True
            else:  # network error, 5xx, oversized or a redirect we won't chase: be conservative
                rp.disallow_all = True
            self._robots[origin] = rp
        return self._robots[origin].can_fetch(UA, url)

    def _polite(self, url: str) -> None:
        host = urlparse(url).netloc
        wait = self._last_hit.get(host, 0) + PER_HOST_DELAY - time.monotonic()
        if wait > 0:
            self.sleep(wait)
        self._last_hit[host] = time.monotonic()

    # -- pages --------------------------------------------------------------

    def fetch(self, url: str) -> dict:
        """Returns {url, final_url, ok, reason, text, words, date, title}."""
        out = {"url": url, "final_url": url, "ok": False, "reason": "", "text": "", "words": 0,
               "date": None, "title": "", "site": ""}
        current = url
        for _ in range(MAX_HOPS + 1):
            if urlparse(current).scheme not in ("http", "https"):
                out["reason"] = "non-http redirect"
                return out
            if not self.robots_allows(current):
                out["reason"] = f"robots.txt disallows {current}"
                return out
            try:
                status, body, location = self._read_capped(current, MAX_BYTES)
            except httpx.HTTPError as e:
                out["reason"] = f"network error: {type(e).__name__}"
                return out
            if location:
                current = urljoin(current, location)
                out["final_url"] = current
                continue
            if status == -1:
                out["reason"] = f"page larger than {MAX_BYTES} bytes"
                return out
            if status != 200 or body is None:
                out["reason"] = f"HTTP {status}"
                return out
            break
        else:
            out["reason"] = "too many redirects"
            return out

        html = body.decode("utf-8", "replace")
        text = trafilatura.extract(html, output_format="txt", favor_precision=True,
                                   include_comments=False, include_tables=True) or ""
        out["text"] = text
        out["words"] = len(text.split()) if not _mostly_cjk(text) else len(text) // 2
        out["date"], out["title"], out["site"] = page_meta(html, current)
        out["ok"] = len(text) >= 300
        if not out["ok"]:
            out["reason"] = "too little readable text"
        return out


def _mostly_cjk(text: str) -> bool:
    cjk = sum(1 for ch in text if "㐀" <= ch <= "鿿")
    return cjk > len(text) * 0.3


def page_meta(html: str, url: str = "") -> tuple[date | None, str, str]:
    """(original publication date, title, site name) from page metadata only — not body
    text, not last-modified. Third-party HTML can make the parser raise; a page
    we cannot date simply cannot prove freshness."""
    try:
        meta = trafilatura.extract_metadata(
            html, default_url=url or None, extensive=False,
            date_config={"original_date": True, "extensive_search": False,
                         "max_date": datetime.now().strftime("%Y-%m-%d")},
        )
    except (ValueError, TypeError, AttributeError):
        return None, "", ""
    if not meta:
        return None, "", ""
    title, site = meta.title or "", meta.sitename or ""
    try:
        return (date.fromisoformat(meta.date[:10]) if meta.date else None), title, site
    except ValueError:
        return None, title, site

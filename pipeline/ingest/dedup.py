"""Three-layer deduplication: URL, title similarity, content SimHash."""

import hashlib
import json
import logging
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

logger = logging.getLogger(__name__)


def _normalize_url(url: str) -> str:
    """Strip tracking params, normalize for comparison."""
    parsed = urlparse(url.lower().rstrip("/"))
    params = parse_qs(parsed.query)
    # Remove tracking parameters
    clean_params = {
        k: v for k, v in params.items()
        if not k.startswith("utm_") and k not in ("ref", "source", "campaign")
    }
    clean_query = urlencode(clean_params, doseq=True)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", clean_query, ""))


def _hash_string(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def _clean_title(title: str) -> str:
    """Lowercase, strip punctuation for comparison."""
    return re.sub(r"[^\w\s]", "", title.lower()).strip()


def _title_similarity(a: str, b: str) -> float:
    """Simple Jaccard similarity on word sets."""
    words_a = set(a.split())
    words_b = set(b.split())
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    union = words_a | words_b
    return len(intersection) / len(union)


def _simhash(text: str, hashbits: int = 64) -> int:
    """Compute a 64-bit SimHash of text."""
    words = text.lower().split()[:500]
    v = [0] * hashbits
    for word in words:
        h = int(hashlib.md5(word.encode()).hexdigest(), 16)
        for i in range(hashbits):
            bitmask = 1 << i
            if h & bitmask:
                v[i] += 1
            else:
                v[i] -= 1
    fingerprint = 0
    for i in range(hashbits):
        if v[i] >= 0:
            fingerprint |= 1 << i
    return fingerprint


def _hamming_distance(a: int, b: int) -> int:
    """Count differing bits between two integers."""
    return bin(a ^ b).count("1")


class Deduplicator:
    def __init__(self, state_path: str = "data/dedup/seen_hashes.json"):
        self.state_path = Path(state_path)
        self.state = self._load()

    def _load(self) -> dict:
        if self.state_path.exists():
            return json.loads(self.state_path.read_text(encoding="utf-8"))
        return {"urls": {}, "titles": {}, "simhashes": {}}

    def save(self):
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(
            json.dumps(self.state, indent=2), encoding="utf-8"
        )

    def prune(self, max_age_days: int = 30):
        """Remove entries older than max_age_days."""
        cutoff = (datetime.now(timezone.utc) - timedelta(days=max_age_days)).isoformat()
        for store_name in ("urls", "titles", "simhashes"):
            store = self.state.get(store_name, {})
            self.state[store_name] = {
                k: v for k, v in store.items()
                if v.get("added", "") > cutoff
            }

    def is_duplicate(self, url: str, title: str, content: str = "") -> bool:
        """Check all three layers. Returns True if duplicate."""
        now = datetime.now(timezone.utc).isoformat()

        # Layer 1: URL
        norm_url = _normalize_url(url)
        url_hash = _hash_string(norm_url)
        if url_hash in self.state.get("urls", {}):
            logger.debug(f"Duplicate URL: {url}")
            return True

        # Layer 2: Title similarity
        clean = _clean_title(title)
        for existing_title in self.state.get("titles", {}).values():
            if _title_similarity(clean, existing_title.get("clean", "")) > 0.85:
                logger.debug(f"Duplicate title: {title}")
                return True

        # Layer 3: Content SimHash (if content available)
        if content and len(content) > 200:
            sh = _simhash(content)
            for existing in self.state.get("simhashes", {}).values():
                if _hamming_distance(sh, existing.get("hash", 0)) < 5:
                    logger.debug(f"Duplicate content (SimHash): {title}")
                    return True
            # Store simhash
            content_hash = _hash_string(content[:500])
            self.state.setdefault("simhashes", {})[content_hash] = {
                "hash": sh, "added": now
            }

        # Not a duplicate - register it
        self.state.setdefault("urls", {})[url_hash] = {"added": now}
        title_hash = _hash_string(clean)
        self.state.setdefault("titles", {})[title_hash] = {
            "clean": clean, "added": now
        }

        return False

    def deduplicate(self, items: list) -> list:
        """Filter a list of FeedItems, removing duplicates."""
        unique = []
        for item in items:
            if not self.is_duplicate(item.url, item.title):
                unique.append(item)
        logger.info(f"Dedup: {len(items)} -> {len(unique)} ({len(items) - len(unique)} duplicates)")
        self.save()
        return unique

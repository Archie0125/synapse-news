"""Full article extraction using trafilatura with BeautifulSoup fallback."""

import logging
from datetime import datetime, timezone

import httpx
import trafilatura
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


async def extract_article(client: httpx.AsyncClient, url: str) -> str | None:
    """Fetch URL and extract clean article text as markdown."""
    try:
        resp = await client.get(url, follow_redirects=True)
        resp.raise_for_status()
        html = resp.text
    except httpx.HTTPError as e:
        logger.warning(f"Failed to fetch {url}: {e}")
        return None

    # Primary: trafilatura
    text = trafilatura.extract(
        html,
        output_format="markdown",
        include_links=True,
        favor_precision=True,
    )
    if text and len(text) > 100:
        return text

    # Fallback: BeautifulSoup article tag
    logger.info(f"Trafilatura failed for {url}, trying BeautifulSoup fallback")
    try:
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article")
        if article:
            # Strip scripts, styles, nav
            for tag in article.find_all(["script", "style", "nav", "aside"]):
                tag.decompose()
            text = article.get_text(separator="\n\n", strip=True)
            if len(text) > 100:
                return text
    except Exception as e:
        logger.warning(f"BeautifulSoup fallback failed for {url}: {e}")

    logger.warning(f"Could not extract content from {url}")
    return None


async def scrape_articles(
    items: list,
    timeout: float = 30.0,
) -> list[dict]:
    """Scrape full article content for a list of FeedItems.

    Returns list of dicts with FeedItem fields + 'content' and 'word_count'.
    """
    results = []
    async with httpx.AsyncClient(timeout=timeout) as client:
        for item in items:
            content = await extract_article(client, item.url)
            if content:
                results.append({
                    **item.to_dict(),
                    "content": content,
                    "word_count": len(content.split()),
                    "fetched": datetime.now(timezone.utc).isoformat(),
                    "status": "raw",
                })
            else:
                logger.info(f"Skipping (no content): {item.title}")

    logger.info(f"Scraped {len(results)}/{len(items)} articles successfully")
    return results

"""Write raw articles to data/raw/ as markdown with YAML frontmatter."""

import logging
from datetime import datetime
from pathlib import Path

import frontmatter
from slugify import slugify

logger = logging.getLogger(__name__)


def save_raw_article(article: dict, base_path: str = "data/raw") -> Path:
    """Save a scraped article as a markdown file with frontmatter.

    Returns the path to the saved file.
    """
    published = article.get("published", datetime.now().isoformat())
    dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
    date_dir = Path(base_path) / f"{dt.year}" / f"{dt.month:02d}" / f"{dt.day:02d}"
    date_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(article["title"], max_length=60)
    filename = f"{article['source_slug']}-{slug}.md"
    filepath = date_dir / filename

    if filepath.exists():
        logger.debug(f"Already exists: {filepath}")
        return filepath

    post = frontmatter.Post(
        content=f"# {article['title']}\n\n{article.get('content', '')}",
        title=article["title"],
        source=article["source_slug"],
        source_name=article["source_name"],
        url=article["url"],
        published=published,
        fetched=article.get("fetched", datetime.now().isoformat()),
        category=article.get("category", "industry"),
        word_count=article.get("word_count", 0),
        status="raw",
        topics=[],
        tldr="",
        entities=[],
        sentiment="",
    )

    filepath.write_text(frontmatter.dumps(post), encoding="utf-8")
    logger.info(f"Saved: {filepath}")
    return filepath


def save_raw_articles(articles: list[dict], base_path: str = "data/raw") -> list[Path]:
    """Save multiple articles. Returns list of saved file paths."""
    paths = []
    for article in articles:
        path = save_raw_article(article, base_path)
        paths.append(path)
    logger.info(f"Saved {len(paths)} articles to {base_path}")
    return paths

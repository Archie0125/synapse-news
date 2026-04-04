"""Identify trending topics from recent articles (bilingual EN + zh-TW)."""

import json
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path

import anthropic
import frontmatter
import yaml

logger = logging.getLogger(__name__)


def _load_prompt() -> str:
    return Path("prompts/trends.md").read_text(encoding="utf-8")


def _get_recent_articles(
    raw_path: str,
    days: int = 3,
    status: str = "summarized",
) -> list[tuple[Path, frontmatter.Post]]:
    """Get articles from the last N days that have been summarized."""
    articles = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    raw = Path(raw_path)
    if not raw.exists():
        return articles

    for md_file in sorted(raw.rglob("*.md"), reverse=True):
        post = frontmatter.load(str(md_file))
        if post.get("status") != status:
            continue
        try:
            pub = datetime.fromisoformat(
                post.get("published", "").replace("Z", "+00:00")
            )
            if pub >= cutoff:
                articles.append((md_file, post))
        except (ValueError, TypeError):
            articles.append((md_file, post))

    return articles


def _format_for_trends(articles: list[tuple[Path, frontmatter.Post]]) -> str:
    """Format articles as compact JSON for the trends prompt."""
    items = []
    for path, post in articles:
        items.append({
            "title": post.get("title", path.stem),
            "source": post.get("source_name", "Unknown"),
            "topics": post.get("topics", []),
            "tldr": post.get("tldr_en", post.get("tldr", "")),
            "category": post.get("category", "industry"),
        })
    return json.dumps(items, indent=2)


def identify_trends(config_path: str = "config.yaml") -> list[dict]:
    """Identify trending themes from recent articles (bilingual)."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    raw_path = config["paths"]["raw"]
    model = config["api"]["summarize_model"]
    trending_count = config["pipeline"].get("trending_count", 5)

    articles = _get_recent_articles(raw_path)
    if not articles:
        logger.info("No summarized articles for trend analysis")
        return []

    logger.info(f"Analyzing trends from {len(articles)} articles (bilingual)")
    prompt = _load_prompt()
    articles_text = _format_for_trends(articles)

    client = anthropic.Anthropic()
    try:
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": prompt + "\n" + articles_text,
            }],
        )
        text = response.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0]
        trends = json.loads(text)
        trends = trends[:trending_count]
        logger.info(f"Identified {len(trends)} trending themes (bilingual)")
        return trends
    except (json.JSONDecodeError, anthropic.APIError) as e:
        logger.error(f"Trend identification failed: {e}")
        return []


def write_daily_digest(
    trends: list[dict],
    wiki_path: str = "data/wiki",
):
    """Write the bilingual daily digest page."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    digest_dir = Path(wiki_path) / "daily"
    digest_dir.mkdir(parents=True, exist_ok=True)
    filepath = digest_dir / f"{today}.md"

    lines = [f"# Daily Digest / 每日摘要: {today}\n"]
    for i, trend in enumerate(trends, 1):
        theme_en = trend.get("theme_en", trend.get("theme", "Unknown"))
        theme_zh = trend.get("theme_zh", theme_en)
        why_en = trend.get("why_it_matters_en", trend.get("why_it_matters", ""))
        why_zh = trend.get("why_it_matters_zh", why_en)
        sentiment = trend.get("sentiment", "neutral")
        articles = trend.get("articles", [])

        lines.append(f"\n## {i}. {theme_en} / {theme_zh}\n")
        lines.append(f"**Sentiment:** {sentiment}\n")
        lines.append(f"\n{why_en}\n")
        lines.append(f"\n{why_zh}\n")
        if articles:
            lines.append("\n**Related articles / 相關文章:**\n")
            for a in articles:
                lines.append(f"- {a}\n")

    filepath.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Bilingual daily digest written: {filepath}")
    return filepath

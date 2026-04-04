"""Generate Threads content: article link posts + native hot takes."""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import frontmatter
import yaml

logger = logging.getLogger(__name__)


def _load_prompt() -> str:
    return Path("prompts/threads.md").read_text(encoding="utf-8")


def _gather_threads_material(
    trends: list[dict],
    raw_path: str,
    content_path: str,
) -> str:
    """Build context for the Threads prompt from trends and hot takes."""
    parts = []

    # Add trending themes
    parts.append("## TRENDING THEMES\n")
    for i, trend in enumerate(trends, 1):
        theme_en = trend.get("theme_en", trend.get("theme", ""))
        theme_zh = trend.get("theme_zh", theme_en)
        why_en = trend.get("why_it_matters_en", trend.get("why_it_matters", ""))
        category = trend.get("category", "industry")
        parts.append(f"{i}. {theme_en} / {theme_zh}")
        parts.append(f"   Category: {category}")
        parts.append(f"   Why: {why_en}\n")

    # Gather hot takes from summarized articles
    parts.append("\n## ARTICLE HOT TAKES\n")
    raw = Path(raw_path)
    if raw.exists():
        for md_file in sorted(raw.rglob("*.md"), reverse=True)[:30]:
            post = frontmatter.load(str(md_file))
            if post.get("status") not in ("summarized", "published"):
                continue
            hot_en = post.get("hot_take_en", "")
            hot_zh = post.get("hot_take_zh", "")
            if hot_en or hot_zh:
                title = post.get("title", md_file.stem)
                category = post.get("category", "industry")
                parts.append(f"- [{category}] {title}")
                if hot_en:
                    parts.append(f"  EN take: {hot_en}")
                if hot_zh:
                    parts.append(f"  ZH take: {hot_zh}")
                parts.append("")

    # List available article URLs for linking
    parts.append("\n## AVAILABLE ARTICLE URLS\n")
    content = Path(content_path)
    if content.exists():
        for md_file in sorted(content.glob("*.md"), reverse=True)[:20]:
            post = frontmatter.load(str(md_file))
            lang = post.get("lang", "en")
            category = post.get("category", "industry")
            title = post.get("title", md_file.stem)
            article_id = md_file.stem
            parts.append(f"- /{lang}/{category}/{article_id}/ — {title}")

    return "\n".join(parts)


def generate_threads_posts(
    trends: list[dict],
    config_path: str = "config.yaml",
) -> list[dict]:
    """Generate Threads posts from trends and article hot takes."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    raw_path = config["paths"]["raw"]
    content_path = config["paths"]["content"]
    model = config["api"]["summarize_model"]

    prompt = _load_prompt()
    material = _gather_threads_material(trends, raw_path, content_path)

    client = anthropic.Anthropic()
    try:
        response = client.messages.create(
            model=model,
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": prompt + "\n" + material,
            }],
        )
        text = response.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0]
        posts = json.loads(text)

        # Validate and clean
        valid_posts = []
        for post in posts:
            if not isinstance(post, dict):
                continue
            if "text" not in post or "type" not in post:
                continue
            # Enforce character limit
            if len(post["text"]) > 500:
                post["text"] = post["text"][:497] + "..."
            post.setdefault("lang", "zh")
            post.setdefault("schedule_priority", 3)
            post.setdefault("generated_at", datetime.now(timezone.utc).isoformat())
            valid_posts.append(post)

        # Sort by priority
        valid_posts.sort(key=lambda p: p.get("schedule_priority", 3))
        logger.info(f"Generated {len(valid_posts)} Threads posts")
        return valid_posts

    except (json.JSONDecodeError, anthropic.APIError) as e:
        logger.error(f"Threads content generation failed: {e}")
        return []

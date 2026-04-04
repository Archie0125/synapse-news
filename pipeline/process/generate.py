"""Generate bilingual analysis articles (EN + zh-TW) from trending themes."""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import frontmatter
import yaml
from slugify import slugify

logger = logging.getLogger(__name__)

LANG_SEPARATOR = "===LANG_SEPARATOR==="


def _load_prompt() -> str:
    return Path("prompts/generate_analysis.md").read_text(encoding="utf-8")


def _gather_source_articles(
    trend: dict,
    raw_path: str,
) -> list[tuple[Path, frontmatter.Post]]:
    """Find raw articles that match a trend's article titles."""
    matching = []
    article_titles = {a.lower().strip() for a in trend.get("articles", [])}

    raw = Path(raw_path)
    if not raw.exists():
        return matching

    for md_file in raw.rglob("*.md"):
        post = frontmatter.load(str(md_file))
        title = post.get("title", "").lower().strip()
        if title in article_titles or any(
            t in title or title in t for t in article_titles
        ):
            matching.append((md_file, post))

    return matching


def _format_sources(sources: list[tuple[Path, frontmatter.Post]]) -> str:
    """Format source articles for the generation prompt."""
    parts = []
    for path, post in sources[:5]:
        content = post.content[:3000]
        parts.append(
            f"--- SOURCE ---\n"
            f"Title: {post.get('title', path.stem)}\n"
            f"Source: {post.get('source_name', 'Unknown')}\n"
            f"URL: {post.get('url', '')}\n\n"
            f"{content}\n"
        )
    return "\n".join(parts)


def _parse_bilingual_response(text: str) -> tuple[frontmatter.Post | None, frontmatter.Post | None]:
    """Parse Claude's bilingual response into EN and ZH posts."""
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]

    if LANG_SEPARATOR in text:
        parts = text.split(LANG_SEPARATOR, 1)
        en_text = parts[0].strip()
        zh_text = parts[1].strip()
    else:
        # Fallback: treat as English only
        en_text = text.strip()
        zh_text = None

    en_post = None
    zh_post = None

    try:
        en_post = frontmatter.loads(en_text)
    except Exception:
        en_post = frontmatter.Post(content=en_text, title="Untitled", summary="")

    if zh_text:
        try:
            zh_post = frontmatter.loads(zh_text)
        except Exception:
            zh_post = frontmatter.Post(content=zh_text, title="Untitled", summary="")

    return en_post, zh_post


def generate_analysis(
    trend: dict,
    config_path: str = "config.yaml",
) -> list[Path]:
    """Generate bilingual analysis articles for a trending theme."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    raw_path = config["paths"]["raw"]
    wiki_path = config["paths"]["wiki"]
    model = config["api"]["analysis_model"]

    theme_en = trend.get("theme_en", trend.get("theme", "Unknown Theme"))
    theme_zh = trend.get("theme_zh", theme_en)
    why_en = trend.get("why_it_matters_en", trend.get("why_it_matters", ""))
    category = trend.get("category", "industry")

    sources = _gather_source_articles(trend, raw_path)
    if not sources:
        logger.warning(f"No source articles found for theme: {theme_en}")
        return []

    prompt_template = _load_prompt()
    prompt = prompt_template.replace("{theme_name}", f"{theme_en} / {theme_zh}")
    prompt = prompt.replace("{why_it_matters}", why_en)
    prompt += "\n" + _format_sources(sources)

    client = anthropic.Anthropic()
    try:
        response = client.messages.create(
            model=model,
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text.strip()
    except anthropic.APIError as e:
        logger.error(f"Analysis generation failed for '{theme_en}': {e}")
        return []

    en_post, zh_post = _parse_bilingual_response(text)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    now_iso = datetime.now(timezone.utc).isoformat()
    source_list = [
        {"name": p.get("source_name", ""), "url": p.get("url", "")}
        for _, p in sources[:5]
    ]

    saved_paths = []
    analysis_dir = Path(wiki_path) / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    # Save English version
    if en_post:
        en_post["title"] = en_post.get("title", theme_en)
        en_post["summary"] = en_post.get("summary", why_en[:200])
        en_post["category"] = category
        en_post["published"] = now_iso
        en_post["type"] = "analysis"
        en_post["lang"] = "en"
        en_post["sources"] = source_list
        en_post["trending_theme"] = theme_en

        slug = slugify(en_post["title"], max_length=60)
        filepath = analysis_dir / f"{today}-{slug}-en.md"
        filepath.write_text(frontmatter.dumps(en_post), encoding="utf-8")
        saved_paths.append(filepath)
        logger.info(f"Analysis (EN) generated: {filepath}")

    # Save Chinese version
    if zh_post:
        zh_post["title"] = zh_post.get("title", theme_zh)
        zh_post["summary"] = zh_post.get("summary", "")
        zh_post["category"] = category
        zh_post["published"] = now_iso
        zh_post["type"] = "analysis"
        zh_post["lang"] = "zh"
        zh_post["sources"] = source_list
        zh_post["trending_theme"] = theme_zh

        slug = slugify(en_post.get("title", theme_en) if en_post else theme_en, max_length=60)
        filepath = analysis_dir / f"{today}-{slug}-zh.md"
        filepath.write_text(frontmatter.dumps(zh_post), encoding="utf-8")
        saved_paths.append(filepath)
        logger.info(f"Analysis (ZH) generated: {filepath}")

    return saved_paths


def run_analysis_generation(
    trends: list[dict],
    config_path: str = "config.yaml",
) -> list[Path]:
    """Generate bilingual analysis articles for top trending themes."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    analysis_count = config["pipeline"].get("analysis_count", 3)

    paths = []
    for trend in trends[:analysis_count]:
        result = generate_analysis(trend, config_path)
        paths.extend(result)

    logger.info(f"Generated {len(paths)} bilingual analysis articles")
    return paths

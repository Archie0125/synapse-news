"""Publish bilingual articles (EN + zh-TW) to Astro content directory."""

import logging
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import frontmatter
import yaml
from slugify import slugify

logger = logging.getLogger(__name__)

# Claude prompt for translating article title + summary to zh-TW
TRANSLATE_PROMPT = """Translate the following tech news title and summary to Traditional Chinese (繁體中文).
Use natural, native-sounding Chinese with proper tech terminology.
Do NOT do word-for-word translation. Adapt for a Taiwanese/Chinese reader.

Title: {title}
Summary: {summary}

Output ONLY a JSON object with two fields:
{{"title_zh": "中文標題", "summary_zh": "中文摘要"}}
"""


def _format_astro_frontmatter(post: frontmatter.Post, lang: str, article_type: str = "news") -> dict:
    """Convert pipeline frontmatter to Astro content collection format."""
    published = post.get("published", datetime.now(timezone.utc).isoformat())
    sources = post.get("sources", [])
    if isinstance(sources, list) and sources and isinstance(sources[0], str):
        sources = [{"name": s, "url": ""} for s in sources]
    elif not isinstance(sources, list):
        sources = []

    clean_sources = []
    for s in sources:
        if isinstance(s, dict) and s.get("name"):
            clean_sources.append({
                "name": str(s.get("name", "")),
                "url": str(s.get("url", "")),
            })

    if not clean_sources and post.get("source_name"):
        clean_sources.append({
            "name": post.get("source_name", ""),
            "url": post.get("url", ""),
        })

    topics = post.get("topics", [])
    category = post.get("category", "industry")
    valid_cats = {"ai-ml", "startups", "products", "policy", "industry", "developer-tools", "hardware"}
    if topics and topics[0] in valid_cats:
        category = topics[0]
    elif category not in valid_cats:
        category = "industry"

    # Pick the right title/summary based on language
    if lang == "zh":
        title = str(post.get("title_zh", post.get("title", "Untitled")))[:120]
        summary = str(post.get("summary_zh", post.get("tldr_zh", post.get("summary", ""))))[:300]
    else:
        title = str(post.get("title", "Untitled"))[:120]
        summary = str(post.get("tldr_en", post.get("tldr", post.get("summary", ""))))[:300]

    # Pick language-specific FAQs and reshape {q,a} -> {question, answer} for Astro schema
    raw_faqs = post.get("faqs_zh" if lang == "zh" else "faqs_en", [])
    faqs = []
    if isinstance(raw_faqs, list):
        for f in raw_faqs:
            if isinstance(f, dict):
                q = str(f.get("q") or f.get("question") or "").strip()
                a = str(f.get("a") or f.get("answer") or "").strip()
                if q and a:
                    faqs.append({"question": q, "answer": a})

    meta = {
        "title": title,
        "summary": summary,
        "category": category,
        "publishedAt": published,
        "featured": False,
        "trending": False,
        "sources": clean_sources,
        "relatedSlugs": [],
        "tags": [str(t) for t in topics],
        "type": article_type,
        "lang": lang,
    }
    if faqs:
        meta["faqs"] = faqs
    return meta


def _translate_title_summary(client: anthropic.Anthropic, title: str, summary: str, model: str) -> dict:
    """Use Claude to translate title and summary to zh-TW."""
    import json
    prompt = TRANSLATE_PROMPT.format(title=title, summary=summary)
    try:
        response = client.messages.create(
            model=model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0]
        return json.loads(text)
    except Exception as e:
        logger.warning(f"Translation failed for '{title}': {e}")
        return {"title_zh": title, "summary_zh": summary}


def publish_article(
    post: frontmatter.Post,
    content_dir: str,
    lang: str,
    article_type: str = "news",
) -> Path | None:
    """Write a single article to the Astro content directory for a given language."""
    content_path = Path(content_dir)
    content_path.mkdir(parents=True, exist_ok=True)

    title = post.get("title", "Untitled")
    published = post.get("published", "")[:10]
    slug = slugify(title, max_length=60)
    filename = f"{published}-{slug}-{lang}.md" if published else f"{slug}-{lang}.md"
    filepath = content_path / filename

    astro_meta = _format_astro_frontmatter(post, lang, article_type)

    # Clean content
    content = post.content
    lines = content.split("\n")
    if lines and lines[0].startswith("# "):
        content = "\n".join(lines[1:]).lstrip()

    astro_post = frontmatter.Post(content=content, **astro_meta)
    filepath.write_text(frontmatter.dumps(astro_post), encoding="utf-8")
    logger.info(f"Published ({lang}): {filepath.name}")
    return filepath


def publish_summarized_articles(config_path: str = "config.yaml") -> list[Path]:
    """Publish summarized articles with per-category quota (default 3 per category).

    Ensures balanced coverage across all categories by picking the best
    articles from each category first, then filling remaining slots.
    """
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    raw_path = config["paths"]["raw"]
    content_dir = config["paths"]["content"]
    per_category = config["pipeline"].get("articles_per_category", 3)
    model = config["api"]["summarize_model"]

    published = []
    raw = Path(raw_path)
    if not raw.exists():
        return published

    # Group summarized articles by category
    by_category: dict[str, list[tuple[Path, frontmatter.Post]]] = {}
    for md_file in sorted(raw.rglob("*.md"), reverse=True):
        post = frontmatter.load(str(md_file))
        if post.get("status") == "summarized":
            cat = post.get("category", "industry")
            by_category.setdefault(cat, []).append((md_file, post))

    # Select top N articles per category
    selected: list[tuple[Path, frontmatter.Post]] = []
    cat_counts: dict[str, int] = {}
    for cat, items in by_category.items():
        picked = items[:per_category]
        selected.extend(picked)
        cat_counts[cat] = len(picked)

    logger.info(
        f"Publishing {len(selected)} articles across {len(cat_counts)} categories: "
        + ", ".join(f"{k}={v}" for k, v in sorted(cat_counts.items()))
    )

    client = anthropic.Anthropic()

    for path, post in selected:
        # Publish English version
        result_en = publish_article(post, content_dir, "en", "news")
        if result_en:
            published.append(result_en)

        # Generate zh-TW title/summary if not already present
        if not post.get("title_zh"):
            title_en = post.get("title", "")
            summary_en = post.get("tldr_en", post.get("tldr", ""))
            translated = _translate_title_summary(client, title_en, summary_en, model)
            post["title_zh"] = translated.get("title_zh", title_en)
            post["summary_zh"] = translated.get("summary_zh", summary_en)
            path.write_text(frontmatter.dumps(post), encoding="utf-8")

        # Publish Chinese version
        result_zh = publish_article(post, content_dir, "zh", "news")
        if result_zh:
            published.append(result_zh)

        # Mark as published
        post["status"] = "published"
        path.write_text(frontmatter.dumps(post), encoding="utf-8")

    logger.info(f"Published {len(published)} articles ({len(published)//2} EN + {len(published)//2} ZH)")
    return published


def publish_analysis_articles(config_path: str = "config.yaml") -> list[Path]:
    """Publish bilingual analysis articles to Astro content."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    wiki_path = config["paths"]["wiki"]
    content_dir = config["paths"]["content"]

    published = []
    analysis_dir = Path(wiki_path) / "analysis"
    if not analysis_dir.exists():
        return published

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for md_file in analysis_dir.glob(f"{today}*.md"):
        post = frontmatter.load(str(md_file))
        lang = post.get("lang", "en")
        result = publish_article(post, content_dir, lang, "analysis")
        if result:
            # Mark analysis as featured
            astro_post = frontmatter.load(str(result))
            astro_post["featured"] = True
            astro_post["trending"] = True
            result.write_text(frontmatter.dumps(astro_post), encoding="utf-8")
            published.append(result)

    logger.info(f"Published {len(published)} analysis articles")
    return published

"""Batch summarization of raw articles via Claude (bilingual EN + zh-TW)."""

import json
import logging
from pathlib import Path

import anthropic
import frontmatter
import yaml

from pipeline.process.perspectives import compose_perspectives

logger = logging.getLogger(__name__)


def _load_prompt(perspective_names: list[str] | None = None) -> str:
    base = Path("prompts/summarize.md").read_text(encoding="utf-8")
    if not perspective_names:
        return base
    dna = compose_perspectives(perspective_names)
    if not dna:
        return base
    return f"{base}\n\n{dna}\n"


def _get_raw_articles(raw_path: str, status: str = "raw") -> list[tuple[Path, frontmatter.Post]]:
    """Find all articles with the given status."""
    articles = []
    raw = Path(raw_path)
    if not raw.exists():
        return articles
    for md_file in sorted(raw.rglob("*.md")):
        post = frontmatter.load(str(md_file))
        if post.get("status") == status:
            articles.append((md_file, post))
    return articles


def _build_batch(articles: list[tuple[Path, frontmatter.Post]], batch_size: int = 10) -> list[list]:
    """Split articles into batches."""
    batches = []
    for i in range(0, len(articles), batch_size):
        batches.append(articles[i:i + batch_size])
    return batches


def _format_articles_for_prompt(batch: list[tuple[Path, frontmatter.Post]]) -> str:
    """Format a batch of articles for the summarize prompt."""
    parts = []
    for i, (path, post) in enumerate(batch):
        content = post.content[:2000]
        parts.append(
            f"--- ARTICLE {i} ---\n"
            f"ID: {path.stem}\n"
            f"Title: {post['title']}\n"
            f"Source: {post.get('source_name', 'Unknown')}\n\n"
            f"{content}\n"
        )
    return "\n".join(parts)


def summarize_batch(
    client: anthropic.Anthropic,
    batch: list[tuple[Path, frontmatter.Post]],
    model: str,
    perspectives: list[str] | None = None,
) -> list[dict]:
    """Send a batch to Claude for bilingual summarization."""
    prompt = _load_prompt(perspectives)
    articles_text = _format_articles_for_prompt(batch)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt + "\n" + articles_text}],
        )
        text = response.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0]
        summaries = json.loads(text)
        return summaries
    except (json.JSONDecodeError, IndexError, KeyError) as e:
        logger.error(f"Failed to parse summarization response: {e}")
        return []
    except anthropic.APIError as e:
        logger.error(f"Claude API error during summarization: {e}")
        return []


def apply_summaries(
    batch: list[tuple[Path, frontmatter.Post]],
    summaries: list[dict],
):
    """Apply Claude's bilingual summaries back to article frontmatter."""
    summary_map = {s.get("id", ""): s for s in summaries}

    for path, post in batch:
        summary = summary_map.get(path.stem)
        if not summary:
            idx = next(
                (i for i, (p, _) in enumerate(batch) if p == path), None
            )
            if idx is not None and idx < len(summaries):
                summary = summaries[idx]

        if summary:
            # Bilingual TLDR
            post["tldr_en"] = summary.get("tldr_en", "")
            post["tldr_zh"] = summary.get("tldr_zh", "")
            post["tldr"] = post["tldr_en"]
            post["hot_take_en"] = summary.get("hot_take_en", "")
            post["hot_take_zh"] = summary.get("hot_take_zh", "")
            post["topics"] = summary.get("topics", [])
            post["entities"] = summary.get("entities", [])
            post["sentiment"] = summary.get("sentiment", "neutral")
            post["status"] = "summarized"

            # Bilingual key points
            post["key_points_en"] = summary.get("key_points_en", [])
            post["key_points_zh"] = summary.get("key_points_zh", [])

            # Bilingual FAQs for FAQPage schema — gracefully skip malformed entries
            def _clean_faqs(raw):
                out = []
                if not isinstance(raw, list):
                    return out
                for item in raw:
                    if isinstance(item, dict):
                        q = str(item.get("q") or item.get("question") or "").strip()
                        a = str(item.get("a") or item.get("answer") or "").strip()
                        if q and a:
                            out.append({"q": q, "a": a})
                return out
            post["faqs_en"] = _clean_faqs(summary.get("faqs_en"))
            post["faqs_zh"] = _clean_faqs(summary.get("faqs_zh"))

            # Add bilingual summary section to content
            kp_en = summary.get("key_points_en", [])
            kp_zh = summary.get("key_points_zh", [])
            if kp_en:
                section = "\n\n## Summary\n\n"
                section += f"**TLDR:** {post['tldr_en']}\n\n"
                for point in kp_en:
                    section += f"- {point}\n"
                section += f"\n## 摘要\n\n"
                section += f"**重點摘要：** {post['tldr_zh']}\n\n"
                for point in kp_zh:
                    section += f"- {point}\n"
                if not post.content.endswith(section):
                    post.content += section

            path.write_text(frontmatter.dumps(post), encoding="utf-8")
            logger.info(f"Summarized: {post['title']}")
        else:
            logger.warning(f"No summary found for: {path.stem}")


def run_summarization(config_path: str = "config.yaml"):
    """Main entry point: summarize all raw articles."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    raw_path = config["paths"]["raw"]
    model = config["api"]["summarize_model"]
    batch_size = config["pipeline"].get("batch_size", 10)
    perspectives = (config.get("perspectives") or {}).get("summarize") or []

    articles = _get_raw_articles(raw_path, status="raw")
    if not articles:
        logger.info("No raw articles to summarize")
        return

    if perspectives:
        logger.info(f"Using editorial perspectives: {', '.join(perspectives)}")
    logger.info(f"Summarizing {len(articles)} articles (bilingual EN + zh-TW)")
    client = anthropic.Anthropic()
    batches = _build_batch(articles, batch_size)

    for i, batch in enumerate(batches):
        logger.info(f"Processing batch {i + 1}/{len(batches)} ({len(batch)} articles)")
        summaries = summarize_batch(client, batch, model, perspectives=perspectives)
        if summaries:
            apply_summaries(batch, summaries)

    logger.info("Bilingual summarization complete")

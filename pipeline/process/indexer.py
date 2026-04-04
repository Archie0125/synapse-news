"""Maintain topic and entity index pages in the wiki."""

import logging
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

import frontmatter
import yaml
from slugify import slugify

logger = logging.getLogger(__name__)


def _get_summarized_articles(
    raw_path: str,
    days: int = 7,
) -> list[tuple[Path, frontmatter.Post]]:
    """Get all summarized articles from the last N days."""
    articles = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    raw = Path(raw_path)
    if not raw.exists():
        return articles

    for md_file in sorted(raw.rglob("*.md"), reverse=True):
        post = frontmatter.load(str(md_file))
        if post.get("status") not in ("summarized", "indexed"):
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


def update_topic_indexes(config_path: str = "config.yaml"):
    """Update topic index pages with recent articles."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    raw_path = config["paths"]["raw"]
    wiki_path = config["paths"]["wiki"]
    categories = {c["slug"]: c["name"] for c in config.get("categories", [])}

    articles = _get_summarized_articles(raw_path)
    if not articles:
        logger.info("No articles for topic indexing")
        return

    # Group by topic
    topic_articles = defaultdict(list)
    for path, post in articles:
        for topic in post.get("topics", []):
            topic_articles[topic].append(post)
        # Also group by category
        cat = post.get("category", "")
        if cat:
            topic_articles[cat].append(post)

    # Write topic pages
    topics_dir = Path(wiki_path) / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)

    for topic, posts in topic_articles.items():
        topic_name = categories.get(topic, topic.replace("-", " ").title())
        filepath = topics_dir / f"{topic}.md"

        lines = [f"# {topic_name}\n"]
        lines.append(f"\n*{len(posts)} articles in the last 7 days*\n")
        lines.append("\n## Latest\n")

        seen_titles = set()
        for post in posts[:20]:
            title = post.get("title", "Untitled")
            if title in seen_titles:
                continue
            seen_titles.add(title)
            tldr = post.get("tldr", "")
            source = post.get("source_name", "")
            pub = post.get("published", "")[:10]
            lines.append(f"\n### {title}\n")
            lines.append(f"*{source} | {pub}*\n")
            if tldr:
                lines.append(f"\n{tldr}\n")

        filepath.write_text("\n".join(lines), encoding="utf-8")
        logger.info(f"Topic index updated: {topic} ({len(posts)} articles)")


def update_entity_pages(config_path: str = "config.yaml"):
    """Update entity (company/person/product) pages."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    raw_path = config["paths"]["raw"]
    wiki_path = config["paths"]["wiki"]

    articles = _get_summarized_articles(raw_path)

    # Group by entity
    entity_mentions = defaultdict(list)
    for path, post in articles:
        for entity in post.get("entities", []):
            entity_mentions[entity].append(post)

    # Write entity pages
    entities_dir = Path(wiki_path) / "entities"
    entities_dir.mkdir(parents=True, exist_ok=True)

    for entity, posts in entity_mentions.items():
        if len(posts) < 2:  # Only create pages for entities with multiple mentions
            continue
        slug = slugify(entity)
        filepath = entities_dir / f"{slug}.md"

        lines = [f"# {entity}\n"]
        lines.append(f"\n*Mentioned in {len(posts)} articles*\n")
        lines.append("\n## Recent Mentions\n")

        seen_titles = set()
        for post in posts[:15]:
            title = post.get("title", "Untitled")
            if title in seen_titles:
                continue
            seen_titles.add(title)
            pub = post.get("published", "")[:10]
            tldr = post.get("tldr", "")
            lines.append(f"\n- **{title}** ({pub})")
            if tldr:
                lines.append(f"  - {tldr}")

        filepath.write_text("\n".join(lines), encoding="utf-8")
        logger.info(f"Entity page updated: {entity}")


def rebuild_master_index(config_path: str = "config.yaml"):
    """Rebuild the master wiki index."""
    config = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    wiki_path = Path(config["paths"]["wiki"])
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines = ["# Synapse Knowledge Base\n"]
    lines.append(f"\n*Last updated: {today}*\n")

    # Daily digest link
    digest = wiki_path / "daily" / f"{today}.md"
    if digest.exists():
        lines.append(f"\n## Today's Digest\n\n- [Daily Digest {today}](daily/{today}.md)\n")

    # Recent analysis
    analysis_dir = wiki_path / "analysis"
    if analysis_dir.exists():
        analysis_files = sorted(analysis_dir.glob("*.md"), reverse=True)[:5]
        if analysis_files:
            lines.append("\n## Recent Analysis\n")
            for f in analysis_files:
                post = frontmatter.load(str(f))
                title = post.get("title", f.stem)
                lines.append(f"- [{title}](analysis/{f.name})\n")

    # Topic directory
    topics_dir = wiki_path / "topics"
    if topics_dir.exists():
        topic_files = sorted(topics_dir.glob("*.md"))
        if topic_files:
            lines.append("\n## Topics\n")
            for f in topic_files:
                name = f.stem.replace("-", " ").title()
                lines.append(f"- [{name}](topics/{f.name})\n")

    # Entity directory
    entities_dir = wiki_path / "entities"
    if entities_dir.exists():
        entity_files = sorted(entities_dir.glob("*.md"))
        if entity_files:
            lines.append("\n## Entities\n")
            for f in entity_files[:20]:
                name = f.stem.replace("-", " ").title()
                lines.append(f"- [{name}](entities/{f.name})\n")

    index_path = wiki_path / "_index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info(f"Master index rebuilt: {index_path}")


def run_indexing(config_path: str = "config.yaml"):
    """Run all indexing operations."""
    update_topic_indexes(config_path)
    update_entity_pages(config_path)
    rebuild_master_index(config_path)
    logger.info("Indexing complete")

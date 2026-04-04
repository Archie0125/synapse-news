"""Daily pipeline orchestrator.

Usage:
    python -m pipeline.main              # Run full pipeline
    python -m pipeline.main --phase fetch # Run specific phase
"""

import argparse
import asyncio
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from pipeline.ingest.rss import fetch_all_feeds
from pipeline.ingest.dedup import Deduplicator
from pipeline.ingest.scraper import scrape_articles
from pipeline.ingest.writer import save_raw_articles
from pipeline.process.summarize import run_summarization
from pipeline.process.trends import identify_trends, write_daily_digest
from pipeline.process.generate import run_analysis_generation
from pipeline.process.indexer import run_indexing
from pipeline.build.publisher import publish_summarized_articles, publish_analysis_articles
from pipeline.process.threads import generate_threads_posts
from pipeline.build.threads_publisher import enqueue_posts, export_for_site

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("pipeline")

STATE_FILE = "data/pipeline_state.json"


def _load_state() -> dict:
    path = Path(STATE_FILE)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def _save_state(state: dict):
    path = Path(STATE_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


async def phase_fetch(config_path: str = "config.yaml"):
    """Phase 1: Fetch RSS, deduplicate, scrape, save raw articles."""
    logger.info("=== PHASE 1: FETCH ===")

    # Fetch RSS feeds
    items = await fetch_all_feeds(config_path)
    if not items:
        logger.info("No new items from feeds")
        return 0

    # Deduplicate
    dedup = Deduplicator()
    dedup.prune()
    unique = dedup.deduplicate(items)
    if not unique:
        logger.info("All items were duplicates")
        return 0

    # Scrape full articles
    articles = await scrape_articles(unique)
    if not articles:
        logger.info("No articles could be scraped")
        return 0

    # Save to data/raw/
    paths = save_raw_articles(articles)
    logger.info(f"Phase 1 complete: {len(paths)} articles saved")
    return len(paths)


def phase_summarize(config_path: str = "config.yaml"):
    """Phase 2: Summarize raw articles via Claude."""
    logger.info("=== PHASE 2: SUMMARIZE ===")
    run_summarization(config_path)


def phase_analyze(config_path: str = "config.yaml") -> list[dict]:
    """Phase 3: Identify trends and generate analysis."""
    logger.info("=== PHASE 3: ANALYZE ===")
    trends = identify_trends(config_path)
    if trends:
        write_daily_digest(trends)
        run_analysis_generation(trends, config_path)
    return trends


def phase_index(config_path: str = "config.yaml"):
    """Phase 4: Update wiki indexes."""
    logger.info("=== PHASE 4: INDEX ===")
    run_indexing(config_path)


def phase_publish(config_path: str = "config.yaml"):
    """Phase 5: Publish to Astro content directory."""
    logger.info("=== PHASE 5: PUBLISH ===")
    news = publish_summarized_articles(config_path)
    analysis = publish_analysis_articles(config_path)
    logger.info(f"Published {len(news)} news + {len(analysis)} analysis articles")


def phase_threads(trends: list[dict], config_path: str = "config.yaml"):
    """Phase 6: Generate and queue Threads posts."""
    logger.info("=== PHASE 6: THREADS ===")
    posts = generate_threads_posts(trends, config_path)
    if posts:
        enqueue_posts(posts)
        export_for_site()
        logger.info(f"Threads: {len(posts)} posts queued")
    else:
        logger.info("No Threads posts generated")


async def run_full_pipeline(config_path: str = "config.yaml"):
    """Run the complete daily pipeline."""
    state = _load_state()
    state["last_run_start"] = _now()
    logger.info("Starting full pipeline run")

    try:
        # Phase 1: Fetch
        state["fetch_start"] = _now()
        count = await phase_fetch(config_path)
        state["fetch_end"] = _now()
        state["fetch_count"] = count

        if count == 0:
            logger.info("No new articles, skipping remaining phases")
            state["last_run_end"] = _now()
            state["last_run_status"] = "empty"
            _save_state(state)
            return

        # Phase 2: Summarize
        state["summarize_start"] = _now()
        phase_summarize(config_path)
        state["summarize_end"] = _now()

        # Phase 3: Analyze
        state["analyze_start"] = _now()
        trends = phase_analyze(config_path)
        state["analyze_end"] = _now()

        # Phase 4: Index
        state["index_start"] = _now()
        phase_index(config_path)
        state["index_end"] = _now()

        # Phase 5: Publish
        state["publish_start"] = _now()
        phase_publish(config_path)
        state["publish_end"] = _now()

        # Phase 6: Threads
        state["threads_start"] = _now()
        phase_threads(trends, config_path)
        state["threads_end"] = _now()

        state["last_run_end"] = _now()
        state["last_run_status"] = "success"
        logger.info("Pipeline complete!")

    except Exception as e:
        state["last_run_end"] = _now()
        state["last_run_status"] = f"error: {e}"
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        raise

    finally:
        _save_state(state)


def main():
    parser = argparse.ArgumentParser(description="Synapse news pipeline")
    parser.add_argument(
        "--phase",
        choices=["fetch", "summarize", "analyze", "index", "publish", "threads", "all"],
        default="all",
        help="Run a specific phase or all phases",
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to config file",
    )
    args = parser.parse_args()

    if args.phase == "all":
        asyncio.run(run_full_pipeline(args.config))
    elif args.phase == "fetch":
        asyncio.run(phase_fetch(args.config))
    elif args.phase == "summarize":
        phase_summarize(args.config)
    elif args.phase == "analyze":
        phase_analyze(args.config)
    elif args.phase == "index":
        phase_index(args.config)
    elif args.phase == "publish":
        phase_publish(args.config)
    elif args.phase == "threads":
        trends = phase_analyze(args.config)
        phase_threads(trends, args.config)


if __name__ == "__main__":
    main()

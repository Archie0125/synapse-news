"""Auto-poster: reads queue, posts to Threads API, marks as posted.

Usage:
    python -m pipeline.threads.poster              # Post all due items
    python -m pipeline.threads.poster --dry-run     # Preview without posting
    python -m pipeline.threads.poster --post-next   # Post the next pending item
"""

import argparse
import logging
import time
from datetime import datetime, timezone

from pipeline.threads.api import ThreadsAPI
from pipeline.threads.oauth import get_access_token, load_token, refresh_token
from pipeline.build.threads_publisher import (
    get_due_posts,
    get_pending_posts,
    mark_posted,
    mark_skipped,
    get_queue_summary,
    export_for_site,
)

logger = logging.getLogger(__name__)


def _check_token_expiry():
    """Refresh token if it's within 7 days of expiring."""
    token_data = load_token()
    if not token_data or "expires_at" not in token_data:
        return

    expires_at = datetime.fromisoformat(token_data["expires_at"])
    now = datetime.now(timezone.utc)
    days_left = (expires_at - now).days

    if days_left < 7:
        logger.info(f"Token expires in {days_left} days, refreshing...")
        refresh_token()
    elif days_left < 14:
        logger.info(f"Token expires in {days_left} days")


def _check_quota(api: ThreadsAPI) -> int:
    """Check remaining posting quota. Returns remaining count."""
    try:
        limit_data = api.get_publishing_limit()
        data = limit_data.get("data", [{}])[0]
        usage = data.get("quota_usage", 0)
        total = data.get("config", {}).get("quota_total", 250)
        remaining = total - usage
        logger.info(f"Threads quota: {usage}/{total} used, {remaining} remaining")
        return remaining
    except Exception as e:
        logger.warning(f"Could not check quota: {e}")
        return 250  # Assume OK if check fails


def post_due(dry_run: bool = False, delay_between: float = 30.0) -> int:
    """Post all items that are due (scheduled_for <= now).

    Returns number of posts published.
    """
    _check_token_expiry()
    token = get_access_token()

    due = get_due_posts()
    if not due:
        logger.info("No posts are due right now")
        return 0

    logger.info(f"Found {len(due)} due posts")

    if dry_run:
        for i, post in enumerate(due, 1):
            print(f"\n--- Post {i}/{len(due)} ---")
            print(f"Type: {post.get('type')}")
            print(f"Lang: {post.get('lang')}")
            print(f"Scheduled: {post.get('scheduled_for')}")
            print(f"Text:\n{post.get('text')}")
            if post.get("article_url"):
                print(f"Article: {post.get('article_url')}")
        return 0

    api = ThreadsAPI(token)
    remaining = _check_quota(api)
    posted = 0

    for i, post in enumerate(due):
        if remaining <= 5:
            logger.warning("Near quota limit, stopping")
            break

        text = post["text"]
        logger.info(f"Posting {i+1}/{len(due)}: {text[:50]}...")

        try:
            result = api.publish_text(text)
            post_id = result.get("id", "")
            mark_posted(text, threads_post_id=post_id)
            posted += 1
            remaining -= 1
            logger.info(f"Posted successfully: {post_id}")

            # Delay between posts to avoid looking spammy
            if i < len(due) - 1:
                logger.info(f"Waiting {delay_between}s before next post...")
                time.sleep(delay_between)

        except Exception as e:
            logger.error(f"Failed to post: {e}")
            if "spam" in str(e).lower() or "rate" in str(e).lower():
                logger.error("Rate limited or flagged as spam, stopping")
                break
            mark_skipped(text, reason=str(e))

    # Update the site export
    export_for_site()
    api.close()

    logger.info(f"Done: {posted}/{len(due)} posts published")
    return posted


def post_next(dry_run: bool = False) -> bool:
    """Post just the next pending item (regardless of schedule).

    Returns True if a post was published.
    """
    _check_token_expiry()
    token = get_access_token()

    pending = get_pending_posts()
    if not pending:
        logger.info("No pending posts in queue")
        return False

    post = pending[0]
    text = post["text"]

    print(f"\nNext post ({post.get('type')}, {post.get('lang')}):")
    print(f"  {text}")
    if post.get("article_url"):
        print(f"  Link: {post.get('article_url')}")

    if dry_run:
        return False

    api = ThreadsAPI(token)
    try:
        result = api.publish_text(text)
        post_id = result.get("id", "")
        mark_posted(text, threads_post_id=post_id)
        export_for_site()
        logger.info(f"Posted: {post_id}")
        return True
    except Exception as e:
        logger.error(f"Failed: {e}")
        return False
    finally:
        api.close()


def show_status():
    """Print queue status."""
    summary = get_queue_summary()
    token_data = load_token()

    print("\n" + "=" * 50)
    print("  Threads Queue Status")
    print("=" * 50)
    print(f"  Pending posts:  {summary['pending']}")
    print(f"  Total posted:   {summary['total_posted']}")

    if summary.get("next_post"):
        nxt = summary["next_post"]
        print(f"\n  Next post:")
        print(f"    Type: {nxt.get('type')}")
        print(f"    Lang: {nxt.get('lang')}")
        print(f"    Scheduled: {nxt.get('scheduled_for')}")
        print(f"    Preview: {nxt.get('text', '')[:80]}...")

    if token_data:
        expires = token_data.get("expires_at", "unknown")
        print(f"\n  Token expires: {expires}")
    else:
        print(f"\n  Token: NOT SET — run: python -m pipeline.threads.oauth")

    due = get_due_posts()
    if due:
        print(f"\n  {len(due)} posts are DUE NOW — run: python -m pipeline.threads.poster")

    print("=" * 50 + "\n")


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    parser = argparse.ArgumentParser(description="Threads auto-poster")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    parser.add_argument("--post-next", action="store_true", help="Post just the next item")
    parser.add_argument("--status", action="store_true", help="Show queue status")
    parser.add_argument(
        "--delay", type=float, default=30.0, help="Seconds between posts (default: 30)"
    )
    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.post_next:
        post_next(dry_run=args.dry_run)
    else:
        post_due(dry_run=args.dry_run, delay_between=args.delay)


if __name__ == "__main__":
    main()

"""Threads post queue manager.

Saves generated posts to a JSON queue file. Each post has:
- status: "pending" | "posted" | "skipped"
- scheduled_for: ISO timestamp for when to post
- posted_at: when it was actually posted (filled by poster)

Future: connect to Threads API (graph.threads.net) to auto-post.
"""

import json
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

QUEUE_FILE = "data/threads/queue.json"
HISTORY_FILE = "data/threads/history.json"


def _load_queue() -> list[dict]:
    path = Path(QUEUE_FILE)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return []


def _save_queue(queue: list[dict]):
    path = Path(QUEUE_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(queue, indent=2, ensure_ascii=False), encoding="utf-8")


def _load_history() -> list[dict]:
    path = Path(HISTORY_FILE)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return []


def _save_history(history: list[dict]):
    path = Path(HISTORY_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")


def enqueue_posts(
    posts: list[dict],
    posts_per_day: int = 6,
    start_hour: int = 8,
    end_hour: int = 22,
):
    """Add posts to the queue with scheduled times.

    Spreads posts across the day between start_hour and end_hour.
    """
    queue = _load_queue()
    existing_texts = {p["text"] for p in queue}

    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=start_hour, minute=0, second=0, microsecond=0)
    if now > today_start:
        today_start = now  # Don't schedule in the past

    # Calculate posting intervals
    hours_available = end_hour - start_hour
    interval_hours = hours_available / max(posts_per_day, 1)

    new_count = 0
    slot = 0
    for post in posts:
        # Skip duplicates
        if post["text"] in existing_texts:
            continue

        # Calculate scheduled time
        scheduled = today_start + timedelta(hours=slot * interval_hours)
        if scheduled < now:
            scheduled = now + timedelta(minutes=30 * (slot + 1))

        queue_entry = {
            **post,
            "status": "pending",
            "scheduled_for": scheduled.isoformat(),
            "queued_at": now.isoformat(),
        }
        queue.append(queue_entry)
        existing_texts.add(post["text"])
        new_count += 1
        slot += 1

    _save_queue(queue)
    logger.info(f"Enqueued {new_count} new Threads posts (total queue: {len(queue)})")
    return new_count


def get_pending_posts() -> list[dict]:
    """Get all pending posts, sorted by scheduled time."""
    queue = _load_queue()
    pending = [p for p in queue if p.get("status") == "pending"]
    pending.sort(key=lambda p: p.get("scheduled_for", ""))
    return pending


def get_due_posts() -> list[dict]:
    """Get posts that are due to be posted now."""
    now = datetime.now(timezone.utc).isoformat()
    pending = get_pending_posts()
    return [p for p in pending if p.get("scheduled_for", "") <= now]


def mark_posted(post_text: str, threads_post_id: str = ""):
    """Mark a post as posted (after successfully posting to Threads)."""
    queue = _load_queue()
    history = _load_history()

    for post in queue:
        if post["text"] == post_text and post["status"] == "pending":
            post["status"] = "posted"
            post["posted_at"] = datetime.now(timezone.utc).isoformat()
            post["threads_post_id"] = threads_post_id
            history.append(post)
            break

    # Remove posted items from queue
    queue = [p for p in queue if p.get("status") == "pending"]
    _save_queue(queue)
    _save_history(history)


def mark_skipped(post_text: str, reason: str = ""):
    """Mark a post as skipped."""
    queue = _load_queue()
    for post in queue:
        if post["text"] == post_text and post["status"] == "pending":
            post["status"] = "skipped"
            post["skip_reason"] = reason
            break
    # Remove skipped from active queue
    queue = [p for p in queue if p.get("status") == "pending"]
    _save_queue(queue)


def get_queue_summary() -> dict:
    """Get a summary of the queue state."""
    queue = _load_queue()
    history = _load_history()
    return {
        "pending": len([p for p in queue if p.get("status") == "pending"]),
        "total_posted": len(history),
        "next_post": get_pending_posts()[0] if get_pending_posts() else None,
    }


def export_for_site(output_path: str = "src/data/threads-queue.json"):
    """Export the queue as a JSON file for the Astro site to read."""
    pending = get_pending_posts()
    history = _load_history()

    export = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pending": pending[:20],
        "recent_posted": history[-10:] if history else [],
        "stats": {
            "pending_count": len(pending),
            "posted_today": len([
                h for h in history
                if h.get("posted_at", "")[:10] == datetime.now(timezone.utc).strftime("%Y-%m-%d")
            ]),
            "total_posted": len(history),
        },
    }

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(export, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info(f"Threads queue exported to {output_path}")

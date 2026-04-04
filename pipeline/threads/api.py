"""Threads API client — two-step publish flow via graph.threads.net."""

import logging
import time

import httpx

logger = logging.getLogger(__name__)

BASE_URL = "https://graph.threads.net/v1.0"


class ThreadsAPI:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.client = httpx.Client(timeout=30.0)

    def _params(self, **extra) -> dict:
        return {"access_token": self.access_token, **extra}

    # ── Publishing ────────────────────────────────────────

    def publish_text(self, text: str, reply_to_id: str | None = None) -> dict:
        """Publish a text-only post. Returns {"id": "..."}."""
        # Step 1: create container
        data = {
            "media_type": "TEXT",
            "text": text,
            "access_token": self.access_token,
        }
        if reply_to_id:
            data["reply_to_id"] = reply_to_id

        resp = self.client.post(f"{BASE_URL}/me/threads", data=data)
        resp.raise_for_status()
        creation_id = resp.json()["id"]

        # Step 2: publish
        resp = self.client.post(
            f"{BASE_URL}/me/threads_publish",
            data={
                "creation_id": creation_id,
                "access_token": self.access_token,
            },
        )
        resp.raise_for_status()
        result = resp.json()
        logger.info(f"Published Threads post: {result.get('id')}")
        return result

    def publish_image(self, image_url: str, text: str = "") -> dict:
        """Publish an image post. image_url must be publicly accessible."""
        data = {
            "media_type": "IMAGE",
            "image_url": image_url,
            "access_token": self.access_token,
        }
        if text:
            data["text"] = text

        resp = self.client.post(f"{BASE_URL}/me/threads", data=data)
        resp.raise_for_status()
        creation_id = resp.json()["id"]

        resp = self.client.post(
            f"{BASE_URL}/me/threads_publish",
            data={
                "creation_id": creation_id,
                "access_token": self.access_token,
            },
        )
        resp.raise_for_status()
        return resp.json()

    # ── Read ──────────────────────────────────────────────

    def get_my_posts(self, limit: int = 25) -> dict:
        """Get published posts."""
        resp = self.client.get(
            f"{BASE_URL}/me/threads",
            params=self._params(
                fields="id,media_type,text,permalink,timestamp,is_quote_post",
                limit=limit,
            ),
        )
        resp.raise_for_status()
        return resp.json()

    def get_profile(self) -> dict:
        """Get authorized user profile."""
        resp = self.client.get(
            f"{BASE_URL}/me",
            params=self._params(
                fields="id,username,threads_profile_picture_url,threads_biography"
            ),
        )
        resp.raise_for_status()
        return resp.json()

    def get_publishing_limit(self) -> dict:
        """Check current quota usage (250 posts / 24h)."""
        resp = self.client.get(
            f"{BASE_URL}/me/threads_publishing_limit",
            params=self._params(fields="quota_usage,config"),
        )
        resp.raise_for_status()
        return resp.json()

    def get_post_insights(self, post_id: str) -> dict:
        """Get insights for a specific post."""
        resp = self.client.get(
            f"{BASE_URL}/{post_id}/insights",
            params=self._params(metric="views,likes,replies,reposts,quotes"),
        )
        resp.raise_for_status()
        return resp.json()

    def close(self):
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

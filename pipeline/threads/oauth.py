"""Threads OAuth 2.0 flow with local callback server.

Usage:
    python -m pipeline.threads.oauth          # Start OAuth flow
    python -m pipeline.threads.oauth --refresh # Refresh existing token
"""

import argparse
import json
import logging
import os
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import httpx

logger = logging.getLogger(__name__)

TOKEN_FILE = "data/threads/token.json"
REDIRECT_PORT = 8888
REDIRECT_URI = f"http://localhost:{REDIRECT_PORT}/callback"

SCOPES = [
    "threads_basic",
    "threads_content_publish",
    "threads_manage_insights",
    "threads_manage_replies",
]


def _get_credentials() -> tuple[str, str]:
    """Get app credentials from environment variables."""
    app_id = os.environ.get("THREADS_APP_ID")
    app_secret = os.environ.get("THREADS_APP_SECRET")
    if not app_id or not app_secret:
        raise RuntimeError(
            "Set THREADS_APP_ID and THREADS_APP_SECRET environment variables.\n"
            "Get these from https://developers.facebook.com/ → Your App → Settings"
        )
    return app_id, app_secret


def load_token() -> dict | None:
    """Load saved token from disk."""
    path = Path(TOKEN_FILE)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return None


def save_token(token_data: dict):
    """Save token to disk."""
    path = Path(TOKEN_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(token_data, indent=2), encoding="utf-8")
    logger.info(f"Token saved to {TOKEN_FILE}")


def get_access_token() -> str:
    """Get a valid access token, or raise if none exists."""
    token_data = load_token()
    if not token_data or "access_token" not in token_data:
        raise RuntimeError(
            "No Threads token found. Run: python -m pipeline.threads.oauth"
        )
    return token_data["access_token"]


def _exchange_code(auth_code: str, app_id: str, app_secret: str) -> dict:
    """Exchange auth code for short-lived token, then long-lived token."""
    client = httpx.Client(timeout=30.0)

    # Step 1: auth code → short-lived token
    resp = client.post(
        "https://graph.threads.net/oauth/access_token",
        data={
            "client_id": app_id,
            "client_secret": app_secret,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "code": auth_code,
        },
    )
    resp.raise_for_status()
    short_data = resp.json()
    short_token = short_data["access_token"]
    user_id = short_data.get("user_id", "")
    logger.info(f"Got short-lived token for user {user_id}")

    # Step 2: short-lived → long-lived token (60 days)
    resp = client.get(
        "https://graph.threads.net/access_token",
        params={
            "grant_type": "th_exchange_token",
            "client_secret": app_secret,
            "access_token": short_token,
        },
    )
    resp.raise_for_status()
    long_data = resp.json()
    client.close()

    from datetime import datetime, timezone, timedelta

    token_data = {
        "access_token": long_data["access_token"],
        "token_type": long_data.get("token_type", "bearer"),
        "expires_in": long_data.get("expires_in", 5184000),  # 60 days
        "user_id": user_id,
        "obtained_at": datetime.now(timezone.utc).isoformat(),
        "expires_at": (
            datetime.now(timezone.utc) + timedelta(seconds=long_data.get("expires_in", 5184000))
        ).isoformat(),
    }
    return token_data


def refresh_token() -> dict:
    """Refresh the long-lived token (call before it expires)."""
    token_data = load_token()
    if not token_data:
        raise RuntimeError("No token to refresh. Run OAuth flow first.")

    _, app_secret = _get_credentials()
    client = httpx.Client(timeout=30.0)
    resp = client.get(
        "https://graph.threads.net/refresh_access_token",
        params={
            "grant_type": "th_refresh_token",
            "access_token": token_data["access_token"],
        },
    )
    resp.raise_for_status()
    new_data = resp.json()
    client.close()

    from datetime import datetime, timezone, timedelta

    token_data["access_token"] = new_data["access_token"]
    token_data["expires_in"] = new_data.get("expires_in", 5184000)
    token_data["obtained_at"] = datetime.now(timezone.utc).isoformat()
    token_data["expires_at"] = (
        datetime.now(timezone.utc) + timedelta(seconds=new_data.get("expires_in", 5184000))
    ).isoformat()

    save_token(token_data)
    logger.info("Token refreshed successfully")
    return token_data


class _OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Handle the OAuth redirect callback."""

    auth_code: str | None = None

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if "code" in params:
            _OAuthCallbackHandler.auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                b"<html><body style='font-family:system-ui;text-align:center;padding:60px'>"
                b"<h1>&#10004; Threads Authorization Successful</h1>"
                b"<p>You can close this window and return to the terminal.</p>"
                b"</body></html>"
            )
        elif "error" in params:
            error = params.get("error_description", params["error"])[0]
            self.send_response(400)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"<h1>Error: {error}</h1>".encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Suppress default logging


def run_oauth_flow():
    """Run the full OAuth flow: open browser → wait for callback → save token."""
    app_id, app_secret = _get_credentials()

    auth_url = (
        f"https://threads.net/oauth/authorize"
        f"?client_id={app_id}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={','.join(SCOPES)}"
        f"&response_type=code"
    )

    print("\n" + "=" * 60)
    print("  Threads OAuth Login")
    print("=" * 60)
    print(f"\nOpening browser for authorization...\n")
    print(f"If browser doesn't open, visit:\n{auth_url}\n")

    webbrowser.open(auth_url)

    # Start local server to receive callback
    print(f"Waiting for callback on http://localhost:{REDIRECT_PORT}/callback ...")
    server = HTTPServer(("localhost", REDIRECT_PORT), _OAuthCallbackHandler)
    server.timeout = 120  # 2 minute timeout

    while _OAuthCallbackHandler.auth_code is None:
        server.handle_request()

    auth_code = _OAuthCallbackHandler.auth_code
    server.server_close()

    print("\nExchanging code for token...")
    token_data = _exchange_code(auth_code, app_id, app_secret)
    save_token(token_data)

    print(f"\n{'=' * 60}")
    print(f"  Login successful!")
    print(f"  User ID: {token_data.get('user_id')}")
    print(f"  Token expires: {token_data.get('expires_at')}")
    print(f"  Saved to: {TOKEN_FILE}")
    print(f"{'=' * 60}\n")

    return token_data


def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description="Threads OAuth login")
    parser.add_argument("--refresh", action="store_true", help="Refresh existing token")
    args = parser.parse_args()

    if args.refresh:
        refresh_token()
        print("Token refreshed.")
    else:
        run_oauth_flow()


if __name__ == "__main__":
    main()

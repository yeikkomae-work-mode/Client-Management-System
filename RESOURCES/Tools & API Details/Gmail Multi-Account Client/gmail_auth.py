#!/usr/bin/env python3
"""
One-time OAuth authorization for a Gmail account not covered by the claude.ai
Gmail connector (which only supports one account: yeikkomae@gmail.com).

Usage:
    python3 gmail_auth.py <account_key>

Opens your default browser to Google's real login page. You log in and click
Allow yourself — this script never sees your password. On success it saves a
refresh token to "<account_key>_token.json" next to the client secret files.

Scopes are deliberately read + draft-only (no gmail.send) so nothing can be
sent through this client, matching the "never send without confirmation" rule.
"""
import http.server
import json
import os
import sys
import urllib.parse
import webbrowser

os.environ.setdefault("OAUTHLIB_INSECURE_TRANSPORT", "1")

from google_auth_oauthlib.flow import Flow, InstalledAppFlow

CREDS_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../OAuth Credentials"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.compose",
]

ACCOUNTS = {
    "personal": {
        "email": "eikkomaeybanez@gmail.com",
        "client_secret": "Personal_eikkomaeybanez_client_secret_1080807478962-2schsr021rg9eb1tcg3gu4frln8nta00.apps.googleusercontent.com.json",
    },
    "satlas": {
        "email": "eikko@satlas.com.au",
        "client_secret": "Satlas_client_secret_2_295159186046-1eq4uankkvnoo0ssjssslof14psdq4r3.apps.googleusercontent.com.json",
    },
    "albertscott": {
        "email": "salesmanager@albertscott.com",
        "client_secret": "albertscott_client_secret_784308412505-g1cp8ajsmkt9aht0f4fg70ir5n0c3v0r.apps.googleusercontent.com.json",
    },
    "fractio": {
        "email": "eikko.ybanez@fractio.co",
        "client_secret": "Fractio_client_secret_2_299870782137-qos30684ocr3lose6om2bbv5fe3uak5i.apps.googleusercontent.com.json",
    },
}


def _authorize_fixed_redirect(secret_path, redirect_uri, login_hint):
    """For 'web'-type OAuth clients Google requires an exact redirect_uri
    match — no dynamic-port loopback exception. Spin up a one-shot local
    server on the exact registered host/port/path instead."""
    parsed = urllib.parse.urlparse(redirect_uri)
    port = parsed.port
    path = parsed.path or "/"

    flow = Flow.from_client_secrets_file(secret_path, scopes=SCOPES, redirect_uri=redirect_uri)
    auth_url, _ = flow.authorization_url(
        prompt="select_account consent", access_type="offline", login_hint=login_hint
    )

    captured = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            captured["full_url"] = f"{parsed.scheme}://{parsed.netloc}{self.path}"
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body>Authentication complete. You may close this window.</body></html>")

        def log_message(self, *_args):
            pass

    server = http.server.HTTPServer(("localhost", port), Handler)
    print(f"Opening browser to: {auth_url}")
    webbrowser.open(auth_url)
    print(f"Waiting for the redirect on {redirect_uri} ...")
    server.handle_request()
    server.server_close()

    if "full_url" not in captured:
        raise SystemExit("Did not receive the OAuth redirect — check the callback path/port and try again.")

    flow.fetch_token(authorization_response=captured["full_url"])
    return flow.credentials


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ACCOUNTS:
        print(f"Usage: python3 gmail_auth.py <{'|'.join(ACCOUNTS)}>")
        sys.exit(1)

    key = sys.argv[1]
    account = ACCOUNTS[key]
    secret_path = os.path.join(CREDS_DIR, account["client_secret"])
    token_path = os.path.join(CREDS_DIR, f"{key}_token.json")

    if not os.path.exists(secret_path):
        print(f"Missing client secret file: {secret_path}")
        sys.exit(1)

    print(f"Authorizing {account['email']} — a browser window will open.")
    print("Log in as that account and click Allow. This script never sees your password.")

    with open(secret_path) as f:
        secret_data = json.load(f)
    client_type = "installed" if "installed" in secret_data else "web"
    redirect_uri = secret_data[client_type]["redirect_uris"][0]

    if client_type == "installed" and urllib.parse.urlparse(redirect_uri).port is None:
        flow = InstalledAppFlow.from_client_secrets_file(secret_path, SCOPES)
        creds = flow.run_local_server(
            port=0,
            open_browser=True,
            prompt="select_account consent",
            login_hint=account["email"],
        )
    else:
        creds = _authorize_fixed_redirect(secret_path, redirect_uri, account["email"])

    with open(token_path, "w") as f:
        f.write(creds.to_json())
    os.chmod(token_path, 0o600)

    print(f"Saved token: {token_path}")
    print(f"{account['email']} is now connected for read + draft access.")


if __name__ == "__main__":
    main()

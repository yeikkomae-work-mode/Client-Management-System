#!/usr/bin/env python3
"""
Gmail REST client for accounts authorized via gmail_auth.py.

CLI usage:
    python3 gmail_client.py <account_key> list-unread [max_results]
    python3 gmail_client.py <account_key> get-thread <thread_id>
    python3 gmail_client.py <account_key> create-draft <to> <subject> <body_file>
"""
import base64
import json
import os
import sys
from email.mime.text import MIMEText

import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

CREDS_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../OAuth Credentials"
API_BASE = "https://gmail.googleapis.com/gmail/v1/users/me"


def _load_credentials(account_key):
    token_path = os.path.join(CREDS_DIR, f"{account_key}_token.json")
    if not os.path.exists(token_path):
        raise SystemExit(
            f"No token for '{account_key}'. Run: python3 gmail_auth.py {account_key}"
        )
    creds = Credentials.from_authorized_user_file(token_path)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(token_path, "w") as f:
            f.write(creds.to_json())
        os.chmod(token_path, 0o600)
    return creds


def _get(account_key, path, params=None):
    creds = _load_credentials(account_key)
    resp = requests.get(
        f"{API_BASE}{path}",
        headers={"Authorization": f"Bearer {creds.token}"},
        params=params or {},
    )
    resp.raise_for_status()
    return resp.json()


def _post(account_key, path, body):
    creds = _load_credentials(account_key)
    resp = requests.post(
        f"{API_BASE}{path}",
        headers={"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"},
        json=body,
    )
    resp.raise_for_status()
    return resp.json()


def list_unread(account_key, max_results=20):
    return _get(
        account_key,
        "/threads",
        params={"q": "is:unread -in:draft", "maxResults": max_results},
    )


def get_thread(account_key, thread_id):
    return _get(account_key, f"/threads/{thread_id}", params={"format": "full"})


def create_draft(account_key, to, subject, body_text, thread_id=None):
    message = MIMEText(body_text)
    message["to"] = to
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    payload = {"message": {"raw": raw}}
    if thread_id:
        payload["message"]["threadId"] = thread_id
    return _post(account_key, "/drafts", payload)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    account_key, command = sys.argv[1], sys.argv[2]

    if command == "list-unread":
        max_results = int(sys.argv[3]) if len(sys.argv) > 3 else 20
        print(json.dumps(list_unread(account_key, max_results), indent=2))
    elif command == "get-thread":
        print(json.dumps(get_thread(account_key, sys.argv[3]), indent=2))
    elif command == "create-draft":
        to, subject, body_file = sys.argv[3], sys.argv[4], sys.argv[5]
        with open(body_file) as f:
            body_text = f.read()
        print(json.dumps(create_draft(account_key, to, subject, body_text), indent=2))
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()

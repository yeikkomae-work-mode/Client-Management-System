"""Diff the live PlusVibe unibox against reply_watch_state.json and print any
genuinely new inbound replies (direction=IN, excluding AUTOMATIC_REPLY and
OUT_OF_OFFICE auto-responder noise) as JSON. Does not update the state file --
the caller updates it after successfully notifying, so a failed notification
doesn't silently swallow a reply.

Dedups on `message_id` (the email's real Message-ID header), not `id` --
`id` was observed to change across calls for the same email (looks like a
reindexed/synthetic id, not a stable primary key), which would otherwise
cause every run to re-report the same emails as new.

Usage: PV_KEY=... PV_WS=... python3 check_new_replies.py
"""
import json, os, subprocess, sys

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]
STATE_PATH = os.path.join(os.path.dirname(__file__), "reply_watch_state.json")
NOISE_LABELS = {"AUTOMATIC_REPLY", "OUT_OF_OFFICE"}


def call(method, path, query=""):
    url = f"{API}/{path}" + (f"?{query}" if query else "")
    cmd = ["curl", "-sS", "-X", method, url, "-H", f"x-api-key: {KEY}"]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def main():
    state = json.load(open(STATE_PATH)) if os.path.exists(STATE_PATH) else {"seen_message_ids": []}
    seen = set(state.get("seen_message_ids", []))

    data = call("GET", "unibox/emails", query=f"workspace_id={WS}")
    emails = data.get("data", [])

    new_genuine = []
    all_message_ids = []
    for e in emails:
        mid = e.get("message_id")
        all_message_ids.append(mid)
        if mid in seen:
            continue
        if e.get("direction") != "IN":
            continue
        if e.get("label") in NOISE_LABELS:
            continue
        new_genuine.append({
            "message_id": mid,
            "timestamp": e.get("timestamp_created"),
            "campaign_id": e.get("campaign_id"),
            "label": e.get("label"),
            "from": e.get("from_address_email"),
            "to": e.get("to_address_email_list"),
            "subject": e.get("subject"),
        })

    print(json.dumps({"new_genuine_replies": new_genuine, "all_current_message_ids": all_message_ids}, indent=2))


if __name__ == "__main__":
    main()

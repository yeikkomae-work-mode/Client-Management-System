"""Diff the live PlusVibe unibox against reply_watch_state.json and print any
genuinely new inbound replies (direction=IN, excluding AUTOMATIC_REPLY and
OUT_OF_OFFICE auto-responder noise) as JSON. Does not update the state file --
the caller updates it after successfully notifying, so a failed notification
doesn't silently swallow a reply.

Dedups on `message_id` (the email's real Message-ID header), not `id` --
`id` was observed to change across calls for the same email (looks like a
reindexed/synthetic id, not a stable primary key), which would otherwise
cause every run to re-report the same emails as new.

PlusVibe's AI reply-classifier doesn't label a message instantly -- the first
hourly check after a real send can catch a message with label == "" before
PlusVibe has tagged it AUTOMATIC_REPLY/OUT_OF_OFFICE (observed live: a HubSpot
ticket auto-ack from höfats sat unlabeled for at least one run). An empty
label is therefore left PENDING here -- excluded from both new_genuine_replies
and all_current_message_ids, so it isn't marked seen and gets re-evaluated
next hour once PlusVibe finishes classifying it (or forever, worst case, which
just means an occasional unlabeled message never surfaces -- better than
emailing on every auto-ack). A body-text check backstops cases where PlusVibe
never assigns a label at all.

Usage: PV_KEY=... PV_WS=... python3 check_new_replies.py
"""
import json, os, re, subprocess, sys

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]
STATE_PATH = os.path.join(os.path.dirname(__file__), "reply_watch_state.json")
NOISE_LABELS = {"AUTOMATIC_REPLY", "OUT_OF_OFFICE"}
AUTO_ACK_MARKERS = [
    "out of office", "automatic reply", "auto-reply", "away from",
    "fuori ufficio", "abwesenheit", "urlaub", "nicht im büro",
    "vielen dank für deine nachricht", "wir haben deine nachricht erhalten",
    "wir haben deine anfrage erhalten", "anfrage eingegangen", "anfrage erhalten",
    "ihre nachricht ist eingegangen", "deine e-mail ist eingegangen",
    "thank you for your message", "thank you for contacting",
    "delivery status notification", "undeliverable", "mail delivery failed",
]


def call(method, path, query=""):
    url = f"{API}/{path}" + (f"?{query}" if query else "")
    cmd = ["curl", "-sS", "-X", method, url, "-H", f"x-api-key: {KEY}"]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def looks_like_auto_ack(email):
    subj = (email.get("subject") or "").lower()
    body = email.get("body") or {}
    text = (body.get("text") or "").lower() if isinstance(body, dict) else ""
    haystack = subj + " " + text[:2000]
    return any(marker in haystack for marker in AUTO_ACK_MARKERS)


def main():
    state = json.load(open(STATE_PATH)) if os.path.exists(STATE_PATH) else {"seen_message_ids": []}
    seen = set(state.get("seen_message_ids", []))

    data = call("GET", "unibox/emails", query=f"workspace_id={WS}")
    emails = data.get("data", [])

    new_genuine = []
    all_message_ids = []
    for e in emails:
        mid = e.get("message_id")
        if mid in seen:
            all_message_ids.append(mid)
            continue
        if e.get("direction") != "IN":
            all_message_ids.append(mid)
            continue
        label = e.get("label")
        if label in NOISE_LABELS:
            all_message_ids.append(mid)
            continue
        if not label:
            if looks_like_auto_ack(e):
                all_message_ids.append(mid)
            # else: pending classification -- omit from all_message_ids so
            # it isn't marked seen, and gets re-checked next run.
            continue
        all_message_ids.append(mid)
        new_genuine.append({
            "message_id": mid,
            "timestamp": e.get("timestamp_created"),
            "campaign_id": e.get("campaign_id"),
            "label": label,
            "from": e.get("from_address_email"),
            "to": e.get("to_address_email_list"),
            "subject": e.get("subject"),
        })

    print(json.dumps({"new_genuine_replies": new_genuine, "all_current_message_ids": all_message_ids}, indent=2))


if __name__ == "__main__":
    main()

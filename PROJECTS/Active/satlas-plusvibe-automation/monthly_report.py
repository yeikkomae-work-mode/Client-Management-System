#!/usr/bin/env python3
"""Satlas monthly PlusVibe -> Notion Email KPI rollup.

Scheduled to run daily (launchd can't express "last Thursday of month"
directly), but no-ops unless today actually is the last Thursday of the
month. Rolls the month-to-date into one Notion row. If any source looks
unreliable (a pull failed, or everything came back zero), drafts the row
to a local file instead of writing to the cross-team-visible Notion table.
"""
import calendar
import datetime
import json
import os
import sys
from dotenv import load_dotenv

from plusvibe_client import PlusVibeClient, PlusVibeError
from notion_client_min import NotionMinClient, NotionError
from runlog import RunLog

load_dotenv()

DRAFTS_DIR = os.path.join(os.path.dirname(__file__), "drafts")


def is_last_thursday(today: datetime.date) -> bool:
    if today.weekday() != 3:  # Monday=0 ... Thursday=3
        return False
    last_day = calendar.monthrange(today.year, today.month)[1]
    return today.day + 7 > last_day


def main():
    today = datetime.date.today()
    log = RunLog("monthly")

    if not is_last_thursday(today):
        log.info(f"{today} is not the last Thursday of the month — no-op")
        return

    log.info(f"Running monthly rollup for {today.strftime('%B %Y')}")
    month_start = today.replace(day=1)

    pv = PlusVibeClient()
    confident = True
    totals = {"sent": 0, "contacted": 0, "replied": 0, "positive": 0, "bounced": 0}

    try:
        campaigns = pv.active_campaigns()
        log.info(f"Pulled {len(campaigns)} active campaigns")
    except PlusVibeError as e:
        log.error(f"Campaign list failed: {e}")
        campaigns = []
        confident = False

    for c in campaigns:
        try:
            stats = pv.campaign_stats(c["id"], month_start.isoformat(), today.isoformat())
        except PlusVibeError as e:
            log.missing(f"stats for {c['name']}", str(e))
            confident = False
            continue
        totals["sent"] += stats.get("sent_count", 0) or 0
        totals["contacted"] += stats.get("lead_contacted_count", 0) or 0
        totals["replied"] += stats.get("replied_count", 0) or 0
        totals["positive"] += stats.get("positive_reply_count", 0) or 0
        totals["bounced"] += stats.get("bounced_count", 0) or 0

    try:
        health = pv.inbox_health_summary()
        mailboxes_live = health["active"]
        inbox_health_str = f"{health['summary']} (as of {today})"
    except PlusVibeError as e:
        log.missing("inbox health", str(e))
        mailboxes_live = None
        inbox_health_str = "Not available this run"
        confident = False

    millionverifier_credits = fetch_millionverifier_credits(log)
    apollo_credits = None   # No working balance endpoint found yet — see README "Known gaps"
    plusvibe_credits = None  # Same — flag rather than guess
    log.missing("Apollo credits", "no working balance endpoint identified yet")
    log.missing("PlusVibe credits", "no working balance endpoint identified yet")

    if totals["sent"] == 0:
        confident = False
        log.info("All-zero totals this month — treating as low-confidence")

    bounce_rate = totals["bounced"] / totals["sent"] if totals["sent"] else None
    title = f"{today.strftime('%B %Y')} (to {today.day})" if today.day != calendar.monthrange(today.year, today.month)[1] else today.strftime("%B %Y")

    payload = dict(
        title=title,
        date_start=month_start.isoformat(),
        date_end=today.isoformat(),
        total_sent=totals["sent"],
        total_contacted=totals["contacted"],
        total_replies=totals["replied"],
        positive_replies=totals["positive"],
        bounce_rate=round(bounce_rate, 4) if bounce_rate is not None else 0,
        inbox_health=inbox_health_str,
        mailboxes_live=mailboxes_live or 0,
        notes=f"Auto-generated {today.isoformat()}. " + ("" if confident else "LOW CONFIDENCE — one or more sources failed or returned nothing, see log."),
        apollo_credits=apollo_credits,
        plusvibe_credits=plusvibe_credits,
        millionverifier_credits=millionverifier_credits,
    )

    if not confident:
        os.makedirs(DRAFTS_DIR, exist_ok=True)
        draft_path = os.path.join(DRAFTS_DIR, f"{today.isoformat()}-notion-kpi-draft.json")
        with open(draft_path, "w") as f:
            json.dump(payload, f, indent=2)
        log.info(f"Low confidence — drafted Notion row to {draft_path} instead of writing")
        return

    try:
        notion = NotionMinClient()
        result = notion.create_email_kpi_row(**payload)
        log.wrote("Notion Apollo Email Performance", f"created row '{title}' — {result.get('url', '')}")
    except (NotionError, KeyError) as e:
        os.makedirs(DRAFTS_DIR, exist_ok=True)
        draft_path = os.path.join(DRAFTS_DIR, f"{today.isoformat()}-notion-kpi-draft.json")
        with open(draft_path, "w") as f:
            json.dump(payload, f, indent=2)
        log.error(f"Notion write failed ({e}) — drafted to {draft_path} instead")


def fetch_millionverifier_credits(log: RunLog):
    import requests
    key = os.environ.get("MILLIONVERIFIER_API_KEY")
    if not key:
        log.missing("MillionVerifier credits", "MILLIONVERIFIER_API_KEY not set")
        return None
    try:
        resp = requests.get("https://api.millionverifier.com/api/v3/credits", params={"api": key}, timeout=15)
        resp.raise_for_status()
        return resp.json().get("credits")
    except Exception as e:
        log.missing("MillionVerifier credits", str(e))
        return None


if __name__ == "__main__":
    main()

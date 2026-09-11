#!/usr/bin/env python3
"""Satlas weekly PlusVibe -> Google Sheet update.

Run every Thursday evening (Asia/Manila). Appends one row to the
'Weekly Summary' tab for the Friday-Thursday week ending today, and
refreshes the Audience Revision Tracker's Trend/Status for the campaigns
already listed there. Never overwrites existing rows. If a campaign's
reply rate has declined sharply, drafts an Audience Changes card entry
to a local file for Eikko's review — never posts it anywhere.
"""
import datetime
import os
import sys
from dotenv import load_dotenv

from plusvibe_client import PlusVibeClient, PlusVibeError
from google_sheets import SheetsClient
from runlog import RunLog

load_dotenv()

SHEET_TAB = "Weekly Summary"
DECLINE_RELATIVE_DROP = 0.30
DECLINE_FLOOR = 0.01
DRAFTS_DIR = os.path.join(os.path.dirname(__file__), "drafts")


def week_bounds(today: datetime.date) -> tuple[datetime.date, datetime.date]:
    """Friday-through-Thursday week ending on `today` (expected to be a Thursday)."""
    return today - datetime.timedelta(days=6), today


def pct(numerator: float, denominator: float) -> str:
    if not denominator:
        return "—"
    return f"{100 * numerator / denominator:.2f}%"


def main():
    log = RunLog("weekly")
    today = datetime.date.today()
    week_start, week_end = week_bounds(today)
    log.info(f"Week window: {week_start} to {week_end}")

    pv = PlusVibeClient()
    sheets = SheetsClient()

    try:
        campaigns = pv.active_campaigns()
        log.info(f"Pulled {len(campaigns)} active campaigns from PlusVibe")
    except PlusVibeError as e:
        log.error(f"Could not pull campaign list: {e}")
        sys.exit(1)

    totals = {"sent": 0, "contacted": 0, "replied": 0, "positive": 0, "bounced": 0}
    per_campaign = {}
    for c in campaigns:
        cid, name = c["id"], c["name"]
        try:
            stats = pv.campaign_stats(cid, week_start.isoformat(), week_end.isoformat())
        except PlusVibeError as e:
            log.missing(f"stats for {name}", str(e))
            continue
        per_campaign[name] = stats
        totals["sent"] += stats.get("sent_count", 0) or 0
        totals["contacted"] += stats.get("lead_contacted_count", 0) or 0
        totals["replied"] += stats.get("replied_count", 0) or 0
        totals["positive"] += stats.get("positive_reply_count", 0) or 0
        totals["bounced"] += stats.get("bounced_count", 0) or 0

    try:
        health = pv.inbox_health_summary()
        health_note = f"{health['summary']} (as of {today})"
    except PlusVibeError as e:
        log.missing("inbox health", str(e))
        health_note = "Not available this run — PlusVibe account/list call failed"

    row = [
        week_start.strftime("%-d %b %Y"),
        totals["sent"],
        totals["contacted"],
        pct(totals["replied"], totals["contacted"]),
        totals["positive"],
        pct(totals["positive"], totals["replied"]),
        pct(totals["bounced"], totals["sent"]),
        health_note,
        "",
    ]

    try:
        sheets.append(f"'{SHEET_TAB}'!A4:I", [row])
        log.wrote("Google Sheet Weekly Summary", f"appended row for week of {week_start}")
    except Exception as e:
        log.error(f"Sheet append failed: {e}")
        sys.exit(1)

    check_audience_decline(sheets, log, week_start, totals)


def check_audience_decline(sheets: SheetsClient, log: RunLog, week_start, this_week_totals):
    """Compares this week's reply rate to the trailing 3-week average and flags
    early decline — drafts an Audience Changes card entry locally, never posts it."""
    history = sheets.read(f"'{SHEET_TAB}'!A5:D1000")
    reply_rates = []
    for r in history[-4:-1] if len(history) >= 4 else []:
        try:
            reply_rates.append(float(r[3].strip("%")))
        except (IndexError, ValueError):
            continue
    if not reply_rates:
        log.info("Not enough history yet to evaluate decline trend")
        return

    trailing_avg = sum(reply_rates) / len(reply_rates)
    this_week_rate = 100 * this_week_totals["replied"] / this_week_totals["contacted"] if this_week_totals["contacted"] else 0
    relative_drop = (trailing_avg - this_week_rate) / trailing_avg if trailing_avg else 0

    declining = relative_drop >= DECLINE_RELATIVE_DROP or this_week_rate < DECLINE_FLOOR * 100
    log.info(f"This week reply rate {this_week_rate:.2f}% vs trailing avg {trailing_avg:.2f}% (drop {relative_drop:.0%})")

    if not declining:
        return

    os.makedirs(DRAFTS_DIR, exist_ok=True)
    draft_path = os.path.join(DRAFTS_DIR, f"{week_start.isoformat()}-audience-change-draft.md")
    with open(draft_path, "w") as f:
        f.write(f"""# DRAFT — Audience Changes card entry (NOT posted, review before pasting into Notion)

Date: {week_start}
Change: Reply rate dropped to {this_week_rate:.2f}% this week vs a {trailing_avg:.2f}% trailing 3-week average
  ({relative_drop:.0%} relative drop) — flagging early per the decline-detection rule
  (>=30% relative drop or <1% floor), before it becomes urgent.
Impacts: Eikko / Hugh — review whether the current audience needs revising.

(This file is a draft only. Nothing has been posted to Notion or shared with Ally/Hugh.)
""")
    log.info(f"Decline detected — drafted audience-change note to {draft_path} (not posted)")


if __name__ == "__main__":
    main()

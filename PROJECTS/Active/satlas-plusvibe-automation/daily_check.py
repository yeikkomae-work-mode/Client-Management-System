#!/usr/bin/env python3
"""Satlas daily check: positive-reply drought + inbox health -> email.

Runs every day. Always sends an email (a daily habit-check, not just an
alert-only ping) covering current inbox health, plus a warning section
for any actively-sending campaign that's had zero positive replies for
the last DROUGHT_DAYS days.
"""
import datetime
import os
import smtplib
import sys
from email.mime.text import MIMEText
from dotenv import load_dotenv

from plusvibe_client import PlusVibeClient, PlusVibeError
from runlog import RunLog

load_dotenv()

DROUGHT_DAYS = 5


def main():
    log = RunLog("daily")
    today = datetime.date.today()
    window_start = today - datetime.timedelta(days=DROUGHT_DAYS - 1)

    pv = PlusVibeClient()
    drought_campaigns = []
    health_line = "Inbox health: not available this run"

    try:
        campaigns = pv.active_campaigns()
        log.info(f"Checking {len(campaigns)} active campaigns for a {DROUGHT_DAYS}-day positive-reply drought")
        for c in campaigns:
            try:
                stats = pv.campaign_stats(c["id"], window_start.isoformat(), today.isoformat())
            except PlusVibeError as e:
                log.missing(f"drought check for {c['name']}", str(e))
                continue
            sent = stats.get("sent_count", 0) or 0
            positive = stats.get("positive_reply_count", 0) or 0
            if sent > 0 and positive == 0:
                drought_campaigns.append(c["name"])
    except PlusVibeError as e:
        log.error(f"Could not pull campaign list: {e}")

    try:
        health = pv.inbox_health_summary()
        health_line = f"Inbox health: {health['summary']}"
    except PlusVibeError as e:
        log.missing("inbox health", str(e))

    body_lines = [
        f"Satlas Daily Check — {today.isoformat()}",
        "",
        health_line,
        "",
    ]
    if drought_campaigns:
        body_lines.append(f"⚠️ Positive Reply Drought (0 positive replies in the last {DROUGHT_DAYS} days, still sending):")
        body_lines.extend(f"  - {name}" for name in drought_campaigns)
    else:
        body_lines.append(f"No campaigns in a {DROUGHT_DAYS}-day positive-reply drought today.")

    send_email("\n".join(body_lines), today, log)


def send_email(body: str, today: datetime.date, log: RunLog):
    from_addr = os.environ["SATLAS_FROM_EMAIL"]
    to_addr = os.environ["PERSONAL_EMAIL"]
    gmail_user = os.environ["GMAIL_SMTP_USER"]
    app_password = os.environ["GMAIL_APP_PASSWORD"]

    msg = MIMEText(body)
    msg["Subject"] = f"Satlas Daily Check — Reply Drought & Inbox Health ({today.isoformat()})"
    msg["From"] = from_addr
    msg["To"] = to_addr

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as s:
            s.starttls()
            s.login(gmail_user, app_password)
            s.sendmail(from_addr, [to_addr], msg.as_string())
        log.wrote("Email", f"sent daily check to {to_addr} from {from_addr}")
    except Exception as e:
        log.error(f"Email send failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

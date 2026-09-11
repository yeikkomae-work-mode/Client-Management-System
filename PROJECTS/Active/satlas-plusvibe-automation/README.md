# Satlas PlusVibe Reporting Automation

Three standalone Python scripts, no Claude Code / MCP dependency at runtime — they authenticate with their own API keys, so they work headless on a schedule.

| Script | Runs | Does |
|---|---|---|
| `weekly_report.py` | Every Thursday evening | Appends one row to the Google Sheet "Weekly Summary" tab for the week just finished (Fri-Thu). Checks reply-rate decline vs trailing 3-week average; if declining, drafts an Audience Changes note to `drafts/` — never posts it anywhere. |
| `monthly_report.py` | Every day (self-guards) | Only actually does anything on the last Thursday of the month. Rolls the month-to-date into one row in the Notion "Apollo Email Performance" database. If any data source failed or looks unreliable, drafts the row to `drafts/` as JSON instead of writing to Notion. |
| `daily_check.py` | Every day | Emails you (from `eikko@satlas.com.au` to `yeikkomae@gmail.com`) current inbox health plus a list of any actively-sending campaign with zero positive replies in the last 5 days. Sends every day regardless, not alert-only. |

Every run writes a dated log to `logs/YYYY-MM-DD-<job>.log` — what it pulled, what it wrote, and anything it couldn't get.

## Setup (one-time)

```bash
cd PROJECTS/Active/satlas-plusvibe-automation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in `.env` with real values:

- **PlusVibe**: the key you already have.
- **Google**: `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` from the OAuth client JSON you uploaded; `GOOGLE_REFRESH_TOKEN` from the token this session already generated (ask me for it, or redo the one-time consent flow — see "Known gaps" below for why this session's copy can't just be handed over as a file).
- **Notion**: still needs a fresh internal integration secret — see "Known gaps".
- **MillionVerifier**: the key you already have.
- **Apollo**: the key you already have (balance endpoint still unresolved, see below).
- **Gmail**: the app password you already generated.

Test each script manually once before scheduling anything:

```bash
python3 weekly_report.py
python3 monthly_report.py   # no-ops unless run on the actual last Thursday
python3 daily_check.py
```

Check the `logs/` output and the Sheet/Notion/inbox after each manual run before trusting the schedule.

## Installing the launchd jobs

**Do this only after you've reviewed the plist files below and are happy with the schedule.** Nothing installs itself.

1. Edit each `.plist` in `launchd/` and replace every `REPLACE_WITH_ABSOLUTE_PATH` with the real absolute path to this folder on your Mac (e.g. `/Users/eikko/Client-Management-System/PROJECTS/Active/satlas-plusvibe-automation`). Also change `/usr/bin/python3` to your venv's python if you used one (`.venv/bin/python3`, absolute path).
2. Copy them into place and load:

```bash
cp launchd/com.satlas.weekly-report.plist ~/Library/LaunchAgents/
cp launchd/com.satlas.monthly-report.plist ~/Library/LaunchAgents/
cp launchd/com.satlas.daily-check.plist ~/Library/LaunchAgents/

launchctl load -w ~/Library/LaunchAgents/com.satlas.weekly-report.plist
launchctl load -w ~/Library/LaunchAgents/com.satlas.monthly-report.plist
launchctl load -w ~/Library/LaunchAgents/com.satlas.daily-check.plist
```

To check they're loaded: `launchctl list | grep satlas`
To run one immediately without waiting for its schedule (useful for testing): `launchctl start com.satlas.daily-check`
To uninstall: `launchctl unload ~/Library/LaunchAgents/com.satlas.<name>.plist && rm ~/Library/LaunchAgents/com.satlas.<name>.plist`

**Schedule assumes your Mac's system clock is set to Asia/Manila** (launchd's `StartCalendarInterval` uses local system time, not UTC). If your Mac is on a different timezone, adjust the `Hour`/`Minute` values accordingly:
- Weekly: Thursdays 18:00
- Monthly: daily 19:00 (self-guards to last Thursday only)
- Daily check: daily 08:00

## Known gaps — need your input before these are fully live

1. **Notion write needs its own credential.** The Notion access used earlier in this chat is a *connector* tied to this conversation — it can't be exported to a standalone script. You need to:
   - Go to `notion.so/my-integrations` (while logged into the Satlas Notion account) → New integration → Internal → copy the secret.
   - Open the "Satlas" page and the "Apollo Email Performance" database → `•••` → Connections → add that integration to both.
   - Paste the secret into `.env` as `NOTION_TOKEN`.
   Until this is done, `monthly_report.py` will fail the Notion write and fall back to drafting the row locally instead — it won't silently do nothing, but it also won't reach Notion.

2. **Apollo and PlusVibe credit balances** — `monthly_report.py` currently leaves these blank on the Notion row (MillionVerifier's is filled in fine). I couldn't find a working balance endpoint for either via their key-based REST APIs after a reasonable search. If you know the right endpoint (or it's only visible in-app), let me know and I'll wire it in — otherwise the script will keep flagging this in its log every run rather than guessing.

3. **`GOOGLE_REFRESH_TOKEN`** — this session generated one during the OAuth flow earlier. It's currently only in this session's scratchpad, not in this repo (by design — it's a live credential). Ask me for it directly, or redo the consent flow yourself using the same OAuth client JSON, scope `https://www.googleapis.com/auth/spreadsheets`.

## Design notes

- `weekly_report.py` uses Sheets' `:append` endpoint specifically (not overwrite) — it always adds a new row, never touches existing ones.
- The decline-detection threshold (30% relative drop vs trailing 3-week average, or reply rate under 1%) lives as constants at the top of `weekly_report.py` — change `DECLINE_RELATIVE_DROP` / `DECLINE_FLOOR` there if you want different sensitivity.
- Nothing in any of these three scripts posts to the cross-team "Audience Changes" Notion card automatically — that stays a manual copy-paste from the drafted file, per the original requirement that audience changes need Hugh's visibility window before acting.

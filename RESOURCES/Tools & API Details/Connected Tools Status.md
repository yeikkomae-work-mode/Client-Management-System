# Connected Tools Status — API & Connector Tracking

**Purpose:** Track which tools have working API/connector access and which require manual input.

---

## CURRENT STATUS

### ✓ CONFIRMED CONNECTED (Auto-pull in "Good Morning")

| Tool | Client(s) | Status | Notes |
|------|-----------|--------|-------|
| Smartlead | Yoni | ✓ Connected | Pulling prospect tags, interested count |
| Pipedrive | Yoni | ✓ Connected | Pulling prospect stages, pipeline data |
| TimeDoctors | Yoni | ✓ Connected | Auto-tracking hours (5 hrs/day, 9pm-5am PHT) |

### ✗ CANNOT BE AUTOMATED (Manual Input Required)

| Tool | Client(s) | Reason | Alternative |
|------|-----------|--------|-------------|
| Hubspot | Chris Caffera | Automation not possible | Manual metrics at end of day |
| Lemlist | Chris Caffera | Automation not possible | Manual metrics at end of day |
| LinkedIn | Chris Caffera | Platform restriction | Manual post/engagement tracking |

| Google Sheets (write) | Eikko / Penji | ✓ Connected (service account) | Service account `claude@noted-minutia-506607-j3.iam.gserviceaccount.com`, key stored at `RESOURCES/Tools & API Details/OAuth Credentials/google-service-account-cms-sheets-writer-credentials.json` (gitignored, two independent rules). Uses the Sheets API v4 directly (`google-auth` + `google-api-python-client`, not an MCP tool) — the Drive MCP connector only supports read/download/create-new-file, no in-place writes to an existing sheet. Verified 2026-08-25: appended 85 rows to the "Gojiberry Listing" tab (gid 1776270089) of Eikko's "Agency Master List" spreadsheet. Write access is per-sheet — only works on sheets explicitly shared with the service account email as Editor. To extend to another sheet, share it with that email first. |
### ⚠️ LOCAL-ONLY (works on Eikko's Mac, NOT from cloud/web Claude sessions)

| Tool | Client(s) | Status | Notes |
|------|-----------|--------|-------|
| Gojiberry | Penji | ✓ Connected (key) | Hosted MCP at `https://mcp.gojiberry.ai/mcp`, wired in `.mcp.json` as `gojiberry` via `Authorization: Bearer ${GOJIBERRY_API_KEY}`. Verified working 2026-08-25 from the cloud container — handshake succeeded, **25 tools** exposed. Server also supports OAuth (PKCE, dynamic registration) as an alternative. ⚠️ The issued key is an **org-level** credential for `business@penji.co` (not Eikko's personal login), valid until **2036-08-24**, and includes write/send tools: `impersonate_user`, `send_unibox_linkedin_message`, `update_campaign`, `create_contact`. Treat as production access. |
| AdsPower | Penji | ⚠️ Local-only | API key held (stored in `tools_api_details.md`, gitignored). The AdsPower API is served by the desktop app on `localhost:50325` — `local.adspower.net` resolves to loopback by design, so a remote/web Claude session cannot reach it. Verified 2026-08-25: connection refused from the cloud container. Wired up in `.mcp.json` (`adspower-local-api`) + the `adspower-browser` skill; both only function in a **local** Claude Code session with AdsPower running. |

### ❓ TO BE TESTED (Report Back After Testing)

| Tool | Client(s) | Target Status | Action |
|------|-----------|----------------|--------|
| Apollo | Chris Caffera, Chris Drew, Krishna | Determine if API-able | Test connection, report if works |
| Instantly | Chris Drew | Determine if API-able | Test connection, report if works |
| Zapmail | Chris Drew | Determine if API-able | Test connection, report if works |
| Inboxkit | Chris Drew | Determine if API-able | Test connection, report if works |
| PlusVibe | Chris Drew | Determine if API-able | Test connection, report if works |
| Notion | Chris Drew | Determine if API-able | Test connection, report if works |

---

## HOW TO REPORT BACK

**When you test an API/connector, tell me:**

```
TOOL TEST RESULT

Tool: [Tool name]
Client: [Client using it]
Result: [Connected / Cannot be automated]
Details: [If connected: what data can be pulled? If failed: what's the blocker?]
```

**Example (if it connects):**
```
TOOL TEST RESULT

Tool: Apollo
Client: Chris Caffera & Chris Drew
Result: Connected
Details: Can pull replies per sequence, open rates, bounce status. Auto-pulls daily at 8am PHT.
```

**Example (if it doesn't):**
```
TOOL TEST RESULT

Tool: Instantly
Client: Chris Drew
Result: Cannot be automated
Details: API requires manual refresh; will add to manual input list.
```

---

## ONCE YOU REPORT

I'll update this file and the automation workflows:
- If connected: I'll pull from it automatically in "good morning" recap
- If manual: I'll add it to the manual metrics template

---

## WHAT TO PULL (Per Tool Type)

### Email Campaign Tools (Apollo, Instantly, Zapmail, Inboxkit, etc.)
- **Metrics to track:** Emails sent, open rate %, reply rate %, bounces, clicks, sequences active
- **Frequency:** Daily or as-needed

### CRM Tools (Hubspot, Pipedrive)
- **Metrics to track:** Prospects added, stage moved, reply rate, close rate, deal status
- **Frequency:** Daily or as-needed

### Outreach Tools (Smartlead, PlusVibe)
- **Metrics to track:** Prospects tagged, interested count, inbox health %, replies
- **Frequency:** Daily (auto-pull)

### Content/Social Tools (LinkedIn, Notion)
- **Metrics to track:** Posts scheduled, engagements, profile views, notes/updates
- **Frequency:** Manual (as you work)

---

## NEXT STEPS

1. **Test the tools listed in "TO BE TESTED"**
2. **Report back with connection status**
3. **I'll update automation to pull from newly connected tools**
4. **Manual input list shrinks as more tools connect**

---

## STORAGE

Keep this file updated as tools are tested. It's your source of truth for what gets auto-pulled vs. manually logged.

**Last updated:** 2026-08-25 — Added AdsPower (Penji, local-only), Gojiberry (Penji, hosted MCP, org key verified working — 25 tools), and Google Sheets write access (service account, verified with a live 85-row append).

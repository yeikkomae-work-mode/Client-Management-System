# Smartlead ↔ Pipedrive Automation — Python Build (Archived Reference)

**Built:** August 5–6, 2026 | **Status:** Original local Python build; largely superseded by the MCP-connector-based workflow now documented in `Smartlead-Pipedrive-Automation-Workflow.md` (Aug 12) and `Yoni - Live Automation Setup Runbook.md`.

*(Consolidated from 3 companion docs — AUTOMATION-SMARTLEAD-PIPEDRIVE-SYNC.md, DEPLOYMENT-GUIDE.md, IMPLEMENTATION-BLUEPRINT.md — which all described this one build effort from different angles: concept, deployment steps, technical architecture. Merged here to remove duplication. Keeping this for reference in case the local Python/cron/webhook approach is ever needed again instead of the MCP-connector approach.)*

⚠️ **Security note:** the original docs had live Smartlead and Pipedrive API keys pasted in plain text. Redacted below — current keys live in `RESOURCES/Tools & API Details/tools_api_details.md` and the project's own `.env` file (`PROJECTS/Active/smartlead-pipedrive-automation/.env`). Treat both as sensitive; don't re-paste keys into markdown docs going forward.

---

## What This Does

Syncs qualified leads from Smartlead → Pipedrive automatically:

| Source | Trigger | Action | Pipedrive Label |
|--------|---------|--------|-----------------|
| Smartlead Master Inbox | Tag: "Interested" | Create Person + Activity | `smartlead` |
| Smartlead Master Inbox | Tag: "Follow-up" | Create Person + Activity | `smartlead` |
| Gmail | `notifications@calendly.com` email | Create Person + Activity | `customers+yoni` |

Plus: auto-blocks the domain in Smartlead for Interested/Follow-up leads.

---

## System Architecture

Two components, running locally:

1. **Daily cron job** (9:30 AM) — fetches all Interested/Follow-up replies, creates/updates Pipedrive Person + Activity records, blocks domains, updates `Daily-Lead-Summary.md`.
2. **Webhook server** (`localhost:5000`, must stay running) — receives Smartlead tag events and Gmail Calendly notifications in real time, syncs instantly.

```
TRIGGER SOURCES → NORMALIZE & VALIDATE → PIPEDRIVE LOOKUP/SYNC → SMARTLEAD DOMAIN BLOCK → REPORTING
```

**Pipedrive sync steps:** search Person by email → if not found, search/create Organization → create Person (name, email, org_id, label) → create Activity (subject, notes, assigned to Yoni, due +3 days) → log to `Smartlead-Pipedrive-Sync-Log.md`.

**Domain block (Smartlead sources only):** extract domain from email → POST to blocklist endpoint → log success/already-blocked/error.

---

## Codebase

Lives at `PROJECTS/Active/smartlead-pipedrive-automation/`:

```
sync_automation.py    # Main script (cron + webhook modes)
webhook_server.py     # Flask webhook listener
sync_engine.py        # Core sync logic
pipedrive_api.py      # Pipedrive API client
smartlead_api.py      # Smartlead API client
logger.py             # Logging & file updates
config.py             # Configuration
.env / .env.example   # Environment variables (keys — do not share)
requirements.txt
README.md
```

## Deployment Steps (if reactivating)

1. `pip install -r requirements.txt`
2. `cp .env.example .env` (keys already configured from `tools_api_details.md`)
3. Test: `python3 sync_automation.py --mode test`
4. Cron: `crontab -e`, add `0 9 * * * /usr/bin/python3 ~/.../sync_automation.py --mode daily >> automation_logs/cron.log 2>&1`
5. Webhook server: `python3 sync_automation.py --mode webhook` (keep terminal open, or run under `screen`/`tmux`)
6. Test webhook: `curl http://127.0.0.1:5000/webhook/health`
7. Verify `Daily-Lead-Summary.md` updates next morning

**Note:** webhook server must stay running or real-time sync stops; cron and webhook run independently and can both be active.

## API Reference (redacted)

**Smartlead** — Base URL `https://api.smartlead.io/v1`, auth header `X-API-Key: [REDACTED — see tools_api_details.md]`
- `GET /inbox/campaigns/{campaign_id}/replies?tag=Interested`
- `POST /settings/blocklist` — body `{"domain": "company.com", "reason": "Synced to Pipedrive"}`

**Pipedrive** — Base URL `https://api.pipedrive.com/v1`, auth header `Authorization: Bearer [REDACTED — see tools_api_details.md]`
- `GET /persons/search?term={email}`
- `POST /persons` — body `{name, email, org_id, label}`
- `GET /organizations/search?term={company_name}`
- `POST /organizations` — body `{name}`
- `POST /activities` — body `{subject, type, person_id, note, due_date, user_id}`

## Error Handling

| Error | Action |
|-------|--------|
| Lead not found in Smartlead | Skip (may be old) |
| Pipedrive rate limit | Retry with backoff |
| Duplicate person (email exists) | Skip Person creation, create Activity anyway |
| Organization creation fails | Create Person without org, flag for manual setup |
| Domain block fails | Log, continue (don't block Person creation) |
| Gmail webhook fails | Retry next cron run |
| Missing required field | Skip lead, flag in error log |

## Monitoring Files

| File | Purpose | Cadence |
|------|---------|---------|
| `Daily-Lead-Summary.md` | EOD report of all syncs | Daily |
| `Automation-Status.md` | System health/errors | Real-time |
| `Smartlead-Pipedrive-Sync-Log.md` | Full audit trail | Real-time |

## Troubleshooting

- **Cron not running:** `crontab -l | grep sync_automation`, check `automation_logs/cron.log`, test manually with `--mode daily`.
- **Webhook not receiving events:** `curl http://127.0.0.1:5000/webhook/health`, check terminal running the webhook for errors.
- **Sync failing for a lead:** check tail of `Smartlead-Pipedrive-Sync-Log.md`.

---

**Why archived:** the operational workflow has since moved to calling Smartlead/Pipedrive directly as connected MCP tools (see `Smartlead-Pipedrive-Automation-Workflow.md`), which doesn't require a locally-running Python webhook server. Keep this doc in case the MCP connector path breaks and the local Python system needs to come back as a fallback.

# Connector Status — Single Source of Truth

**All 10 agents read this before claiming any tool is live.** Update this ONE file when you fix/authorize a connector — don't hand-edit the status inside individual agent files.

**Twin copy in Notion:** [🔌 Connector Status](https://app.notion.com/p/3ba811e21c7f8193a87fd0e68c38987a), inside the [🎛️ VA Command Center](https://app.notion.com/p/3ba811e21c7f8000b6a5f7952cb0c76b). Update both when something changes — this file is the one agents actually read at runtime; the Notion copy is for Eikko to check without opening Claude Code.

**Last verified:** 2026-08-13

| Tool | Status | Notes |
|---|---|---|
| Apollo | ✅ Connected | Raw API key over curl/Bash (`APOLLO_API_KEY` [Satlas/Chris Drew], `APOLLO_API_KEY_ACCOUNT2` [Krishna]) — verified live 2026-08-13 against `/v1/auth/health`. **Not** the Apollo MCP connector, which is unauthenticated. Chris Caffera's segments are actively worked per task-list evidence, but no dedicated key is documented for him — likely shares one of the above. |
| Pipedrive | ✅ Connected | Yoni/Albert Scott CRM |
| Smartlead | ✅ Connected | Scoped to the Albert Scott (Yoni) account only |
| Gmail (yeikkomae@gmail.com) | ✅ Connected | Native claude.ai Gmail connector (MCP). Calendar/Drive also live for this account only. |
| Gmail (eikko@satlas.com.au) | ✅ Connected | **Not** the native connector — claude.ai only permits one Gmail account. Custom OAuth script instead: `RESOURCES/Tools & API Details/Gmail Multi-Account Client/gmail_client.py satlas ...`. Read + draft only, no send scope. |
| Gmail (salesmanager@albertscott.com) | ✅ Connected | Same custom script, account key `albertscott`. Read + draft only. |
| Gmail (eikko.ybanez@fractio.co) | ✅ Connected | Same custom script, account key `fractio`. Read + draft only. |
| Gmail (eikkomaeybanez@gmail.com) | ✅ Connected | Same custom script, account key `personal`. Read + draft only. |
| Notion (this workspace) | ✅ Connected | eikko mae ybanez's Space |
| Satlas team Notion ("Cold Email" hub) | 🟡 Not connected | Different workspace from this one — still needs access |
| PlusVibe (Chris Drew/Satlas) | ✅ Connected | Raw API key over curl/Bash (`SATLAS_PLUSVIBE_API_KEY` + `workspace_id=6a5f60452fd3fe45b2605b48`), not the native connector — verified live 2026-08-13, 13 real campaigns returned. Old key was dead; replaced same day. |
| HubSpot | 🟡 Not connected | Connector exists in registry — needs Eikko to authorize in claude.ai connector settings |
| Slack | 🟡 Not connected | Same — exists, needs authorizing |
| Fireflies | 🟡 Not connected | Needed for live meeting transcript pulls; needs authorizing |
| Instantly (Satlas) | ⚫ Deprecated | Migrated off in early Aug — shouldn't be in active use. Fresh key tested dead 2026-08-13 (`ERR_AUTH_FAILED`) regardless — moot either way, don't wire in. |
| Instantly (Cüneyt/Starfix) | ✅ Active | **Separate account from Satlas's — don't confuse the two.** Live and in active use for this client's 11 campaigns as of 2026-08-13 (`STARFIX_INSTANTLY_API_KEY`). Not yet tested directly against the API by Claude — status per client profile/EOD log, not independently verified here. |
| Hostinger (Starfix — hellostarfix.com, starfix.online, sellervate.net) | ✅ Active | 3 domain-scoped API tokens, all added 2026-08-13 (`STARFIX_HOSTINGER_API_KEY_HELLOSTARFIX/STARFIXONLINE/SELLERVATE`). Received as account access, not yet independently tested against the API by Claude. |
| Porkbun | 🟡 Incomplete | Raw API key tested 2026-08-13 — clean `MISSING_SECRETAPIKEY` response, meaning Porkbun's paired secret key was never stored. Need that from Eikko before this can go live. |
| Zapmail | ⚫ Dead key | Fresh key tested 2026-08-13 — clean `401 Invalid API key` (not a path issue). Needs a new key from the Zapmail dashboard. |
| InboxKit | ❓ Inconclusive | Fresh key tested 2026-08-13 across 4 endpoint guesses — all generic 404s, not auth-rejected. Likely a wrong/undocumented path rather than a dead key. See `tools_api_details.md` for exactly what was tried. |
| MillionVerifier | ⚫ No connector | Manual 2FA login by design — can't be automated regardless |
| Lemlist | ⚫ No connector | Browser-only |
| LinkedIn (personal profiles) | ⚫ No connector | No API path; browser-assisted only, and LinkedIn flags automated activity — keep to drafting, not unattended posting |
| Asana, ClickUp, Trello | ⚫ Not in use | Task tracking currently lives in markdown files (`PROJECTS/Active/`) and Google Sheets, not a PM tool |

**Rule for all agents:** if a task needs a 🔴 or 🟡 or ⚫ item, say so plainly and use the fallback (manual log, browser check, or flag-for-Eikko) instead of reporting fabricated live data.

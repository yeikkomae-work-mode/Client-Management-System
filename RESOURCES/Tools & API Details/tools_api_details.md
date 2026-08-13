# API Credentials Details

---

## 🚀 Satlas Campaign Monitoring Apps (Quick Access)

| Tool | URL | Purpose | Current Status |
|------|-----|---------|-----------------|
| **Zapmail** | https://app.zapmail.ai/domains/connect | Email infrastructure & deliverability | 10 domains connected ✓ |
| **InboxKit** | https://app.inboxkit.com/ | Mailbox management & warmup | 15 domains, 30 mailboxes ✓ |
| **Plusvibe** | https://app.plusvibe.ai/v2/campaigns/ | Outbound campaign management | 4 campaigns, 1,469 leads ✓ |

**Access Method:** Log in with eikko@satlas.com.au (Google OAuth)
**Important:** Use .ai domain suffix (NOT .com)

---

## 1. Satlas Apollo API
- **Environment Variable:** `APOLLO_API_KEY`
- **API Key:** L45tc7GCGIdF8q06cWNqLA
- **Service:** Apollo.io (Lead database & enrichment)
- **Owner:** Satlas
- **Status:** Active

## 2. Krishna Apollo
- **Environment Variable:** `APOLLO_API_KEY_ACCOUNT2`
- **API Key:** Tqu6SgcCjQ18Sam-brrZrA
- **Service:** Apollo.io
- **Owner:** Krishna
- **Status:** Active

## 3. Satlas Instantly API
- **Environment Variable:** `SATLAS_INSTANTLY_API_KEY`
- **API Key:** MjBlOTJlOTktMTQ0Mi00YjY0LTg4NmQtNjk0ODAzMDFkY2JkOmxjampGU05HYUJXaQ== (replaced 2026-08-13, decodes to a `uuid:secret` Basic-auth-style v1 pair)
- **Service:** Instantly (Email outreach & automation)
- **Owner:** Satlas
- **Status:** ❌ Dead — tested 2026-08-13 as both `Authorization: Basic <key>` and `Authorization: Bearer <key>` against `api.instantly.ai/api/v1/campaign/list`, both returned `ERR_AUTH_FAILED`. **Also: Instantly is deprecated** (migrated off to PlusVibe in early Aug per `connector-status.md`) — don't wire this into any agent even if a working key surfaces later.

## 4. Satlas Porkbun API
- **Environment Variable:** `SATLAS_PORKBUN_API_KEY`
- **API Key:** pk1_8b4e9c65c9876183dcfd06848f6db4f6a803f7f353f9fe517fb203b2e8b3c314
- **Service:** Porkbun (Domain registration & purchase)
- **Owner:** Satlas
- **Status:** ⚠️ Incomplete — tested 2026-08-13 against `api.porkbun.com/api/json/v3/ping`, got back a clean `MISSING_SECRETAPIKEY` error. **This key alone isn't enough** — Porkbun requires a paired secret key (format `sk1_...`) that was never stored. Need Eikko to provide it before this can be verified live.

## 5. Satlas Zapmail API
- **Environment Variable:** `SATLAS_ZAPMAIL_API_KEY`
- **API Key:** 5da97441-50ce-4fec-aa28-d612f4cfb118 (replaced 2026-08-13)
- **Service:** Zapmail (Email inboxes management)
- **App URL:** https://app.zapmail.ai/domains/connect
- **API Base:** `https://api.zapmail.ai/api/v2/`
- **Owner:** Satlas
- **Status:** ❌ Dead — tested 2026-08-13 via `x-api-key` and `Authorization: Bearer` against `domains/available`, both returned a clean `401 Invalid API key` (server understood the request, rejected the key itself — not a path/format issue). Needs a fresh key from the Zapmail dashboard (API Settings).
- **Authentication:** eikko@satlas.com.au (Google OAuth) — app login only, separate from the API key above
- **Current Metrics (last known, unverified since):** 10 domains connected with successful connections

## 6. Satlas Inboxkit API
- **Environment Variable:** `SATLAS_INBOXKIT_API_KEY`
- **API Key:** eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjZhNTA1NWI0NDdlNjRmM2E2NzJhZWYzNiIsInR5cGUiOiJhcGkiLCJyb3RhdGlvbiI6ImUxYmE5ZTQyLTY5MzItNDAzYi1iNDY0LWZmMTQ1N2I0MDU0YSIsImlhdCI6MTc4MzY0OTcxNn0.zeR2KaJHhmIc4MPtxTA2FJsIG7D5VDb4FtKdL3qmFws (issued 2026-07-10 per JWT `iat` claim)
- **Service:** Inboxkit (Email inboxes management & warmup)
- **App URL:** https://app.inboxkit.com/
- **Owner:** Satlas
- **Status:** ❓ Inconclusive — tested 2026-08-13 against 4 domain/path combinations (`api.inboxkit.com/v1/api/workspaces`, `api.inboxkit.com/v1/workspaces`, `api.inboxkit.io/v1/inboxes` [DNS doesn't resolve — that domain from the old usage example is wrong], `app.inboxkit.com/api/v1/workspaces`), all returned generic `404 Not found` rather than an auth-specific rejection. Unlike Zapmail's clean 401, this doesn't confirm the key is dead — more likely the correct endpoint path just isn't publicly documented. Would need the exact endpoint from InboxKit support or their dashboard's API reference.
- **Authentication:** eikko@satlas.com.au (Google OAuth) — app login only, separate from the API key above
- **Current Metrics (last known, unverified since):** 15 domains (100% healthy), 30 mailboxes (100% in use)

## 7. Satlas Plusvibe API
- **Environment Variable:** `SATLAS_PLUSVIBE_API_KEY`
- **API Key:** e95e5d13-4c3da07c-417e3e99-0c6f62f7 (replaced 2026-08-13 — old key `84f14202-...` was expired/dead, confirmed via `authtoken_expired` error)
- **Workspace ID:** `6a5f60452fd3fe45b2605b48` ("Eikko's Workspace") — required as a query param on every request
- **Service:** Plusvibe (Outreach campaigns & campaign management)
- **App URL:** https://app.plusvibe.ai/v2/campaigns/
- **API Base:** `https://api.plusvibe.ai/api/v1/` — note the `/api/` prefix, easy to miss
- **Owner:** Satlas
- **Status:** ✅ Active — verified live 2026-08-13 via `campaign/list`, returned 13 real campaigns (7 active: Commercial Real Estate ×3, Financial Planner ×2, Mortgage Brokers ×2; 3 draft under Capital Financing — Trades/Logistics/Labour Hire; 2 draft under the original avatars; 1 completed test)
- **Authentication:** `x-api-key` header (lowercase) + `workspace_id` query param — not the `eikko@satlas.com.au` Google OAuth login used for the app UI
- **Example:** `curl -H "x-api-key: $SATLAS_PLUSVIBE_API_KEY" "https://api.plusvibe.ai/api/v1/campaign/list?workspace_id=6a5f60452fd3fe45b2605b48"`

## 8. Satlas MillionVerifier API
- **Environment Variable:** `SATLAS_MILLIONVERIFIER_API_KEY`
- **API Key:** 9QFS7AuzM5LXz01DgwLCC9wW5
- **Service:** MillionVerifier (Lead enrichment & verification)
- **Owner:** Satlas
- **Status:** Active

## 9. Albertscott Smartlead API
- **Environment Variable:** `ALBERTSCOTT_SMARTLEAD_API_KEY`
- **API Key:** 89e0fb66-3408-4abf-b88c-78793b63a34f_0ue2z1f
- **Service:** Smartlead (Outreach campaigns)
- **Owner:** Albertscott
- **Status:** Active

## 10. Albertscott Pipedrive API
- **Environment Variable:** `ALBERTSCOTT_PIPEDRIVE_API_KEY`
- **API Key:** 82e6b91c07acc4ac052cc4ed4b88da5be3e4a7bf
- **Service:** Pipedrive (CRM)
- **Owner:** Albertscott
- **Status:** Active

## 11. Albertscott Quickemailver API
- **Environment Variable:** `ALBERTSCOTT_QUICKEMAILVER_API_KEY`
- **API Key:** 8b7ccb0824b58c19ec690cf0f9cd0d5df25aeebcf91f73e1285624dc0dfd
- **Service:** Quickemailver (Lead enrichment & database verification)
- **Owner:** Albertscott
- **Status:** Active

## 12. Fractio Hubspot API
- **Environment Variable:** `FRACTIO_HUBSPOT_API_KEY`
- **API Key:** CiRuYTEtNmVkMS01YzlkLTQwYjctOTFkYy1mNDBhYzYxODlhMDUQt6qAFRjrxIQtKhkABeaRgm_zmXsEHfzRBYOAaG-vh2Rfv93mSgNuYTE
- **Service:** Hubspot (CRM)
- **Owner:** Fractio
- **Status:** Active (see also connector-status.md — this same token tested dead 2026-08-13 against the live HubSpot API; token itself may be a placeholder rather than a real credential)

## 13. Starfix Hostinger API — hellostarfix.com
- **Environment Variable:** `STARFIX_HOSTINGER_API_KEY_HELLOSTARFIX`
- **API Key:** c68b2d80e7b245a47e63c2f983f5852f5ae55b84e9fdbc10b6db85d94a8e6b42
- **Service:** Hostinger (Domain & mailbox management)
- **Owner:** Cüneyt (Starfix / Elevate Commerce)
- **Scope:** Access to mailboxes on hellostarfix.com — confirmed covers cueneyt@, daniel@, james@ (all Active, 0% usage, 5.00 GB quota each) as of Aug 13, 2026. Domain-wide scope beyond these 3 not yet confirmed.
- **Status:** Active, untested against API directly (received as account access, not yet validated via an authenticated call)
- **Added:** 2026-08-13

## 14. Starfix Hostinger API — starfix.online
- **Environment Variable:** `STARFIX_HOSTINGER_API_KEY_STARFIXONLINE`
- **API Key:** c0293a5710978255a8720d95beb894cdef56465683b531d9af68069aabc7055f
- **Service:** Hostinger Mail API (Developers → Agentic mail → API access), token name "Claude"
- **Owner:** Cüneyt (Starfix / Elevate Commerce)
- **Scope:** All mailboxes on starfix.online — confirmed covers alex@, ben@, jake@, sam@ (all Active, 0% usage, 5.00 GB quota each) as of Aug 13, 2026. Token permissions: manage all SMTP/IMAP actions, manage webhooks.
- **Status:** Active, untested against API directly
- **Added:** 2026-08-13
- **Note:** alex@starfix.online was found Suspended at the Hostinger account level earlier the same day and was manually unsuspended before this token was created — separate issue from the Instantly-side 554 5.7.1 errors already resolved via the DKIM fix.

## 15. Starfix Hostinger API — sellervate.net
- **Environment Variable:** `STARFIX_HOSTINGER_API_KEY_SELLERVATE`
- **API Key:** a4b69c399cfb325e72a070f6976f5a6c506c0664da11ecb8af9e9648661af7d9
- **Service:** Hostinger Mail API
- **Owner:** Cüneyt (Starfix / Elevate Commerce)
- **Scope:** All 5 mailboxes on sellervate.net (0/5 seats left) — david@, jonas@, maximilian@, sebastian@, tobias@sellervate.net, all Active, 0% usage, 10.00 GB quota each. Note: quota here is 10 GB/mailbox vs. 5 GB on the other two domains, and maximilian@ wasn't in the original Aug 13 Instantly audit — new mailbox on this domain.
- **Status:** Active, untested against API directly
- **Added:** 2026-08-13

## 16. Starfix Instantly API
- **Environment Variable:** `STARFIX_INSTANTLY_API_KEY`
- **API Key:** ZWFlZThjZDUtZjc0MS00ZGUzLTlmY2QtYTA4M2NkZDQ3OTViOkpOREdMdlZDaGVqcA== (decodes to a `uuid:secret` Basic-auth-style v1 pair: `eaee8cd5-f741-4de3-9fcd-a083cdd4795b:JNDGLvVChejp`)
- **Service:** Instantly (Email outreach & automation)
- **Owner:** Cüneyt (Starfix / Elevate Commerce)
- **Status:** Active — this is the key already being used for the mailbox/campaign audits logged in the profile and `OUTPUT/Campaign Tracking/Cüneyt - Starfix Campaign Tracking.md`. **Important: this is a completely separate Instantly account from Satlas's** (entry #3, deprecated/dead) — Instantly is very much live and in active use for this client, don't let Satlas's deprecated status bleed into Cüneyt's work.
- **Added:** 2026-08-13

---

## Usage Instructions

### In Bash Commands
```bash
# Use Satlas Apollo API
curl -H "X-Api-Key: $APOLLO_API_KEY" https://api.apollo.io/v1/...

# Use Krishna Apollo
curl -H "X-Api-Key: $APOLLO_API_KEY_ACCOUNT2" https://api.apollo.io/v1/...

# Use Satlas Instantly API
curl -H "Authorization: Bearer $SATLAS_INSTANTLY_API_KEY" https://api.instantly.ai/api/v1/...

# Use Satlas Porkbun API
curl -X POST "https://porkbun.com/api/json/v3/domain/register" \
  -H "Content-Type: application/json" \
  -d '{"apikey": "'$SATLAS_PORKBUN_API_KEY'", "secretapikey": "your-secret-key", ...}'

# Use Satlas Zapmail API
curl -H "Authorization: Bearer $SATLAS_ZAPMAIL_API_KEY" \
  https://api.zapmail.io/v1/inboxes

# Use Satlas Inboxkit API
curl -H "Authorization: Bearer $SATLAS_INBOXKIT_API_KEY" \
  https://api.inboxkit.io/v1/inboxes

# Use Satlas Plusvibe API
curl -H "X-API-Key: $SATLAS_PLUSVIBE_API_KEY" \
  https://api.plusvibe.io/v1/campaigns

# Use Satlas MillionVerifier API
curl -H "Authorization: Bearer $SATLAS_MILLIONVERIFIER_API_KEY" \
  https://api.millionverifier.io/v1/enrich

# Use Albertscott Smartlead API
curl -H "X-API-Key: $ALBERTSCOTT_SMARTLEAD_API_KEY" \
  https://api.smartlead.io/v1/campaigns

# Use Albertscott Pipedrive API
curl -H "Authorization: Bearer $ALBERTSCOTT_PIPEDRIVE_API_KEY" \
  https://api.pipedrive.com/v1/deals

# Use Albertscott Quickemailver API
curl -H "X-API-Key: $ALBERTSCOTT_QUICKEMAILVER_API_KEY" \
  https://api.quickemailver.com/v1/verify

# Use Fractio Hubspot API
curl -H "Authorization: Bearer $FRACTIO_HUBSPOT_API_KEY" \
  https://api.hubapi.com/crm/v3/objects/contacts
```

### In Claude Code
All variables are available as environment variables and can be used with their respective service integrations and MCP tools.

---

**Last Updated:** August 5, 2026
**Configured in:** ~/.claude/settings.json

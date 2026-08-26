# PlusVibe campaign migration

Builds a drafted campaign into PlusVibe via the API — campaign shell, sequences, settings,
mailboxes, and leads. Written for Cüneyt (SellerVate), but the shape is reusable.

Campaigns are always created **PAUSED**. Nothing sends until it is activated by hand.

## Run

```bash
export PV_KEY=<plusvibe api key>          # never commit this
export PV_WS=6a8c1c4f92e45be273aa9201     # Cüneyt's Workspace
python3 migrate.py
```

Set `PV_CAMPAIGN_ID` to re-apply settings to an existing campaign instead of creating a new one.
Re-running is safe: leads already present come back as `already_in_campaign` rather than duplicating.

## API notes (learned the hard way)

Base `https://api.plusvibe.ai/api/v1`, auth via the `x-api-key` header.

- PlusVibe sits behind Cloudflare, which **403s urllib's default user-agent** (error 1010).
  The script shells out to `curl`.
- `POST campaign/add/campaign` takes only `workspace_id` + `camp_name`. Everything else is a
  follow-up `PATCH campaign/update/campaign`.
- `schedules` is an **array**, not an object.
- `schedules[].days` accepts only the **enabled** days as keys, `1`=Mon..`7`=Sun. A key set to
  `false` is rejected outright (`Day 6 must be true`), and `0` is not a valid key — omit days you
  want off.
- `sequences[].wait_time` means days *after* that step, and must be **≥1** on every step —
  including the last one, where it is unused.
- Custom variables upload under `custom_variables` but are stored and referenced with a
  `custom_` prefix: `product_category` → `{{custom_product_category}}`.
- Standard variables are **snake_case** (`{{first_name}}`, `{{company_name}}`), not camelCase.
- **Only one variable per spintax section.** `{{RANDOM | ...{{a}}...{{b}}... | ...}}` is invalid.
  `sequences.py` asserts against this — keep merge fields outside RANDOM blocks.

Useful reads: `campaign/list?workspace_id=`, `campaign/get/status`, `campaign/get/accounts`,
`lead/get?...&email=`, `account/list?workspace_id=`.

## Reusing for the other lists

`sequences.py` holds Sequence B (product-category), built and live as `Amazon Seller UK/USA
[MIGRATED]` (107 leads). `sequences_rating.py` + `migrate_rating.py` hold Sequence A (rating) and
are already built and live as `Amazon Seller - Rating [MIGRATED FROM INSTANTLY DRAFT]` (2026-08-26)
— pulled straight from the "Amazon Seller" campaign drafted in Instantly rather than the local
markdown draft, so the shipped copy matches what's actually in the client's account. That campaign
now holds all 1,327 leads from the local star-rating database (964 from the Instantly draft +
363 more via `add_leftover_batch.py`, which folds in local leads never uploaded to Instantly at
all — dry-run it against a fresh `amazon_seller_leads_full.json` export before reusing, since the
"already in this campaign" set changes over time).

Neither `amazon_seller_leads_full.json` (the raw Instantly export) nor `leftover_rating_leads.json`
(the normalized local leftover) are committed — both hold lead PII and are regenerated locally by
`migrate_rating.py` / the Instantly pull each time.

## Pulling from Instantly directly (used for the 964-lead rating campaign)

Base `https://api.instantly.ai/api/v2`, auth via `Authorization: Bearer <key>` — the account's key
decodes to a `uuid:secret` pair but the whole base64 string is what goes in the header, not the
decoded parts. `api_key=` query-param auth (the old v1 scheme) 401s; don't bother with it.

- `GET /campaigns?limit=100&starting_after=<cursor>` — list campaigns, paginated.
- `GET /campaigns/{id}` — full detail including `sequences` (steps → variants → subject/body) and
  `custom_variables` (the field names configured for that campaign, e.g. `Rating`, `Product Type`).
- `POST /leads/list` with body `{"campaign": "<id>", "limit": 100, "starting_after": "<cursor>"}` —
  full lead objects, personalization fields live under `payload` (e.g. `payload.Rating`,
  `payload["Product Type"]`, `payload["Amazon URL"]`). `{"filter": {...}}` is NOT the right shape
  for this endpoint (400s) — pass the campaign id as a top-level key.
- `GET /campaigns/analytics?id=<id>` — per-campaign send stats (`emails_sent_count`, `bounced_count`,
  etc.). A draft campaign that's never been launched returns `emails_sent_count: 0` — use this to
  confirm a "drafted, never sent" campaign really has zero send history before treating its leads as
  untouched.
- Campaign `status`: 0=Draft, 1=Active, 2=Paused, 3=Completed, 4=Running Subsequences. The
  lead-level `status` field is a **separate**, undocumented enum — don't assume it maps the same way;
  use `status_summary` (non-empty = has a `lastStep`, i.e. has been sent to before) as the reliable
  signal for "already contacted somewhere," not the raw status code.

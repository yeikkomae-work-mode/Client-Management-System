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

## MillionVerifier + `build_batch2.py` / `verify_batch.py`

Used to migrate the other 24 Instantly campaigns (2026-08-27) — pull → dedupe → verify → revise →
upload. `MV_KEY` (the MillionVerifier key) and `PV_KEY`/`PV_WS` must be set as environment
variables; never hardcode a key directly in a script, even one handed to you inline in a URL by
the user — a hardcoded key like that is exactly what got caught and fixed here.

- `GET /api/v3/?api=<key>&email=<email>&timeout=10` — single lookup, real SMTP handshake for
  valid-looking domains, so ~1-2s per call. `GET /api/v3/credits?api=<key>` — check balance before
  a large run. Same Cloudflare block as PlusVibe/Instantly — shell out to `curl`, don't use
  `requests`/`urllib` directly.
- Response has `quality` (good/risky/bad/unknown — use `quality == "good"` as the pass bar),
  `result`/`resultcode`/`subresult` for the detailed reason, and `credits` (balance after this
  call). `verify_batch.py` parallelizes with a thread pool (`ThreadPoolExecutor`, concurrency 15)
  since sequential calls at ~2s each don't scale past a few hundred leads.
- `build_batch2.py` first collapses near-duplicate Instantly campaigns down to their distinct copy
  (many campaigns in this account reuse an identical sequence under different names/segments —
  hash each sequence's variant bodies to find the real count of unique campaigns before revising
  anything). None of the other 24 campaigns used spintax, so "revising" them was pure mechanical
  variable renaming (`{{firstName}}` → `{{first_name}}`, `{{jobTitle}}` → `{{custom_job_title}}`,
  etc.) plus a targeted brand-name correction on the campaigns that were still signed "Starfix"
  instead of "SellerVate" — not creative rewriting.

## SalesFix brand fix (2026-08-28)

Cüneyt confirmed via WhatsApp: the "SalesFix"-signed campaign (built by `build_salesfix.py` with
`fix_brand=False`, since at build time it wasn't clear whether SalesFix was a real second brand or
a leftover mistake) needed the **same** Starfix→SellerVate correction as every other campaign, and
should stay paused ("dont make it active"). `fix_salesfix_brand.py` PATCHes only the `sequences`
field on the live campaign (`6a9023eb0d0bcf449012149a`) — leads, mailboxes, schedule, and PAUSED
status are untouched. `salesfix_sequences_fixed.json` is the corrected sequence payload it sends
(committed here since it's small and is the definitive record of what shipped, unlike the large raw
pulls elsewhere in this pipeline which are left uncommitted and regenerable).

## Test sends (2026-08-28)

Cüneyt asked (same WhatsApp thread) to check warmup status and send a few test emails. Warmup:
`account/list?workspace_id=` shows all 19 mailboxes `ACTIVE`, warming since 2026-08-24 at a slow
15/day rampup — normal for 4-day-old warmup, not a blocker on its own but worth watching before any
campaign goes live.

Test sends use `POST unibox/emails/send`, which behaves differently from every other endpoint in
this file:
- `workspace_id` must be a **query param** (`?workspace_id=`), not a body field — passing it in the
  body gets back a misleading `"workspace_id" is required` even though the body clearly has it.
- Body requires `subject`, `from` (must be an existing connected mailbox — validated by lookup;
  an unrecognized address returns `Email Account not found`, not a generic validation error), `to`.
  `body` is optional.
- There is no live "fetch full campaign detail" GET endpoint (`campaign/get/campaign`,
  `campaign/get/sequences` etc. all 404) — `send_test_emails.py` renders each campaign's Step 1
  Variant A copy from the same local source data used to build it (`sequences.py`,
  `sequences_rating.py`, `other24_full.json` via `build_batch2.convert_sequences`,
  `salesfix_sequences_fixed.json`), resolving spintax to its first branch and filling merge
  variables with clearly-labeled placeholder values (no real lead was used) plus a `[TEST SEND]`
  banner in the body. One test per campaign (11 total), spread across 11 distinct mailboxes, all
  sent to `cueneyt.nurdogan@sellervate.de`.

## Splitting a campaign by timezone (`split_uk_us.py`, 2026-08-28)

`schedules` accepts **at most one entry** — confirmed via a live 400 (`schedules must contain ≤ 1
items`) when trying to add a second block for a different timezone. A single campaign cannot serve
two timezones; the only way to actually match send time to each lead's region is to split into
separate campaigns, one per region.

- `campaign/update/campaign` rejects `status: "ACTIVE"` in the same call that first attaches
  `email_accounts` to a brand-new campaign (`"Email account must be added before you can start the
  campaign"`) even though the accounts array is right there in the same request body — apply
  settings/sequences/mailboxes/schedule first while still `PAUSED`, upload leads, then send a
  second, separate `PATCH` with just `{"status": "ACTIVE"}`.
- `POST lead/delete` removes leads from one campaign: `{"workspace_id", "campaign_id",
  "delete_list": ["email1@x.com", ...]}` — note the key is `delete_list`, not `emails` (`emails` is
  rejected outright as "not allowed"). Used to move UK leads out of a campaign before re-uploading
  them into a new UK-only one, so nothing gets sent from both.
- Before touching anything live, `split_uk_us.py` reconstructs each campaign's exact lead list from
  the same source files used to originally build it (CSV + dedupe list for the product-category
  campaign; the Instantly export + leftover-batch JSON for the rating campaign) and dry-run-checks
  the country-split counts against the documented live total — both matched exactly (107 = 62 US/CA
  + 45 UK, 1,327 = 936 US/other + 391 UK) before any write happened.
- There is still no bulk "list leads in a campaign" GET endpoint (`lead/list`, `lead/get/all`,
  `campaign/get/leads` all 404) — reconstructing from source, not reading back from PlusVibe, is the
  only option for this kind of split.

## Autonomous writes to live campaigns are not something the session can schedule unsupervised

Tried to set up a daily cron Routine that would both increment a campaign's `daily_limit` (ramp) and
report health — the permission classifier declined it, since it's a standing job that would keep
changing a live client campaign's send volume with no human in the loop. A **read-only** daily
health-check Routine (status/bounce rate/mailbox health, no writes) was approved instead. Any ramp
step that changes `daily_limit` needs to be applied from an active session, not a background cron,
unless the client/user explicitly grants standing write permission for it.

## Splitting further by recipient mail provider (`classify_esp.py` + `split_esp.py`, 2026-08-28)

No PlusVibe field exposes a lead's mail provider — the `provider: "REGULAR_ACCOUNT"` field on
*sending* mailboxes (from `account/list`) is about how that inbox connects to PlusVibe (generic
IMAP/SMTP vs OAuth), not the recipient's ESP. The only way to classify leads by Google vs Microsoft
is an **MX-record lookup per email domain**. This box has no `dig`/`host`/`nslookup`; `pip install
dnspython` and `dns.resolver.resolve(domain, "MX")` works instead. Classification rule: MX host
containing `google.com`/`googlemail.com` → Google, `outlook.com`/`protection.outlook.com` →
Microsoft, anything else (including lookup failures/NXDOMAIN) → Other. Resolve concurrently
(`ThreadPoolExecutor`) — 679 domains took a couple minutes sequential-equivalent, seconds in
parallel.

`split_esp.py` reuses the same "reconstruct from source, don't rely on a bulk-read API" pattern as
`split_uk_us.py` (no `lead/list` endpoint exists), and the same "existing campaign becomes one
bucket, create new campaigns for the rest" approach — rename in place + `lead/delete` the
leads that moved out, rather than deleting and rebuilding the whole campaign.

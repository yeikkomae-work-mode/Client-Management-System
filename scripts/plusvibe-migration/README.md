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

`sequences.py` holds Sequence B (product-category). The two star-rating lists — Amazon USA Product
Review 2nd SMB (613) and Amazon Leads MAIN List (714) — need Sequence A from
`OUTPUT/Campaign Tracking/Cüneyt - SellerVate Revised Sequences (Cleaned Database, 2026-08-21).md`,
with `{{star_rating}}` mapped from the `Rating` column as `{{custom_star_rating}}`. Point
`CSV_PATH` and `CAMP_NAME` in `migrate.py` at the right list.

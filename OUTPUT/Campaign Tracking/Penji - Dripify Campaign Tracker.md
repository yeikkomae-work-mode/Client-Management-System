# Penji — Dripify Campaign Tracker (Amanda Scott / Cristy / Eikko)

**No API access.** Dripify has no working programmatic API — tested three separate keys (Cristy's, Amanda's, Whitney's) across two sessions (2026-09-01, 2026-09-02); all three gave the identical result: `Authorization: Bearer` returns a real "expects OAuth JWT" rejection, `X-API-KEY`/`Api-Key` return a generic 500 on every endpoint tried. This is a platform limitation, not account-specific — see `OUTPUT/End-of-Day Reports/Penji - End of Day Log.md`, 2026-09-01 and 2026-09-02 entries.

**This means tracking here is manual**, same pattern as the tools with no API in `RESOURCES/Tools & API Details/Connected Tools Status.md` (Hubspot/Lemlist/LinkedIn for Chris Caffera). Update this table from whatever Eikko can report — a dashboard screenshot, an export, or numbers read off Dripify directly. I'll log and maintain it; I can't pull it myself.

---

## Status by account

| Account | Leads loaded | Campaign launched? | Connections sent | Accepted | Replies | Meetings | Last updated |
|---|---|---|---|---|---|---|---|
| **Amanda Scott** (`amanda@trypenji.co`) | 131 (CSV sent 2026-09-02) | **Unconfirmed** — CSV was sent for manual import, launch not yet confirmed back | — | — | — | — | 2026-09-02 |
| **Cristy** (Cristy Jane Muñosco) | 62 clean + up to 80 in-flight from the old HeyReach campaign (see note below) | **Unconfirmed** — CSV of the 62 untouched leads sent 2026-09-01, import not yet confirmed | — | — | 3 replies were sitting unanswered as of 2026-09-01 (Christopher Campbell, Maxwell Veitch, Eric Hoffman) — status since unknown | — | 2026-09-01 |
| **Eikko** (personal LinkedIn) | — | **Unknown — see open question below** | — | — | — | — | — |

*(Whitney Cole also received a CSV — 130 leads, 2026-09-02 — not asked about in this task but tracked here for completeness since she's part of the same rollout.)*

---

## Open questions before this can be a real tracker

1. **Did the Amanda Scott and Cristy CSV imports actually happen, and were campaigns launched?** I prepared the data; I have no visibility into whether either was imported or started.
2. **Is Eikko's own Dripify seat active?** Last known status (2026-08-25 EOD entry): billing/card not set up, unresolved, outreach running manually on personal LinkedIn in the meantime. If that's since been fixed, what's the account and is a campaign running on it?
3. **Cristy's old HeyReach leads** — the 67 "connection sent, no accept" and 6 "accepted" leads from the dead HeyReach campaign were left alone pending a decision (2026-09-01 entry). Did those get resolved, folded into the new Dripify campaign, or left as-is?
4. **What cadence and what numbers matter?** Connections sent/accepted/replies/meetings is my best guess at what's worth tracking (matches the columns on Penji's own Signal Tracker in Notion) — confirm or adjust.

---

**Last updated:** 2026-09-02

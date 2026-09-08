# Penji — Dripify Campaign Tracker (Amanda Scott / Cristy / Eikko)

**Correction, 2026-09-02:** the "no working API" conclusion below (and in the 2026-09-01/2026-09-02 EOD entries) was wrong. Dripify's real public API is `https://api.dripify.com/v1/open-api` with an `X-Api-Key` header — a different host and path from what was tested. This was live-verified against all four accounts (Amanda, Cristy, Whitney, Eikko) on 2026-09-02; see `RESOURCES/Tools & API Details/scripts/dripify_stats.py` and `RESOURCES/Tools & API Details/OAuth Credentials/dripify-api-keys-credentials.json`. Numbers below are pulled live from that API, not manually reported.

~~**No API access.** Dripify has no working programmatic API...~~ *(superseded — kept struck through rather than deleted so the record of what was tried is preserved)*

---

## Status by account — live from Dripify Open API, 2026-09-02

| Account | Campaign | Status | Total leads | Contacted | Accepted | Acceptance rate | Replies | Reply rate | Failed |
|---|---|---|---|---|---|---|---|---|---|
| **Amanda Scott** (`amanda@trypenji.co`) | Gojiberry -Agency (id 2064895) | ACTIVE | 75 | 5 | 0 | 0.0% | 0 | 0.0% | 0 |
| **Cristy** | Gojiberry - Agency (id 2064892) | ACTIVE | 100 | 5 | 0 | 0.0% | 0 | 0.0% | 9 |
| **Whitney Cole** | — | no campaign | — | — | — | — | — | — | — |
| **Eikko** (personal LinkedIn) | Gojiberry Marketing (id 2044911) | ACTIVE | 322 | 149 | 28 | 18.8% | 4 | 2.7% | 4 |

All four campaigns are live and running. Amanda's and Cristy's are both brand-new (created 2026-09-02) with most leads still queued (`gettingReady`/`uploading`) — too early for acceptance/reply data. Eikko's campaign has been running since 2026-08-17 and has real traction: 28 accepted connections, 4 replies.

Lead-list totals (75 for Amanda, 100 for Cristy) are higher than the CSVs originally sent (Amanda's half-split CSV, Cristy's 62-lead CSV) — Dripify may be counting from a combined/pre-existing list rather than only the import. Not yet investigated; flagging for Eikko to confirm against what's actually loaded per campaign.

---

## Open questions

1. **Amanda's and Cristy's lead-list counts are higher than the CSVs sent.** Amanda's list shows 75 (CSV was ~half of 130-ish split); Cristy's shows 100 (CSV was 62 clean leads). Possible causes: combined with an existing list, duplicate imports, or a list that includes leads beyond what was exported. Needs Eikko to confirm what's actually in each Dripify list.
2. **Whitney Cole's account has zero campaigns** despite the API key authenticating successfully. Either no campaign has been launched yet, or the key belongs to a separate/unlinked Dripify org from the one with the imported leads. Needs confirmation from Whitney or Eikko.
3. **Cristy's old HeyReach leads** — the 67 "connection sent, no accept" and 6 "accepted" leads from the dead HeyReach campaign (flagged 2026-09-01) — status still unresolved; not visible via the Dripify API since that's a different platform.
4. **Refresh cadence** — this table is now pulled live via `dripify_stats.py`; re-run it and update this table whenever an updated read is needed rather than waiting on manual reports.

---

## Update — 2026-09-07: Amanda's account retired; Gojiberry leads moved to Cristy via API

- Amanda Scott's LinkedIn was restricted, so her Dripify account is no longer in use. Per Eikko, Cristy's account is now the destination for the Agency-Eikko leads.
- Cross-referenced Cristy's existing campaign leads (131 in list "Gojiberry", id 3353134) against the full Gojiberry export of list "Agency - Eikko leads" (499 contacts, see `Penji - Agency-Eikko Gojiberry Leads Export (2026-09-07).xlsx`). Match key: LinkedIn public ID / profile slug.
  - 126 of Cristy's 131 leads are the 2026-09-02 "Amanda Scott" import batch — that CSV had already been loaded into Cristy's account.
  - 5 of Cristy's leads are not in the Gojiberry export at all (HeyReach leftovers).
- **Uploaded 239 leads to Cristy's campaign 2064892 via `POST /campaigns/{id}/leads`** — new lead list "Gojiberry - Agency-Eikko export 2026-09-07" (id 3362829): 239 accepted, 0 duplicates. Record of exactly what was sent: `Agency-Eikko Leads - Uploaded to Cristy Dripify via API (2026-09-07).csv`. Breakdown: 234 new Gojiberry leads found after 09-02, plus 5 from the Amanda 09-02 batch that had not made it into Cristy's list.
- **Held back, not uploaded:** the 130 leads in the 2026-09-02 "Whitney Cole" import batch (assumed to be Whitney's to work — Eikko to confirm; Whitney's account still shows no campaign), and 4 Gojiberry contacts whose first+last name already exists in Cristy's list under a different LinkedIn URL (Marc Mintle, Rene W., Tim Souers, Santiago Faus) — probable duplicates.
- The Open API upload endpoint takes `{"name": <list name>, "leads": [{"linkedinUrl": ...}]}` (1–1000 per request) and returns accepted/duplicate counts; documented at https://api.dripify.com/ (Redoc).

## Update — 2026-09-08: Whitney's batch also moved to Cristy

- Eikko confirmed Whitney Cole's account will not be used for outreach — her LinkedIn still needs to reach 100+ connections first. Her Dripify shows no campaign.
- Uploaded the 130 leads from the 2026-09-02 "Whitney Cole" import batch to Cristy's campaign 2064892 via the Open API — new lead list "Gojiberry - Agency-Eikko (ex-Whitney batch) 2026-09-08" (id 3363938): 130 accepted, 0 duplicates. Record: `Agency-Eikko Leads - Uploaded to Cristy Dripify via API - Whitney batch (2026-09-08).csv`.
- Cristy's campaign now has 3 lead lists (131 + 239 + 130). Both API-uploaded lists still show `READY_FOR_SEARCH` and 369 leads in `uploading`; totalLeads still reports 131 until Dripify finishes collecting them. Watch the daily sync — if `uploading` has not dropped by 2026-09-09, open the campaign in Dripify and check the lists are being processed.
- Still not in Cristy: the 4 probable name duplicates (Marc Mintle, Rene W., Tim Souers, Santiago Faus). Only Amanda's now-retired 100-lead campaign and Eikko's own campaign remain elsewhere.

**Last updated:** 2026-09-08 (live API data)



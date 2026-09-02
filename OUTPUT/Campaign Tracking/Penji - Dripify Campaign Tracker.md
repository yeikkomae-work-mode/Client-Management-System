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

**Last updated:** 2026-09-02 (live API data)

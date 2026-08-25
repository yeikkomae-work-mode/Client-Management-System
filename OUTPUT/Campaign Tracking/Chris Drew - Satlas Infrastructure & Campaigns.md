# Chris Drew (Satlas) — Infrastructure & Campaign Tracking

**Client:** Chris Drew  
**Account:** eikko@satlas.com.au  
**Infrastructure Type:** Email infrastructure + Outbound campaigns  
**Status:** 🟢 ACTIVE & MONITORED  

---

## INFRASTRUCTURE OVERVIEW

### Domain Portfolio (Porkbun Managed)
| Component | Count | Status |
|-----------|-------|--------|
| **Total Domains** | 25 | ✅ Active (registered) |
| **Total Mailboxes** | 60 | 🟡 Active but not all healthy — see below |
| **Email Accounts** | 180+ | ✅ Active |
| **Average Domain Health** | 22.65/100 (Zapmail, 10 domains) · 100/100 (InboxKit, 15 domains) | 🔴 Zapmail batch is degraded, InboxKit batch is healthy — corrected 2026-08-22 |

### Batch 1 — Zapmail Infrastructure
- **Domains:** 10
- **Mailboxes:** 30 (3 per domain)
- **Purchase Date:** May 2026
- **Expiration:** 2027-05-14 (281 days remaining)
- **Health Score:** 🔴 22.65/100 — corrected 2026-08-22 via live Zapmail API (`get_domain_health_score`), sampled 3 of 10 domains, all identical. Previous "87/100" figure was stale/wrong — never re-verified since the original deliverability incident.
- **Warmup:** All 30 mailboxes show `isWarmedUp: false` as of 2026-08-22 — none of this infrastructure is warm.
- **Status:** 🔴 Not sending-safe. All-Active status in Zapmail's dashboard is misleading — "active" just means not suspended, not that it's healthy. Decide whether to release these domains or attempt recovery; don't launch from them as-is.

**Domain List:**
1. trysatlas.com
2. satlastry.com
3. gosatlas.com
4. satlasgo.com
5. satlaswork.com
6. partnersatlas.com
7. satlaspartner.com
8. discoversatlas.com
9. satlasdiscover.com
10. satlasworks.com

### Batch 2 — InboxKit Infrastructure
- **Total Domains:** 15 (10 with mailboxes + 5 unprovisioned)
- **Active Mailboxes:** 30 (3 per domain), all `status: active` per InboxKit API
- **Backup Capacity:** 5 domains (unprovisioned, 0 mailboxes)
- **Purchase Date:** July 2026
- **Expiration:** 2027-07-07 (336 days remaining)
- **Health Score:** 100/100 (InboxKit domains, unlike Zapmail's, are genuinely healthy — verified 2026-08-22)
- **Status:** 🟢 Active
- **Correction 2026-08-22:** the domain lists below were swapped in a previous version of this doc (e.g. hellosatlas.com and satlasway.com were listed as "active" when they actually have 0 mailboxes). Corrected via live `domains/list` + `mailboxes/list` pull.

**Domains with mailboxes assigned (10, 3 each = 30 total):**
1. satlasedge.com
2. satlaszone.com
3. withsatlas.com
4. satlasplus.com
5. satlasrise.com
6. satlasready.com
7. satlashq.com
8. satlasbase.com
9. satlasmail.com
10. satlaslink.com

**Unprovisioned domains (5, 0 mailboxes):**
- hellosatlas.com
- satlashub.com
- usesatlas.com
- satlasway.com
- satlascore.com

---

## CAMPAIGN MONITORING DASHBOARD

### Active Campaigns (Plusvibe) — Updated August 12, 2026 (live pull via Satlas Chrome session)

*Per-campaign metrics below are the Aug 12 pull and have not been refreshed since. Account-level metrics were re-pulled Aug 22 — see Email Health Tracking.*

| Campaign | Status | Leads | Contacted | Replied | Positive Reply | Bounced |
|----------|--------|-------|-----------|---------|-----------------|---------|
| Mortgage Brokers - Catchall | 🟢 ACTIVE | 109 | 70.6% | 0% | 0% | 23.5% |
| Mortgage Brokers - Googles, Microsoft & Others | 🟢 ACTIVE | 459 | 21.4% | 3.1% | 0% | 7.1% |
| Financial Planner - Catchall | 🟢 ACTIVE | 291 | 27.1% | 1.3% | 100% | 9% |
| Financial Planner - Microsoft | 🟢 ACTIVE | 2677 | 2.9% | 0% | 0% | 1% |
| Commercial Real Estate - Catchall | 🟢 ACTIVE | 73 | 15.1% | 0% | 0% | 5% |
| Commercial Real Estate - Microsoft | 🟢 ACTIVE | 1170 | 7% | 0% | 0% | 2.3% |
| Commercial Real Estate - Google & Others | 🟢 ACTIVE | 225 | 32% | 1.4% | 100% | 10.7% |
| Hillary — Finance Broker | 🟡 DRAFT | 0 | - | - | - | - |
| Referral Finance Campaign | 🟡 DRAFT | 0 | - | - | - | - |
| Capital Financing - Trades | 🟡 DRAFT | 0 | - | - | - | - |
| Capital Financing - Logistics | 🟡 DRAFT | 0 | - | - | - | - |
| Capital Financing - Labour Hire | 🟡 DRAFT | 0 | - | - | - | - |

*Historical Instantly campaigns (Commercial Real Estate - ESG, Financial Planner - ESG, all 4 Finance Brokers segments) are completed and archived — see the Instantly Campaign Analytics Report for their final numbers.*

### Current Performance Metrics
- **Plusvibe Total Campaigns:** 13 as of Aug 12 (excludes internal "test duplicate") — ⚠️ the 2026-08-22 API pull returned **17** campaigns. The extra 4 have not been identified in this doc; reconcile the campaign table against a fresh pull before treating it as complete.
- **Account-wide (Aug 12):** 5,005 total leads · 498 contacted · 1.2% replied · 50% positive reply rate · 0.8% bounced
- **Capital Financing (new client, Rohan Burgess):** 3 campaign shells built, Apollo lists built for all 3 segments, Trades sequence built in Plusvibe (needs a subject-line format fix — see EOD log 2026-08-12), Logistics/Labour Hire sequences not yet built
- **Workspace:** Eikko's Workspace (browser: "Satlas" profile, deviceId db5bac87)

### ⚠️ Live tracker connector note (added 2026-08-12)
The Plusvibe MCP/API connector available in Claude tool calls is authenticated to a **different, unrelated account** (mailboxes under "Yoni Lebovits" on albertscott*.com domains) — not Satlas. Do not trust any Plusvibe numbers pulled via that connector until it's reauthorized with the Satlas login (eikko@satlas.com.au). All figures in this doc were pulled manually via the "Satlas" Chrome browser session instead.

### Live trackers for the team
- **Satlas Campaign Tracker (Google Sheet):** shared with Ally (ally@satlas.com.au) as Editor — manually refreshed on request, intended to be pinned in Notion
- **Cowork artifacts:** Plusvibe campaign tracker + inbox & replies tracker, built 2026-08-12 (manual refresh until the connector issue above is fixed)
- Ally has a setup prompt (`Ally-Plusvibe-Artifact-Prompt.md`) to build her own live-refreshing artifacts once she connects her own Plusvibe MCP with the correct login

### Email Health Tracking — 2026-08-22 (live API pull, current)
| Platform | Domains | Mailboxes | Health | Status |
|----------|---------|-----------|--------|--------|
| **Zapmail** | 10 | 30 (0 warmed up) | 22.65/100 | 🔴 Not sending-safe |
| **InboxKit** | 10 provisioned + 5 empty | 30 active (15 Google / 15 M365) | 100/100 | 🟢 Optimal |
| **Plusvibe** | 20 | 60 | 0 errors / 0 alerts | 🟡 6 mailboxes bouncing >5%, 2 below 90% warmup |

**Plusvibe status (2026-08-22):** 60/60 active · 60/60 warmup running · 30-day reply rate 0.66% (17/2,588) · 30-day bounce 1.28% · worst mailbox tremaynec@satlasmail.com at 20% bounce.

<details>
<summary>Superseded — Email Health Tracking 2026-08-06 (automated snapshot)</summary>

| Platform | Domains | Mailboxes | Health | Status |
|----------|---------|-----------|--------|--------|
| **Zapmail** | 10 | 30 | 87/100 | 🟢 Good |
| **InboxKit** | 10 active + 5 backup | 30 active | 100/100 | 🟢 Optimal |
| **Plusvibe** | 20 | 60 | ✅ All Active | 🟢 Healthy |

Plusvibe Daily Status (Aug 6, 9:00 AM PHT): 60/60 active, 0 errors, 0 alerts, 60/60 warming, 🟢 HEALTHY.
**The Zapmail 87/100 figure here was never re-verified after the July deliverability incident and is now known to be wrong — see the Aug 22 table above.**

</details>

---

## DAILY MONITORING CHECKLIST

### 🤖 AUTOMATED MONITORING (9:05 AM Daily) — ⚠️ NOT ACTUALLY RUNNING
**Task:** `plusvibe-daily-mailbox-monitor`
**Reality check 2026-08-24:** the daily monitor file only contains snapshots for Aug 5, Aug 6 and Aug 22, and the Aug 22 entry is labelled "Manual check via API — Eikko". Whatever scheduled task this section describes has not produced a daily entry in over two weeks. Either re-create the scheduled task or drop the "automated" framing and treat this as a manual daily check.
- Threshold logic still valid: 98%+ utilization, error/alert count 0, bounce >5%, deliverability <95%

**See:** `PLUSVIBE MONITORING SETUP.md` for full details

### Zapmail (app.zapmail.ai)
- [ ] Domain health score (target: 85+)
- [ ] Nameserver status (all connected)
- [ ] Export integrations active (Slack, Pinterest)
- [ ] Mailbox utilization (30 in use)
- [ ] Any delivery issues or warnings

### InboxKit (app.inboxkit.com)
- [ ] Domain health status (target: 100)
- [ ] Mailbox warmup percentage
- [ ] Active mailbox count (30)
- [ ] Backup domains ready for expansion
- [ ] Warmup email send/reply activity

### Plusvibe (app.plusvibe.ai/v2/email-accounts)
**Automated via scheduled task - See "PLUSVIBE MONITORING SETUP.md"**
- [✅] Mailbox count (60 total) — checked daily
- [✅] Error count (target: 0) — checked daily
- [✅] Alert count (target: 0) — checked daily
- [✅] Utilization levels (alert at 98%+) — checked daily
- [✅] Campaign status (draft/active/completed) — manual weekly

---

## WEEKLY CAMPAIGN CHECK-IN

**Template for Wednesday end-of-week report:**

```
SATLAS INFRASTRUCTURE — Week of [DATE]

DOMAIN & MAILBOX STATUS:
- Zapmail Health: [Score]/100
- InboxKit Health: [Score]/100
- Total Active Domains: 20/25
- Total Active Mailboxes: 60/60

EMAIL PERFORMANCE:
- Opens (this week): [Count]
- Replies (this week): [Count]
- Bounce Rate: [%]
- Average Response Time: [Hours]

CAMPAIGN STATUS:
- Active Campaigns: [Count]
- Leads in Pipeline: [Count]
- Best Performing Campaign: [Name] ([%] reply rate)

NEXT WEEK PRIORITIES:
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]

NOTES:
- [Any issues, blockers, or wins]
```

---

## RENEWAL & MAINTENANCE CALENDAR

| Date | Event | Action | Owner |
|------|-------|--------|-------|
| 2026-08-05 | Infrastructure documented | ✅ COMPLETE | Eikko |
| 2027-05-14 | Batch 1 renewal due | Renew 10 domains | Tremayne |
| 2027-07-07 | Batch 2 renewal due | Renew 15 domains | Tremayne |

---

## DOCUMENTATION & REFERENCES

**Complete Infrastructure Files:**
- `/DOMAIN_INVENTORY.md` — Full domain list with dates and configuration
- `/CLIENT_PROFILE_Chris_Drew_Satlas.md` — Client profile with infrastructure details
- `/EIKKO_MEMORY.md` — Quick reference memory system
- `/CLAUDE.md` — Client Management System overview

**Direct Access:**
- **Zapmail Dashboard:** app.zapmail.ai
- **InboxKit Dashboard:** app.inboxkit.com
- **Plusvibe Campaigns:** app.plusvibe.ai/v2/campaigns/
- **Domain Management:** Porkbun (Satlas account)

---

## CAMPAIGN MIGRATION STATUS — ✅ CLOSED 2026-08-10

The Instantly → Plusvibe migration is **complete**. Campaigns launched 2026-08-10; Instantly is deprecated and its API key is dead. Two campaigns were deliberately held back and remain in draft: **Hillary — Finance Broker** and **Referral Finance Campaign** (reason/timeline still to confirm with Chris).

### Phase 1: Campaign Shell Creation ✅ COMPLETE (Aug 5)
Hillary — Finance Broker · Mortgage Brokers · Referral Finance Campaign

### Phase 2: Sequence Configuration ✅ COMPLETE (Aug 6–7)

### Phase 3: Lead Import & Launch ✅ COMPLETE (Aug 10)
All migrated campaigns live except the two held-back drafts above.

### Campaign Inventory Update
- **Before Migration (Aug 5 AM):** 6 campaigns
- **After Phase 1 (Aug 5 PM):** 9 campaigns
- **New Campaigns:** 3 draft campaigns from Instantly
- **Status:** All shells created, sequences pending

---

## QUICK STATUS SNAPSHOT

```
DATE: 2026-08-22 (Infra audit)
STATUS: 🟡 Satlas campaigns live but underperforming | 🔴 Zapmail batch not sending-safe | 🟡 Capital Financing mid-build

✅ 25 Porkbun domains accounted for; 60 mailboxes provisioned; PlusVibe 0 errors / 0 alerts
✅ 7 Satlas campaigns live (Mortgage Brokers x2, Financial Planner x2, Commercial Real Estate x3)
✅ Instantly → PlusVibe migration closed (launched Aug 10)
✅ Zapmail, InboxKit and Porkbun connectors all reconnected and verified live (Aug 22)
✅ Satlas Campaign Tracker (Google Sheet) shared with Ally as single source of truth
🟡 30-day reply rate 0.66% vs 2% target — copy/targeting review needed, not just infra
🟡 6 mailboxes bouncing >5% (tremaynec@satlasmail.com worst at 20%); 2 below 90% warmup health
🟡 Capital Financing — Logistics & Labour Hire sequences still unbuilt; Trades subject lines need the v3 fix
🟡 Ally's 2 new audiences (~47K net new) exceed available capacity — estimates need rerunning now that Zapmail is known-bad
🔴 Zapmail: 22.65/100 domain health, 0/30 warmed up, CloudNS SURBL unresolved — Chris to decide release vs recover
🔴 PlusVibe MCP/native connector still on the wrong account (Yoni Lebovits / Albert Scott) — use the raw API key instead

NEXT REVIEW: Next session — Zapmail decision, high-bounce mailbox triage, Capital Financing sequences
```

---

**Last Updated:** 2026-08-24 (reconciled with EOD log + Aug 22 infra audit)  
**Created by:** Eikko (kept in sync by Claude each session)  
**Next Review:** Next working session

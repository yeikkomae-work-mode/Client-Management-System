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
| **Total Domains** | 25 | ✅ Active |
| **Total Mailboxes** | 60 | ✅ Active |
| **Email Accounts** | 180+ | ✅ Active |
| **Average Domain Health** | 87-100/100 | ✅ Optimal |

### Batch 1 — Zapmail Infrastructure
- **Domains:** 10
- **Mailboxes:** 30 (3 per domain)
- **Purchase Date:** May 2026
- **Expiration:** 2027-05-14 (281 days remaining)
- **Health Score:** 87/100
- **Status:** 🟢 Active

**Domain List:**
1. trysatlas.com
2. satlastry.com
3. gosatlas.com
4. satlasgo.com
5. satlaswork.com
6. partnersatlas.com
7. satlaspartner.com
8. discoversatlas.com
9. satlasdi**scover.com
10. satlasworks.com

### Batch 2 — InboxKit Infrastructure
- **Total Domains:** 15 (10 active + 5 backup)
- **Active Mailboxes:** 30 (3 per domain)
- **Backup Capacity:** 5 domains (unprovisioned)
- **Purchase Date:** July 2026
- **Expiration:** 2027-07-07 (336 days remaining)
- **Health Score:** 100/100
- **Status:** 🟢 Active

**Active Domains (10):**
1. hellosatlas.com
2. usesatlas.com
3. satlasready.com
4. satlasriq.com
5. withsatlas.com
6. satlasplus.com
7. satlasway.com
8. satlasedge.com
9. satlasbase.com
10. satlascore.com

**Backup Domains (5):**
- satlasmail.com
- satlaslink.com
- satlasrise.com
- satlashub.com
- satlaszone.com

---

## CAMPAIGN MONITORING DASHBOARD

### Active Campaigns (Plusvibe) — Updated August 12, 2026 (live pull via Satlas Chrome session)
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
- **Plusvibe Total Campaigns:** 13 (excludes internal "test duplicate")
- **Account-wide (Aug 12):** 5,005 total leads · 498 contacted · 1.2% replied · 50% positive reply rate · 0.8% bounced
- **Capital Financing (new client, Rohan Burgess):** 3 campaign shells built, Apollo lists built for all 3 segments, Trades sequence built in Plusvibe (needs a subject-line format fix — see EOD log 2026-08-12), Logistics/Labour Hire sequences not yet built
- **Workspace:** Eikko's Workspace (browser: "Satlas" profile, deviceId db5bac87)

### ⚠️ Live tracker connector note (added 2026-08-12)
The Plusvibe MCP/API connector available in Claude tool calls is authenticated to a **different, unrelated account** (mailboxes under "Yoni Lebovits" on albertscott*.com domains) — not Satlas. Do not trust any Plusvibe numbers pulled via that connector until it's reauthorized with the Satlas login (eikko@satlas.com.au). All figures in this doc were pulled manually via the "Satlas" Chrome browser session instead.

### Live trackers for the team
- **Satlas Campaign Tracker (Google Sheet):** shared with Ally (ally@satlas.com.au) as Editor — manually refreshed on request, intended to be pinned in Notion
- **Cowork artifacts:** Plusvibe campaign tracker + inbox & replies tracker, built 2026-08-12 (manual refresh until the connector issue above is fixed)
- Ally has a setup prompt (`Ally-Plusvibe-Artifact-Prompt.md`) to build her own live-refreshing artifacts once she connects her own Plusvibe MCP with the correct login

### Email Health Tracking — 2026-08-06 (Automated)
| Platform | Domains | Mailboxes | Health | Status |
|----------|---------|-----------|--------|--------|
| **Zapmail** | 10 | 30 | 87/100 | 🟢 Good |
| **InboxKit** | 10 active + 5 backup | 30 active | 100/100 | 🟢 Optimal |
| **Plusvibe** | 20 | 60 | ✅ All Active | 🟢 Healthy |

**Plusvibe Daily Status (Aug 6, 9:00 AM PHT):**
- Total Active Accounts: 60/60 ✅
- Error Count: 0 ✅
- Alert Count: 0 ✅
- Warmup Running: 60/60 ✅
- Overall Status: 🟢 HEALTHY

---

## DAILY MONITORING CHECKLIST

### 🤖 AUTOMATED MONITORING (9:05 AM Daily)
**Task:** `plusvibe-daily-mailbox-monitor` (Runs automatically)
- ✅ Plusvibe mailbox health checked daily
- ✅ 98%+ utilization alert threshold active
- ✅ Error/Alert count monitored (target: 0)
- ✅ All tracking files updated automatically
- ✅ Critical issues trigger immediate notification

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

## CAMPAIGN MIGRATION STATUS (Updated Aug 5, 2026)

### Phase 1: Campaign Shell Creation ✅ COMPLETE
- **Date Completed:** August 5, 2026
- **Campaigns Created:** 3
  - Hillary — Finance Broker
  - Mortgage Brokers  
  - Referral Finance Campaign
- **Status:** Ready for sequence configuration

### Phase 2: Sequence Configuration 🟡 IN PROGRESS
- **Timeline:** Aug 6-7, 2026
- **Tasks:**
  - [ ] Hillary — Finance Broker: Add 4 steps with variations
  - [ ] Mortgage Brokers: Add 3 steps with variations
  - [ ] Referral Finance Campaign: Add 2 steps with variations

### Phase 3: Lead Import ⏳ PENDING
- **Timeline:** Aug 8, 2026
- **Status:** Awaiting CSV exports from Instantly

### Campaign Inventory Update
- **Before Migration (Aug 5 AM):** 6 campaigns
- **After Phase 1 (Aug 5 PM):** 9 campaigns
- **New Campaigns:** 3 draft campaigns from Instantly
- **Status:** All shells created, sequences pending

---

## QUICK STATUS SNAPSHOT

```
DATE: 2026-08-12 (Evening Update)
STATUS: 🟢 Satlas campaigns healthy | 🟡 Capital Financing mid-build | 🔴 Plusvibe MCP connector on wrong account

✅ 25 domains active & managed, 60/60 mailboxes active, 20 domains, 0 errors/alerts
✅ 7 Satlas campaigns live (Mortgage Brokers x2, Financial Planner x2, Commercial Real Estate x3)
✅ Capital Financing onboarded — 3 Apollo lists built, 3 Plusvibe campaign shells created, Trades sequence built
✅ Satlas Campaign Tracker (Google Sheet) shared with Ally as single source of truth
✅ Two Cowork artifacts live for campaign + inbox/reply tracking (manual refresh)
🟡 Capital Financing - Logistics & Labour Hire sequences still need building
🟡 Trades sequence subject-line format needs a fix pass to match the v3 doc
🔴 Plusvibe MCP connector authenticated to wrong account (Yoni Lebovits/Albert Scott) — needs reauthorization before any live auto-refresh is possible

NEXT REVIEW: Next session — finish Capital Financing sequences, fix Trades subject lines, reconnect Plusvibe MCP
```

---

**Last Updated:** 2026-08-12  
**Created by:** Eikko (kept in sync by Claude each session)  
**Next Review:** Next working session

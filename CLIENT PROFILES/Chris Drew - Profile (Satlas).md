# Chris Drew (Satlas) — Client Profile

**Status:** Active | **Rate:** $200 AUD/month | **Hours:** Variable (1pm-4pm PHT) | **Role:** Lead Generation & Outreach Specialist
**Coverage Period:** February 2026 – Present | **Last Updated:** 2026-08-24 (reconciled against EOD log + infra audit through 2026-08-22)

---

## Contact Details
- **Email:** (TBD) — working account used on Satlas's behalf: eikko@satlas.com.au
- **WhatsApp:** (TBD — group chat)
- **Company:** Satlas
- **Website:** https://satlas.com.au/
- **Industry:** Lead Generation & Cold Email Outreach Services
- **Timezone:** (TBD — Sydney, AEST/AEDT assumed)
- **Meetings:** As-needed (urgent only)

### Others in the account
- **Ally (ally@satlas.com.au)** — Satlas side; owns audience/targeting requests, holds Editor access on the Satlas Campaign Tracker sheet, drives the Capital Financing engagement
- **Tremayne Chivers** — registered owner of all 25 Porkbun domains and all 60 mailboxes; renewals sit with him
- **Spencer Hirst** — copy + capacity framework owner; reviews new segment copy with Chris before launch
- **Rohan Burgess (Capital Financing)** — Satlas's own client, onboarded via Ally 2026-08-11 (see below)

---

## Role & Responsibilities

1. **Email Infrastructure Management** — oversee domain purchasing and inbox provisioning across providers
2. **Campaign Migration** — lead transition from Instantly (legacy) to Plusvibe (current)
3. **Inbox Health Monitoring** — track domain/inbox health metrics across all providers, 60 mailboxes daily
4. **Warmup Management** — monitor email warmup % to protect deliverability
5. **List Building & Validation** — build and validate lead lists for cold email campaigns
6. **Campaign Optimization** — monitor performance, test copy, refresh sequences, handle replies
7. **Deliverability Oversight** — monthly deliverability checks and domain/inbox health audits

---

## Current Status (as of 2026-08-22 infra audit — most recent verified pull)

**Infrastructure:** 25 Porkbun domains, 60 mailboxes — but only the 30 InboxKit mailboxes are sending-safe. The 30 Zapmail mailboxes are degraded (see below).

**Instantly → Plusvibe migration: ✅ COMPLETE.** Campaigns launched 2026-08-10. Instantly is deprecated and its API key is dead — treat it as archive only.

**Live Satlas campaigns (7, verified Aug 12):**

| Campaign | Leads | Contacted | Replied | Bounced |
|---|---|---|---|---|
| Mortgage Brokers - Catchall | 109 | 70.6% | 0% | 23.5% |
| Mortgage Brokers - Google/Microsoft & Others | 459 | 21.4% | 3.1% | 7.1% |
| Financial Planner - Catchall | 291 | 27.1% | 1.3% | 9% |
| Financial Planner - Microsoft | 2,677 | 2.9% | 0% | 1% |
| Commercial Real Estate - Catchall | 73 | 15.1% | 0% | 5% |
| Commercial Real Estate - Microsoft | 1,170 | 7% | 0% | 2.3% |
| Commercial Real Estate - Google & Others | 225 | 32% | 1.4% | 10.7% |

**Still in draft (not launched):** Hillary — Finance Broker, Referral Finance Campaign (both deliberately held back Aug 10, reason/timeline still TBD with Chris), plus 3 Capital Financing shells.

**Account-wide:** 5,005 leads loaded · 662 contacted (Aug 13) · 30-day reply rate **0.66%** (17 replies / 2,588 sent) — below the 2% target · 30-day bounce 1.28%. Remaining runway on current 30-mailbox capacity ≈ 43 business days (~2 months).

**🔴 Open issues carried into this update:**
1. **Zapmail batch is not sending-safe** — domain health 22.65/100, `isWarmedUp: false` on all 30 mailboxes, CloudNS SURBL issue unresolved. Open decision for Chris: release the 10 domains or attempt recovery. Do **not** launch from them as-is.
2. **6 PlusVibe mailboxes bouncing >5%** — worst is tremaynec@satlasmail.com at 20%. Pause or investigate.
3. **2 mailboxes below 90% warmup health** — tremayne.c@satlaszone.com (83.3%), tremayne.c@satlasplus.com (89.3%).
4. **0.66% reply rate** is a copy/targeting problem, not just infra — worth a review pass.
5. **Ally's two new audiences** (~47K net new) don't fit current capacity — see Capacity Reality Check below.

**Key notes:**
- No automated logging tool — manual EOD logging required
- PlusVibe inbox health is the critical daily metric; monitor for >98% utilization, errors, alerts
- APIs: PlusVibe ✅ (raw key `SATLAS_PLUSVIBE_API_KEY`, workspace `6a5f60452fd3fe45b2605b48`) · Apollo ✅ (`APOLLO_API_KEY`) · Zapmail ✅ (reconnected 2026-08-22) · InboxKit ✅ (2026-08-22) · Porkbun ✅ ("claudeee" key pair, 2026-08-22) · Instantly ⚫ dead
- ⚠️ The **native/MCP PlusVibe connector** is authenticated to an unrelated account (Yoni Lebovits / albertscott*.com — that's the Albert Scott Smartlead client). Never trust PlusVibe numbers from that connector for Satlas.

---

## Capital Financing (Satlas's client — Rohan Burgess)

Onboarded 2026-08-11 from Ally's kickoff. Satlas white-labels the outreach; Eikko builds it.
- **Segments:** Trades (250 prospects), Logistics, Labour Hire — Apollo lists built for all 3
- **Plusvibe:** 3 campaign shells created; **Trades sequence built**, Logistics + Labour Hire have no content yet
- 🟡 Trades sequence still uses the old subject-line format (time-greeting in the subject) instead of the corrected v3 format (short spintaxed subject, greeting in the body) — needs a fix pass
- **Reference copy:** `OUTPUT/Campaign Tracking/Capital Financing/Capital-Financing-Cold-Email-Sequence-v3.docx` (v1/v2 superseded)

---

## Capacity Reality Check (2026-08-13) — Ally's two new audiences

Two Apollo searches saved in Chris's account:
- **AU - Commercial & Asset Finance Brokers (Ally Targeting)** — 41.9K total / **36.3K net new**
- **AU - Specialist Mortgage & Investment Brokers (Ally Targeting)** — **13.3K / 10.7K net new** with Ally's specialist keywords applied

At 10 campaign emails/inbox/day (Spencer's model), on the 30 free mailboxes: Commercial/Asset ≈ 363 business days (~17 months) — **not viable**. Specialist Mortgage/Investment ≈ 107 days (~5 months) — viable. The 1–20 employee cut of the specialist audience (~1.5K net new) finishes in ~3 weeks and is the recommended fast win.

⚠️ That math assumed the 30 Zapmail mailboxes were free *and healthy*. The Aug 22 audit disproved the healthy half — **rerun these estimates before quoting timelines to Chris or Ally.**

---

## Migration Detail: Instantly → Plusvibe — ✅ CLOSED 2026-08-10

*Kept for reference. All campaigns launched Aug 10 except Hillary and Referral Finance (held back deliberately). The checklist and monitoring plan below are historical; live monitoring now runs off `Plusvibe Mailbox Health - Daily Monitor.md`.*

**Objective:** Move all campaigns/leads off Instantly due to infrastructure issues that hurt deliverability last month (July 2026).

**Campaign migration inventory:**

| Campaign | Step Count | Variations | Status |
|----------|-----------|-----------|--------|
| Hillary — Finance Broker | 4 steps | Multiple A/B/C variants | Migrated |
| Mortgage Brokers | 3 steps | Step 1: 4 vars, Step 2: 2 vars, Step 3: 1 var | Migrated |
| Referral Finance Campaign | 2 steps | Step 1: 4 vars, Step 2: 1 var | Migrated |

Plusvibe campaign count: 9 total (up from 6 pre-migration), 7 drafts, 1 completed at time of migration.

**Remaining migration steps:**
- [ ] Import lead lists for each campaign
- [ ] Configure sending mailboxes from Zapmail/InboxKit pool
- [ ] Test email sends (personalization + rendering)
- [ ] Enable warmup settings (20–30% per campaign)
- [ ] Launch campaigns
- [ ] Activate post-migration monitoring, document baseline metrics
- [ ] Create migration report (Plusvibe vs. Instantly comparison)

### Post-Migration Monitoring Plan

**Week 1–2 (critical observation period) — daily:**
- Warmup % per inbox (Plusvibe dashboard)
- Delivery rate vs. Instantly baseline
- Bounce rate changes
- Spam folder placement (keep <5%)
- Confirm all campaigns sending correctly
- Send volume per domain (even distribution)

**Weeks 3–4 — weekly:**
- Compile performance report (pre/post Plusvibe)
- Flag underperforming campaigns
- Adjust warmup settings if delivery drops >10%

**Red flags:** delivery rate drop >15% vs. Instantly baseline; bounce spike >5%; warmup stuck <40% after 10 days; declining open rates; spam complaints; send failures.

**Recovery protocol:** pause new sends → diagnose (warmup %, domain reputation, IP issues) → contact Plusvibe support if technical → consider reverting critical leads to Instantly → document issue + resolution.

---

## Infrastructure & Tools

### Domain & Inbox Providers

**Porkbun** (registrar) — 25 domains total, owner Tremayne Chivers. Dashboard: https://porkbun.com/account/domainsSpeedy
- **Batch 1 (Zapmail):** 10 domains, purchased May 2026, expires 2027-05-14. 30 inboxes (3/domain). List: trysatlas.com, satlastry.com, gosatlas.com, satlasgo.com, satlaswork.com, partnersatlas.com, satlaspartner.com, discoversatlas.com, satlasdiscover.com, satlasworks.com
- **Batch 2 (InboxKit):** 15 domains, purchased July 2026, expires 2027-07-07. 10 provisioned (30 inboxes) + 5 with **zero** mailboxes.
  - **Provisioned (corrected 2026-08-22 via live `domains/list` + `mailboxes/list`):** satlasedge.com, satlaszone.com, withsatlas.com, satlasplus.com, satlasrise.com, satlasready.com, satlashq.com, satlasbase.com, satlasmail.com, satlaslink.com
  - **Unprovisioned:** hellosatlas.com, satlashub.com, usesatlas.com, satlasway.com, satlascore.com
  - ⚠️ The previous version of this list had provisioned/backup **swapped** — hellosatlas, usesatlas, satlasway and satlascore were wrongly shown as active. Fixed.
  - ⚠️ **Unresolved:** the old list contained `satlasriq.com`; the Aug 22 API pull returns `satlashq.com` and no satlasriq. Almost certainly a transcription error, but it has not been confirmed against Porkbun — verify before using either in a doc that matters.

**Zapmail** (https://app.zapmail.ai) — 10 domains, 30 mailboxes. 🔴 **Health 22.65/100** (verified live 2026-08-22, sampled 3 of 10, all identical), **0 of 30 warmed up**, CloudNS SURBL issue unresolved. The old "87/100" figure was stale and had never been re-verified after the July deliverability incident. "Active" in the Zapmail dashboard means *not suspended*, not healthy. **Not sending-safe.**

**InboxKit** (https://app.inboxkit.com) — 15 domains synced, 30 active inboxes (15 Google + 15 Microsoft 365), health 100/100 (verified 2026-08-22), 0 slots remaining. This is the only healthy sending capacity Satlas currently has.

**Instantly** — DEPRECATED, being migrated off.
**Plusvibe** (https://app.plusvibe.ai/v2/campaigns/) — ACTIVE, primary platform going forward.

### Summary Inventory

| Metric | Batch 1 (Zapmail) | Batch 2 (InboxKit) | Total |
|--------|-------------------|-------------------|-------|
| Domains | 10 | 15 (10+5 backup) | 25 |
| Mailboxes | 30 | 30 | 60 |
| Purchase | May 2026 | July 2026 | — |
| Renewal | 2027-05-14 | 2027-07-07 | — |
| Health (2026-08-22) | 🔴 22.65/100 | 🟢 100/100 | — |
| Warmed up | 0/30 | 30/30 | 30/60 |

Total email accounts: 180+ (3 per mailbox + admin). Full breakdown → `OUTPUT/Campaign Tracking/DOMAIN_INVENTORY.md`.

---

## Recurring Tasks

**Monthly:** lead list build (Apollo filters), list validation/QA, copy refresh & A/B testing, deliverability check, end-of-month scorecard.
**Weekly:** campaign launch, performance review (open/reply/bounce rates), reply handling & lead handoff, warmup % monitoring.

---

## Strategic Framework (Satlas Cold Email Playbook)

Built May–June 2026 across 5 milestone calls (infrastructure x2, list building x2, copywriting). Four pillars: Infrastructure, List Building (8-step framework), Copywriting (5-part structure), Launch & Monitor.

**Email sequence strategy:** 3-step sequence (not 6 — more steps = more spam flags):
1. Day 0 — problem/opportunity hook + soft CTA
2. Day 3 — right-person check or pain point expansion
3. Day 7 — recap + final close

**Copywriting rules:** believable small numbers beat impressive big ones ($20K > $100K); never mention SEO/Facebook ads by name, focus on outcomes; subject lines 3–5 words, lowercase, curiosity-driven; Claude preferred over GPT for copy, strip em-dashes and humanize after generation; Spencer and Chris review all new segment copy before launch.

**5-part email structure:** Hook (specific stat) → Context (what you do) → Proof (small believable number) → Ask (soft CTA) → Signature (name + phone + RANDOM close).

**Segmentation:** decision-makers only (Founder/MD/Owner/Director/Principal), small companies (1-20 employees for certain avatars), Australia primary market.

### Buyer Avatars (4)

| Avatar | Pain Point | Lever | Copy Angle |
|---|---|---|---|
| **Finance Brokers** (primary) | Dependent on accountant referrals | 5–10 predictable funding requests/mo, 72-hr funding | Referral fragility, predictability |
| **Financial Planners** | Aging book, referrer fragility | Book renewal, client acquisition | Exit multiples, book value |
| **Buyer's Agents** | Limited investor access, no consistent deal flow | Early investor pipeline access | Investor pipeline, deal flow |
| **Commercial Real Estate Agents** | Referral dependence on accountants/lawyers | Business owner pipeline, mandate flow | Tenant pipeline, revenue predictability |

Each avatar has 4 versions of Email 1, 2 of Email 2, 1–2 of Email 3.

### Client Onboarding Framework
28-day onboarding, daily tasks. Two account setup options: client's own work email, or shared Gmail (`clientname.logins@gmail.com`). MillionVerifier runs on Satlas's company account (shared credits across clients) — everything else the client bills themselves for transparency.

---

## Key Strategic Decisions

- **Infrastructure flow:** Porkbun → Zapmail/InboxKit → Plusvibe (was Instantly).
- **Lead pipeline (per campaign):** Apollo → MillionVerifier → Plusvibe.
- **Why multiple providers:** diversification reduces provider-specific risk.
- **Billing:** client pays their own tool bills (Apollo, Zapmail/InboxKit, Plusvibe) except MillionVerifier (Satlas company account).

---

## Performance & Reference Docs (Notion)

- [Weekly Report: Week 1, July 2026](https://app.notion.com/p/Weekly-Report-Week-1-July-2026-395dae9d2a1a80caa276d9e0091dc05a)
- [Monthly Loom Scoreboard Update - Satlas](https://app.notion.com/p/Monthly-Loom-Scoreboard-Update-Satlas-3abdae9d2a1a80d08a9afbd97269104c)
- [Email Campaigns Analytics](https://app.notion.com/p/Email-Campaigns-Analytics-391dae9d2a1a80c48b08f045d7992a2d)
- [Cold Email Monthly Deliverability Check](https://app.notion.com/p/Cold-Email-Monthly-Deliverability-Check-3aadae9d2a1a8003b0efcd1c24b4b432)
- [Cold Email End-of-Month Scorecard](https://app.notion.com/p/Cold-Email-End-of-Month-Scorecard-3aadae9d2a1a806a85b7dc8ffb126f93)
- [Setting Up Email Campaign Funnels](https://app.notion.com/p/Setting-Up-Email-Campaign-Funnels-364dae9d2a1a80dca19bf314425c67a4)

Full list of Notion links (list build, validation, copy refresh, weekly launch/review, reply handling) lived in the old detailed profile — see version history if needed.

---

## Communication & Check-Ins

- **Daily:** warmup % checks at Plusvibe (5 min)
- **Weekly:** campaign performance review + reply handling (30–45 min)
- **Monthly:** full deliverability audit + scorecard update (1–2 hrs)
- **As needed:** Chris check-ins for strategy/new campaigns/troubleshooting

---

## References

- `OUTPUT/Campaign Tracking/Chris Drew - Satlas Infrastructure & Campaigns.md`
- `OUTPUT/Campaign Tracking/Instantly to Plusvibe - Campaign Migration Guide.md`
- `OUTPUT/Campaign Tracking/Plusvibe Mailbox Health - Daily Monitor.md`
- `OUTPUT/Campaign Tracking/DOMAIN_INVENTORY.md`
- `OUTPUT/Campaign Tracking/Ally-Plusvibe-Artifact-Prompt.md` — setup prompt so Ally can build her own live trackers
- `OUTPUT/Campaign Tracking/Capital Financing/` — Capital Financing sequences + Apollo filters
- Satlas Campaign Tracker (Google Sheet) — shared with Ally as Editor, manual refresh

---

## Open Threads (as of 2026-08-24)

- [ ] Chris's decision: release or recover the 10 Zapmail domains
- [ ] Pause/investigate the 6 high-bounce mailboxes (satlasmail.com pair worst)
- [ ] Copy/targeting review — 0.66% reply rate vs 2% target
- [ ] Fix Capital Financing Trades subject lines to v3 format
- [ ] Build Capital Financing Logistics + Labour Hire sequences
- [ ] Confirm why Hillary + Referral Finance are still held back
- [ ] Rerun Ally's capacity estimates now that Zapmail's 30 mailboxes are known-unhealthy
- [ ] Tremayne's inbound "commercial finance brokers" interest — scope not yet defined
- [ ] Verify satlasriq.com vs satlashq.com against Porkbun

---

**Document owner:** Eikko Ybanez | **Status:** Active & current | **Update monthly** with new projects, avatars, metrics, strategic shifts.
**Change log:** 2026-08-24 — reconciled against EOD log entries Aug 10–22 and the Aug 22 infra audit. Corrected Zapmail health (87→22.65), swapped InboxKit domain lists, closed the Instantly migration, added Capital Financing, Ally capacity work, and current campaign metrics.

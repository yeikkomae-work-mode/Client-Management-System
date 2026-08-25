# Satlas Domain Inventory & Mailbox Configuration

**Account:** Satlas (Porkbun)
**Total Domains:** 25
**Total Mailboxes:** 60 (30 Zapmail + 30 InboxKit)

---

## 📊 BATCH 1: Zapmail Infrastructure (10 Domains + 30 Mailboxes)

**Purchase Date:** May 2026
**Expiration Date:** 2027-05-14 (281 days remaining)
**Connected Platform:** Zapmail (app.zapmail.ai)
**Mailbox Configuration:** 3 mailboxes per domain × 10 domains = 30 mailboxes
**Status:** 🔴 **NOT SENDING-SAFE** — domain health 22.65/100, `isWarmedUp: false` on all 30 mailboxes (verified live 2026-08-22, sampled 3 of 10 domains, identical). CloudNS SURBL issue unresolved. "Active" below means registered/not-suspended only.

### Batch 1 Domains (10 total):
| # | Domain | Status | Created | Expires | Mailboxes |
|---|--------|--------|---------|---------|-----------|
| 1 | trysatlas.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 2 | satlastry.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 3 | gosatlas.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 4 | satlasgo.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 5 | satlaswork.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 6 | partnersatlas.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 7 | satlaspartner.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 8 | discoversatlas.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 9 | satlasdiscover.com | Active | 14 May 2026 | 2027-05-14 | 3 |
| 10 | satlasworks.com | Active | 14 May 2026 | 2027-05-14 | 3 |

**Mailbox Owner:** Tremayne Chivers (all accounts)
**Email Pattern:** tremayne@, tremaynec@, tremayne.c@ (per domain)

---

## 📊 BATCH 2: InboxKit Infrastructure (15 Domains Total)

**Purchase Date:** July 2026
**Expiration Date:** 2027-07-07 (336 days remaining)
**Connected Platform:** InboxKit (app.inboxkit.com)
**Status:** ✅ All Active

### Batch 2A: Provisioned Mailbox Domains (10 domains + 30 mailboxes)

**Corrected 2026-08-22** via live InboxKit `domains/list` + `mailboxes/list`. The previous version of this table had the provisioned and backup lists **swapped**.

| # | Domain | Status | Created | Expires | Mailboxes |
|---|--------|--------|---------|---------|-----------|
| 1 | satlasedge.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 2 | satlaszone.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 3 | withsatlas.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 4 | satlasplus.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 5 | satlasrise.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 6 | satlasready.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 7 | satlashq.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 8 | satlasbase.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 9 | satlasmail.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |
| 10 | satlaslink.com | Active | 07 Jul 2026 | 2027-07-07 | 3 |

Split: 15 Google + 15 Microsoft 365. Slots remaining: 0.

⚠️ **Unresolved:** the previous version of this table listed `satlasriq.com`; the Aug 22 API pull returns `satlashq.com` and no satlasriq. Likely a transcription error, but not confirmed against Porkbun — verify before relying on either.

### Batch 2B: Unprovisioned Domains (5 domains — ZERO mailboxes)

**Purpose:** Registered but never provisioned. Available capacity, not live infrastructure.

| # | Domain | Status | Created | Expires | Mailboxes |
|---|--------|--------|---------|---------|-----------|
| 1 | hellosatlas.com | Registered | 07 Jul 2026 | 2027-07-07 | 0 |
| 2 | satlashub.com | Registered | 07 Jul 2026 | 2027-07-07 | 0 |
| 3 | usesatlas.com | Registered | 07 Jul 2026 | 2027-07-07 | 0 |
| 4 | satlasway.com | Registered | 07 Jul 2026 | 2027-07-07 | 0 |
| 5 | satlascore.com | Registered | 07 Jul 2026 | 2027-07-07 | 0 |

---

## 📈 Summary

### Infrastructure Overview
| Component | Count | Platform | Status |
|-----------|-------|----------|--------|
| **Total Domains** | 25 | Porkbun | ✅ Active |
| **Active Mailboxes** | 60 | Zapmail + InboxKit | ✅ Active |
| **Domain Health** | 🔴 22.65/100 Zapmail · 🟢 100/100 InboxKit | Zapmail / InboxKit | Verified 2026-08-22 |
| **Email Accounts** | 180+ | All platforms | ✅ Active |

### Batch Comparison
| Aspect | Batch 1 (Zapmail) | Batch 2 (InboxKit) |
|--------|------------------|-------------------|
| Domains | 10 | 15 (10 active + 5 backup) |
| Purchase Date | May 2026 | July 2026 |
| Expires | 2027-05-14 | 2027-07-07 |
| Days Remaining | 281 | 336 |
| Mailboxes | 30 (3 per domain) | 30 (3 per domain) |
| Total Email Accounts | 30 | 30 (+ 5 backup domains) |
| Platform | Zapmail | InboxKit |
| Owner | Tremayne Chivers | Tremayne Chivers |

---

## 🔧 Configuration Details

### Zapmail Batch (10 Domains)
- **DNS:** Configured with Zapmail nameservers
- **Mailbox Setup:** 3 accounts per domain (admin + 2 regular)
- **Export Integrations:** Slack ✅, Pinterest ✅
- **Health Score:** 🔴 22.65/100 (2026-08-22) — the old 87/100 figure was stale and never re-verified after the July deliverability incident
- **Warmup:** 0 of 30 mailboxes warmed up
- **Renewal Cost:** 3 × $12.52 = $37.56 per domain annually

### InboxKit Batch (15 Domains)
- **Active Domains (10):** Configured with InboxKit infrastructure
- **Backup Domains (5):** Ready for expansion or failover
- **Mailbox Setup:** 3 accounts per active domain only
- **Status:** 15 domains synced to InboxKit account
- **Capacity:** 5 domains available for future expansion without additional purchases

---

**Last Updated:** 2026-08-24 (domain lists + health corrected from the 2026-08-22 live API audit)
**Next Renewal:** Batch 1 on 2027-05-14, Batch 2 on 2027-07-07

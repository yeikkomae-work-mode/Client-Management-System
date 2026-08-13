# ECO Workflows & Automations
**Last Updated:** 2026-08-05 11:38 PHT

## Active Workflows

### 1. LinkedIn Content Posting (Fractio / Chris Caffera)
**Status:** ✅ Active — v1.1 (confirmed working process, Aug 6, 2026)

**Correction (Aug 6):** Posts go out under **Chris Caffera's own personal LinkedIn** (logged in via the **VA Profile** Chrome profile, yeikkomae@gmail.com) — not Fatin Kwasny/Fractio company page as originally assumed. See `ECO - CHROME PROFILE ACCESS GUIDE.md` for the profile reference.

**Confirmed Workflow:**
1. Open Google Drive → `Fractio_Week2_LinkedIn_Complete.docx` for that week's drafted posts
2. Copy the "ready to paste" post copy block for the post going out
3. In the **VA Profile** Chrome window, go to Chris Caffera's LinkedIn → "Start a post"
4. Paste the copy into the composer
5. Cross-check Slack (**Fractio workspace → #marketing channel**) for the matching image asset — Eikko/Chris/Fatin review images together in a thread each week before posting
6. Download the correct image from Slack and attach it to the LinkedIn post
7. Click the clock icon → "Schedule post" → set date & time (Philippine Standard Time)
8. Confirm — LinkedIn shows "Post scheduled. View scheduled posts"

**Content Themes:**
- Professional services pricing models
- AI economics (no hype, outcomes-focused)
- CPA pricing disruption
- 30-Day Diagnostic framework

**Tools:**
- Browser: VA Profile Chrome (yeikkomae@gmail.com) — logs directly into Chris Caffera's personal LinkedIn
- Google Docs: `Fractio_Week2_LinkedIn_Complete` (copy source)
- Slack: Fractio workspace, #marketing channel (image assets + review thread)

**Log of Scheduled Posts:**
| Date Scheduled | Post | Publish Time | Notes |
|---|---|---|---|
| 2026-08-06 | "What a 30-Day Diagnostic Should Do" | Thu Aug 6, 11:00 PM PHT | Image pulled from Slack #marketing thread; copy from Fractio_Week2_LinkedIn_Complete |

**Next:** Confirm weekly cadence, decide whether ECO should run copy/image pairing + scheduling end-to-end going forward (candidate for a saved skill).

---

## Scheduled Automations

### 1. ECO Morning Email Briefing
**Task ID:** `eco-morning-email-briefing`  
**Schedule:** 8:00 AM PHT, every day  
**Status:** ✅ Active

**What it does:**
- Monitors Gmail (yeikkomae@gmail.com) + Outlook (eikko ybanez)
- Alerts on emails from: Chris Caffera, Chris Drew, Chris Soriano, Yoni, Krishna
- **ALWAYS includes:** Fractio emails (@fractio.co, Fatin Kwasny, "Fractio" mentions)
- Filters client emails + webinar invites
- Auto-creates calendar events for webinars
- Auto-archives promotional/social/update emails
- Delivers morning briefing: Fractio + clients + opportunities + webinars

**Monitored clients:**
- Satlas, MyCloudGCS, PeakPros, Phygtl Inc., BalanceBoat, Wise Transactions
- **Fractio:** @fractio.co domain + Fatin Kwasny + "Fractio" keywords

**Alert Delivery:**
- Real-time (native Gmail/Outlook notifications)
- Morning briefing summary (8 AM PHT) — Fractio section highlighted

---

### 2. Lemwarm Daily Health Check — alex
**Task ID:** `lemwarm-alex-daily-monitor`  
**Schedule:** 9:00 AM PHT, every day  
**Status:** ✅ Active

**What it does:**
- Checks alex's Lemwarm deliverability score daily
- Alerts here in Claude if score ≥90% or ≥100%
- Provides status updates below 90%

**Dashboard:** https://app.lemwarm.com/teams/tea_frti7zwCWCFtBAYtZ/dashboard/usm_CwAQK7dHWRJqaahFh

**Current Score:** 70% (warming domain, capped at ~90 until mature)

**Alert Thresholds:**
- 🔥 100% → "READY FOR CAMPAIGNS"
- ⚠️ 90%+ → "Approaching campaign readiness"
- ✅ <90% → "Continue warmup — [score]%"

---

## Pending Workflows
(None yet — will add as we create)

---

## Sync Protocol
When new workflows/automations created:
1. Document in this file
2. Create separate file if complex (e.g., `ECO_LINKEDIN_WORKFLOW.md`)
3. Link client in ECO_CLIENTS.md
4. Test before marking "active"
5. Update this sync timestamp

# ECO Email Intelligence System
**Last Updated:** 2026-08-05 11:45 PHT

## Overview
ECO now monitors your email across Gmail and Outlook with intelligent filtering for high-value messages while ignoring noise.

---

## Active Monitoring

### Email Accounts Monitored
| Account | Platform | Status |
|---------|----------|--------|
| yeikkomae@gmail.com | Gmail | ✅ Active |
| eikko ybanez | Outlook | ✅ Active |

### Priority 1 — Immediate Alerts

**VIP Contacts:**
- Chris Caffera (Fractio)
- Chris Drew (Satlas)
- Chris Soriano (Project-based)
- Yoni (Albertscott)
- Krishna (Peru campaign)

**Fractio-Related (Always Included):**
- FROM: @fractio.co, Fatin Kwasny
- TO: Chris Caffera (Fractio context)
- Keywords: "Fractio", "content", "LinkedIn", "campaign", "post"

**Other Clients:**
- All known clients + new senders (outside promotional/social/updates)
- Labels: Satlas, MyCloudGCS, PeakPros, Phygtl, BalanceBoat, Wise

**Urgent Keywords:**
- "meeting", "call", "demo", "proposal", "urgent", "action required"

### Priority 2 — Webinars & Events
**Automatically:**
- Extract event details
- Create calendar events (date, time, registration link)
- Report in morning briefing

**Keywords monitored:**
- webinar, event, summit, conference, workshop, training

---

## Automated Filtering

### Auto-Archive (Ignore)
These emails are automatically filtered out:

**Senders:**
- no-reply@*, promo@*, marketing@*, newsletter@*

**Folders/Labels:**
- Promotions
- Social
- Updates

**Keywords:**
- "unsubscribe", "promotional offer", "limited time", "don't miss out"

---

## Scheduled Automations

### 1. ECO Morning Email Briefing
**Task ID:** `eco-morning-email-briefing`  
**Schedule:** 8:00 AM PHT, every day  
**Status:** ✅ Active

**Delivers:**
- 📧 Client & opportunity emails (Priority)
- 🎓 Webinars & events (with calendar events created)
- 📊 Summary count (emails, responses needed, calendar events)

**Next run:** Tomorrow 8:00 AM PHT

---

## Real-Time Alerts

**How it works:**
- Gmail/Outlook native notifications still show (from VIPs + clients)
- ECO doesn't duplicate — morning briefing summarizes all

**Best practice:**
- Keep Gmail/Outlook open during working hours
- Check morning briefing for daily summary at 8 AM
- ECO flags urgent items here in Claude when you check in

---

## Setup Checklist

- [x] Gmail monitored (yeikkomae@gmail.com)
- [x] Outlook monitored (eikko ybanez)
- [x] VIP sender list configured
- [x] Client accounts configured
- [x] Promotional/social/update filters active
- [x] Webinar auto-event creation enabled
- [x] Morning briefing scheduled (8 AM PHT)
- [ ] Gmail/Outlook filters optimized (manual setup)
- [ ] Additional client domains added (if needed)

---

## Manual Setup Recommended

**In Gmail:**
Create filter: `from:(no-reply@ OR promo@ OR marketing@ OR newsletter@) OR "promotional offer"`
→ Auto-archive

**In Outlook:**
Create rule: Subject contains "promotional offer" OR "limited time"
→ Move to Archive

---

## Sync Status
✅ Synced to Claude Code  
✅ Scheduled task created  
✅ Ready for morning briefings  

**Last verified:** 2026-08-05 11:45 PHT

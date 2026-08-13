# Plusvibe Mailbox Monitoring — Setup & Configuration

**Status:** ✅ **ACTIVE AND RUNNING**  
**Created:** 2026-08-05  
**Owner:** Eikko (Chris Drew - Satlas)  
**Monitor Type:** Automated Daily + Manual Inspection

---

## 🎯 MONITORING OBJECTIVE

**Primary Goal:** Track Plusvibe mailbox health and deliverability with immediate alerts on:
- Mailboxes reaching 98%+ utilization
- Any error conditions
- Any alert flags
- Performance degradation

---

## ⚙️ AUTOMATED MONITORING SETUP

### Scheduled Task: `plusvibe-daily-mailbox-monitor`

| Property | Value |
|----------|-------|
| **Status** | ✅ Active |
| **Schedule** | Every day at 9:05 AM PHT |
| **Frequency** | Daily (7 days/week) |
| **Run Duration** | 5-10 minutes |
| **Alert Threshold** | 98%+ utilization or any errors |
| **Next Run** | Tomorrow at 9:05 AM |
| **Notifications** | Enabled (alerts when task completes) |

### What The Task Does

**Every Morning at 9:05 AM PHT:**
1. ✅ Navigates to Plusvibe Email Accounts dashboard
2. ✅ Checks all 60 mailboxes for health status
3. ✅ Scans for errors (target: 0)
4. ✅ Scans for alerts (target: 0)
5. ✅ Checks utilization levels (alert at 98%+)
6. ✅ Reviews bounce rates (alert if >5%)
7. ✅ Reviews deliverability (alert if <95%)
8. ✅ Updates all tracking files automatically
9. ✅ **Notifies Eikko immediately if issues found**

### Alert Conditions

| Alert Level | Trigger | Action |
|-------------|---------|--------|
| 🔴 **CRITICAL** | Mailbox at 100% OR Error count >0 OR Alert flag set | Immediate notification + escalation |
| 🟡 **WARNING** | Mailbox at 98-99% OR Bounce >5% OR Deliverability <95% | End-of-day notification + review |
| 🟢 **HEALTHY** | All metrics within normal range | Routine logging only |

---

## 📋 FILES AUTOMATICALLY UPDATED DAILY

### 1. **Plusvibe Mailbox Health - Daily Monitor.md**
   - **What:** Daily snapshot of mailbox health
   - **Updated:** Every morning at 9:05 AM
   - **Tracks:** Account count, error count, alert count, warmup status
   - **Location:** `/Client-Management-System/Campaign Tracking/`

### 2. **Chris Drew - End of Day Log.md**
   - **What:** Daily work log entry
   - **Updated:** Mailbox health summary added each morning
   - **Tracks:** Daily health status (✅ HEALTHY / 🟡 WARNING / 🔴 CRITICAL)
   - **Location:** `/Client-Management-System/End-of-Day Reports/`

### 3. **Chris Drew - Satlas Infrastructure & Campaigns.md**
   - **What:** Campaign tracking with infrastructure metrics
   - **Updated:** Email health section refreshed daily
   - **Tracks:** Platform health scores, mailbox counts, campaign performance
   - **Location:** `/Client-Management-System/Campaign Tracking/`

### 4. **EIKKO_MEMORY.md**
   - **What:** Quick reference memory system
   - **Updated:** Quick reference if critical issue found
   - **Tracks:** Current status, platform health, key metrics
   - **Location:** `/Claude Code/`

---

## 🚀 HOW TO USE

### Daily Workflow

**Each Morning (9:05 AM):**
1. Task runs automatically
2. Plusvibe dashboard is checked
3. If 🟢 HEALTHY: Files updated silently, you see notification
4. If 🟡 WARNING: Files updated + alert notification
5. If 🔴 CRITICAL: Immediate alert + escalation

### Manual Inspection (Recommended Daily)

**To manually verify status anytime:**
1. Go to: [app.plusvibe.ai/v2/email-accounts/](https://app.plusvibe.ai/v2/email-accounts/)
2. Check dashboard summary cards (top of page)
3. Look for red/yellow indicators
4. Scan account list for any flag icons
5. Review any accounts >98% utilization

### Weekly Review (Fridays)

**Every Friday:** Run manual inspection + review weekly metrics
- Check 7-day warmup deliverability trend
- Review reply rate changes
- Check bounce rate trend
- Identify top/bottom performing domains
- Document in weekly summary section

---

## 📊 KEY METRICS TO MONITOR

### Critical Metrics (Daily Check)

| Metric | Target | Alert Level |
|--------|--------|-------------|
| Total Active Accounts | 60 | If <60 |
| Error Count | 0 | If >0 🔴 |
| Alert Count | 0 | If >0 🔴 |
| Mailbox Utilization | <98% | If 98%+ 🟡 |
| SPF/DKIM/DMARC | Configured | If misconfigured 🔴 |

### Performance Metrics (Weekly Review)

| Metric | Target | Range |
|--------|--------|-------|
| Warmup Deliverability | >98% | 95-100% ✅ |
| Reply Rate | >2% | 0-5% ✅ |
| Bounce Rate | <2% | 0-5% ✅ |
| Account Health Score | >95 | 90-100 ✅ |

---

## 🔔 ALERT SCENARIOS

### Scenario 1: Mailbox at 98%+ Utilization
**What it means:** Account is nearly full, approaching failure  
**Risk:** Email sends will start failing  
**Action:**  
- Check if account has email limits
- Archive old emails if possible
- Consider adding new domain if quota hit
- Monitor closely next 24 hours

### Scenario 2: Error Count Increases
**What it means:** One or more accounts have connection/authentication issues  
**Risk:** Those accounts can't send emails  
**Action:**  
- Identify which account(s)
- Try reconnecting in Plusvibe
- Check Google/Microsoft account permissions
- Verify OAuth tokens
- Re-authenticate if needed

### Scenario 3: Alert Flag Set
**What it means:** Plusvibe detected an issue with account setup/configuration  
**Risk:** Account may be suspended or flagged by ESPs  
**Action:**  
- Click account to see alert details
- Review SPF/DKIM/DMARC status
- Re-check DNS records in Porkbun
- Contact Plusvibe support if needed

### Scenario 4: Bounce Rate >5%
**What it means:** High percentage of sent emails are bouncing  
**Risk:** Domain reputation declining  
**Action:**  
- Check if leads are valid
- Review email content for spam triggers
- Verify sending volume isn't too high
- Check recipient list quality

### Scenario 5: Deliverability <95%
**What it means:** Most emails going to spam or being rejected  
**Risk:** Campaign ROI declining  
**Action:**  
- Review domain reputation (check feedback loops)
- Verify SPF/DKIM/DMARC configuration
- Warm up sending volume gradually
- Check for IP blocks

---

## 📱 RECEIVING ALERTS

### Notification Types

**🟢 HEALTHY Alert**
- Time: 9:05 AM every day
- Message: "Plusvibe mailbox monitoring complete - All systems healthy"
- Action: Review briefly, proceed with day

**🟡 WARNING Alert**
- Time: 9:05 AM when warning detected
- Message: "Plusvibe WARNING - [ISSUE]: Check end-of-day log for details"
- Action: Review issue, plan fix for tomorrow or urgent if critical

**🔴 CRITICAL Alert**
- Time: Immediate when critical detected
- Message: "🚨 CRITICAL PLUSVIBE ALERT - [ISSUE]: Immediate action required"
- Action: Drop everything and address immediately

### Where Alerts Appear
- Task notification (in app)
- Check "Scheduled" section for task status
- See detail in updated tracking files

---

## 🛠️ MAINTENANCE & TROUBLESHOOTING

### Task Not Running?
1. Check: Is Cowork app open? (Task runs while app is open)
2. Check: Did app close at 9:05 AM? (Task runs on next launch)
3. Verify: Navigate to Scheduled section, see if task shows as active
4. Restart: Close and reopen app to trigger missed run

### Alerts Too Frequent?
- Increase threshold if false alarms
- Adjust task time if 9:05 AM conflicts with other work
- Disable notifications if not needed (but not recommended)

### Manual Override?
If you need to run the task immediately:
1. Open Cowork app
2. Go to Scheduled section
3. Find "plusvibe-daily-mailbox-monitor"
4. Click "Run Now"
5. Task executes immediately and updates all files

---

## 📝 INTEGRATION WITH OTHER MONITORING

### Zapmail Monitoring
- Batch 1: 10 domains, 30 mailboxes
- Health Score: 87/100
- Separate monitoring (different dashboard)
- Check via app.zapmail.ai

### InboxKit Monitoring
- Batch 2: 10 active domains, 30 mailboxes (+ 5 backup)
- Health Score: 100/100
- Separate monitoring (different dashboard)
- Check via app.inboxkit.com

### Correlation
If Plusvibe shows issues:
1. Check which domains are affected
2. Go to Zapmail or InboxKit
3. Verify domain configuration there too
4. Look for related issues (DNS, authentication, etc.)

---

## 📆 WEEKLY & MONTHLY REVIEWS

### Weekly Summary (Every Friday)
Review the daily logs and compile:
- Days with ✅ HEALTHY status
- Any ⚠️ WARNINGS encountered
- Any 🔴 CRITICAL issues
- Performance trends
- Domains needing attention

### Monthly Review (End of Month)
Analyze entire month:
- Overall uptime %
- Average deliverability
- Any systemic issues
- Comparison to previous month
- Forecast for next month

---

## 🎯 SUCCESS METRICS

**Target Performance:**
- ✅ 99%+ uptime (59+ days healthy per month)
- ✅ 98%+ average deliverability
- ✅ <2% bounce rate
- ✅ >2% reply rate
- ✅ 0 critical incidents
- ✅ <2 warnings per month

---

## 📞 SUPPORT & ESCALATION

**If Critical Issue Found:**
1. Document in Plusvibe Mailbox Health Monitor
2. Screenshot the issue
3. Note exact account and metric
4. Check related files (Zapmail, InboxKit)
5. Review Porkbun domain configuration if DNS-related
6. Notify Eikko immediately with full details

**Escalation Contacts:**
- **Plusvibe Support:** help.plusvibe.ai
- **Zapmail Issues:** app.zapmail.ai support
- **InboxKit Issues:** app.inboxkit.com support
- **Domain Issues:** Porkbun account management

---

## ✅ SETUP VERIFICATION CHECKLIST

- [x] Scheduled task created: `plusvibe-daily-mailbox-monitor`
- [x] Schedule: Daily at 9:05 AM PHT
- [x] Alert threshold: 98%+ or any errors
- [x] File updates configured:
  - [x] Plusvibe Mailbox Health - Daily Monitor.md
  - [x] Chris Drew - End of Day Log.md
  - [x] Chris Drew - Satlas Infrastructure & Campaigns.md
  - [x] EIKKO_MEMORY.md
- [x] Notifications enabled
- [x] Manual inspection instructions provided
- [x] Alert scenarios documented
- [x] Escalation protocol defined

---

**Status:** 🟢 **MONITORING SYSTEM LIVE**  
**Last Updated:** 2026-08-05  
**Next Scheduled Run:** Tomorrow 9:05 AM PHT

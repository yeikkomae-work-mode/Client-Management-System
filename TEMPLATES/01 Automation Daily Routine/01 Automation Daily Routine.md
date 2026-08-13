# 01 Automation Daily Routine — Spec

**Purpose:** Repeatable daily workflow to check all clients, log work progress, monitor campaigns, and generate yesterday's recap.

**Trigger:** Eikko runs this every morning (or on-demand during the day).

**Output:** 
- Yesterday's recap (tasks completed, missed messages, campaign metrics, meeting summaries)
- Today's task checklist (what to do per client)
- Work logger ready (for logging current tasks)

---

## Daily Routine Steps (by Client)

### Chris Caffera
**Time to run:** ~15-20 min
```
1. Check messages
   - Outlook for new emails
   - Slack for updates from Chris or team
   - WhatsApp (Chris & Fatin)
   - Note any urgent items
   
2. Review task list
   - What was completed yesterday
   - What carried over
   - What's new from Chris
   
3. Monitor campaigns
   - Hubspot: check campaign status, open rate, replies
   - Lemlist: check sequence performance, open rate, bounces
   - Log metrics (pull via API or manual review)
   
4. Schedule LinkedIn posts
   - Check if new posts are pending
   - Schedule for Chris & Fatin accounts
   
5. Note ad-hoc items
   - Any other tasks Chris mentioned
```

### Chris Drew
**Time to run:** ~10 min
```
1. Check messages
   - Email for updates
   - WhatsApp group chat
   
2. Monitor PlusVibe
   - Campaign inbox health
   - Campaign performance (opens, clicks, replies)
   - Log metrics
   
3. Record data
   - Any data Chris provided
   - Update Notion campaign tracker
```

### Yoni
**Time to run:** ~15 min
```
1. Check messages
   - Email for updates
   - WhatsApp for urgent items
   
2. Open Smartlead
   - Review tagged prospects (per Smartlead workflow rules)
   - Tag any new replies
   - Note which are "interested"
   
3. Open Pipedrive
   - Move interested prospects from Smartlead → Pipedrive
   - Log follow-ups
   
4. Check email for Calendly bookings
   - Any new bookings from prospects
   - Add booked contacts to Pipedrive
   - Add email to Smartlead blocklist
   
5. Log hours (reference TimeDoctors)
```

### Krishna (3x per week, not daily)
**Time to run:** ~10 min
```
1. Check WhatsApp for new requests
2. Review ICP (if changes needed)
3. Run Apollo searches as assigned
4. Log sequences or campaigns created
```

### Chris Soriano (As-needed)
**Time to run:** Variable
```
1. Check WhatsApp for task assignment
2. When assigned:
   - Google search for requested info
   - Compile list in spreadsheet
   - Share with Chris
```

---

## Yesterday's Recap Generator

**Prompt for Claude:** "Generate yesterday's recap for all clients using this data:"

**Data to pull:**
- Work log entries from app (what Eikko logged as completed)
- Campaign metrics (from APIs or manual logs)
- Messages checked (missed WhatsApp/email during sleep)
- Meeting summaries (if meeting occurred yesterday)
- Upcoming tasks/deadlines

**Recap format (bullet list by client):**

```
YESTERDAY'S RECAP — [Date]

✓ CHRIS CAFFERA
  Tasks completed:
    - [Task 1]
    - [Task 2]
  Missed messages: [Summarize if any]
  Campaign metrics:
    - Hubspot: [Open rate, replies, status]
    - Lemlist: [Open rate, bounces, clicks]
  Reminders: [Any action items for today]
  Meeting: [If occurred: summary + action items]

✓ CHRIS DREW
  Tasks completed:
    - [Task 1]
  Missed messages: [Summarize if any]
  Campaign metrics:
    - PlusVibe inbox health: [Status]
    - Campaign performance: [Opens, clicks, replies]
  Reminders: [Action items]

✓ YONI
  Tasks completed:
    - [Prospects tagged: X]
    - [Moved to Pipedrive: X]
    - [Calendly bookings logged: X]
  Missed messages: [Summarize if any]
  Hours logged: [From TimeDoctors]
  Reminders: [Action items]

✓ KRISHNA
  Tasks completed: [If active this week]
  Reminders: [Action items]

✓ CHRIS SORIANO
  Tasks completed: [If assigned]
  Reminders: [Waiting for assignment]
```

---

## Meeting Summary Processor

**When a meeting happens with Chris Caffera (or any client with meetings):**

**Input:** Transcript (from Calendly, Google Meet, Zoom, or manual notes)

**Process:**
1. Summarize: What was discussed (2-3 sentences)
2. Extract action items: Who, what, by when
3. Note decisions made
4. Store in app for future reference

**Output format:**
```
MEETING SUMMARY — [Client] — [Date & Time]
Attendees: [Who was there]
Duration: [How long]

Summary:
[2-3 sentences of what was discussed]

Action Items:
- [Action] — Owner: [Who] — Due: [Date]
- [Action] — Owner: [Who] — Due: [Date]

Key Decisions:
- [Decision 1]
- [Decision 2]

Next meeting: [If scheduled]
```

---

## Work Logger Integration

**Each morning, Eikko uses the work logger to track what they're doing:**

```
WORK LOG ENTRY
Client: [Client name]
Task: [What am I working on]
Goal: [What I want to accomplish]
Start time: [When started]
---
[Work happens]
---
COMPLETED
Accomplishment: [What I actually got done]
Time spent: [Duration]
Notes: [Any blockers or next steps]
```

**The recap pulls from these logs to show: "Yesterday I completed X, Y, Z for client A."**

---

## Campaign Metrics to Track

### Chris Caffera
- **Hubspot:** Emails sent, open rate %, reply rate %, bounces, deal status
- **Lemlist:** Emails sent, open rate %, click rate %, bounces, sequence progress

### Chris Drew
- **PlusVibe:** Inbox health score, campaign open rate %, reply rate %, bounces, clicks

### Yoni
- **Smartlead:** Prospects tagged, interested count, follow-up count
- **Pipedrive:** Prospects added, stages moved, close rate

---

## Automation Trigger Options

**Option 1 (Manual):** Eikko runs Claude prompt each morning
**Option 2 (Scheduled):** Set up recurring prompt at specific time (e.g., 8am PHT daily)
**Option 3 (Hybrid):** Run automatically at night, Eikko reviews in morning

**Recommendation:** Start with manual, move to scheduled once refined.

---

## Questions for Eikko

1. Should the automation pull data directly from APIs or use manual logging?
2. When should the daily routine run? (Morning? Night? On-demand?)
3. Are there other recurring checks we missed?
4. How detailed should campaign metrics be? (All numbers or just key trends?)

---

**Status:** Spec written. Awaiting approval and API connection decisions.

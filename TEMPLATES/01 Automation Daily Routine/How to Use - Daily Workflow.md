# How to Use — Daily Automation Workflow

**Your daily rhythm with this automation system.**

---

## YOUR DAY WORKFLOW (1pm - 5am PHT)

```
LOG IN & START WORK
  ↓
You: "good morning"
  ↓
I: Generate recap + task checklist
  ↓
Review + START WORKING
  └─ Use Work Logger for each task
  ↓
WIND DOWN (approaching 5am)
  ├─ You: "done for today"
  ├─ I: Ask for end-of-day metrics
  ├─ You: Provide metrics
  ├─ I: Store for tomorrow
  ↓
LOG OFF
  └─ Ready for next "good morning"
```

---

## STEP-BY-STEP GUIDE

### MORNING (When you start work)

**1. You say: "Good morning"**

That's it. Just say "good morning" in chat.

**2. I'll respond:**

I'll pull data from:
- API connections (Smartlead, Pipedrive, TimeDoctors)
- Yesterday's manual metrics (if you provided them yesterday)

I'll generate:
```
YESTERDAY'S RECAP — [Date]

✓ CHRIS CAFFERA
  Tasks: [3 items]
  Metrics: [Campaign performance]
  Reminders: [Follow-ups needed]

✓ CHRIS DREW
  Tasks: [2 items]
  Metrics: [Campaign performance]
  ...

✓ YONI
  Tasks: [What you did]
  Hours: [5 hours from TimeDoctors]
  ...

TODAY'S CHECKLIST
☐ Chris Caffera: Check emails, monitor Hubspot, schedule posts
☐ Chris Drew: Check updates, monitor PlusVibe
☐ Yoni: Smartlead tagging, Pipedrive updates, Calendly routing
☐ Krishna: [If active]
☐ Chris Soriano: [If assigned]
```

**3. Review + Start working**

Review the recap, ask any questions, then start your day.

---

### THROUGHOUT YOUR DAY (1pm - 5am)

**Whenever you complete a task or work session:**

Go to `/Build-out/01 Automation Daily Routine/Work Logger Prompt.md`

Paste:
```
COMPLETED WORK

Client: [Eikko's current client]
Task: [What you worked on]
Goal: [What you aimed for]
Accomplished: [What you got done]
Time spent: [Duration]
Blockers: [Any issues?]
Notes: [Next steps?]
```

**Example:**
```
COMPLETED WORK

Client: Yoni
Task: Smartlead tagging and Pipedrive updates
Goal: Process all overnight replies and move interested to Pipedrive
Accomplished: Tagged 25 replies, moved 15 to Pipedrive, added 10 to blocklist
Time spent: 1 hour 20 minutes
Blockers: None
Notes: Strong engagement on latest sequence; follow up tomorrow on 3 warm leads
```

**I'll store this entry. It feeds into tomorrow's recap.**

---

### WHEN YOU HAVE A MEETING

**If a meeting happens with a client (especially Chris Caffera on Mondays):**

1. Record it (phone, Teams, Zoom, etc.)
2. Export the transcript
3. Go to `/Build-out/01 Automation Daily Routine/Meeting Transcript Processor.md`

Paste:
```
MEETING TRANSCRIPT

Client: [Client name]
Date: [Date & time]
Attendees: [Who was there]
Platform: [Teams / Phone / Zoom / etc]

[Paste transcript here]
```

**I'll process it:**
```
MEETING SUMMARY — [Client] — [Date]

Summary: [2-3 sentences]

Action Items:
- [ ] [Action] — Owner: [Person] — Due: [Date]
- [ ] [Action] — Owner: [Person] — Due: [Date]

Key Decisions:
- [Decision 1]
- [Decision 2]

Blockers: [If any]

Next meeting: [Date if scheduled]
```

**This gets stored and included in your next recap.**

---

### END OF DAY (Approaching 5am)

**1. You say: "Done for today"**

**2. I'll ask:**
"What are your end-of-day metrics?"

**3. You provide:**

Quick list of your day's metrics:
```
CHRIS CAFFERA

Hubspot campaigns:
  - "Summer Launch": Open 12%, Replies 8%, Bounces 2

Lemlist sequences:
  - "Welcome series": Open 8%, Clicks 3%

LinkedIn:
  - Posts scheduled: 2
  - Engagements: 15

Other notes:
  - Chris approved new subject lines tomorrow
```

(Just the tools that don't auto-pull. Smartlead, Pipedrive, TimeDoctors are already tracked.)

**4. I'll store it**

Your metrics are saved for tomorrow's recap.

**5. I'll also update your End-of-Day Reports**

Each client has a daily log file (`/End-of-Day Reports/`) where I'll add:
- Date
- Tasks completed
- Metrics from today
- Any notes

This builds a searchable history you can reference anytime.

**6. You're done**

Whenever you're ready tomorrow, say "good morning" and the cycle repeats.

---

## QUICK REFERENCE

| Trigger | Action | What you do |
|---------|--------|------------|
| Start work | You say: "good morning" | I generate recap + checklist |
| During day | After each task | Paste work log entry |
| During day | If meeting | Paste transcript → I process |
| End of day | You say: "done for today" | I ask for metrics → you provide |

---

## TIPS

1. **Work Logger is fast** — 30 seconds to log a task. Do it right after you finish.

2. **Manual metrics** — Copy-paste from your tools (Hubspot, Lemlist, LinkedIn). No manual note-taking needed.

3. **"Good morning" is the trigger** — When you're ready, paste it and I'll generate your recap. It's on-demand, not scheduled.

4. **Meetings are optional** — If you have a transcript, paste it. If not, just note in work log or metrics.

5. **It gets better over time** — First week is manual. As we connect more APIs, less manual input needed.

---

## COMMON QUESTIONS

**Q: What if I forget to log something?**
A: No problem. When you say "done for today," just add missed tasks to your metrics. I'll include them in the recap.

**Q: Can I log multiple work entries at once?**
A: Yes! Paste several "COMPLETED WORK" entries in one message. I'll store them all.

**Q: What if a tool gets connected mid-day?**
A: Tell me in a message. I'll update the automation to pull from it starting next recap.

**Q: What if I don't have yesterday's metrics when I say "good morning"?**
A: I'll generate a recap with API data. When you "done for today," you can fill in manual metrics then, and I'll use them for tomorrow's recap.

**Q: Can I skip days?**
A: Yes. Just say "good morning" whenever you're ready. I'll use whatever metrics you have. If you missed metrics from earlier, just provide them when you say "done for today."

---

## YOU'RE READY

Your automation is set up with four prompts:
1. **Good Morning Prompt** — Daily recap generator (on-demand, 1pm)
2. **Work Logger Prompt** — Task tracker (throughout day)
3. **Meeting Transcript Processor** — Meeting summary generator (as-needed)
4. **Manual Metrics Input** — Metric logger (end-of-day, ~5am)

**Start tomorrow (or whenever you're ready): Say "good morning" and I'll get you started.**

---

**Next:** We move to building **Plugin (02 Client Templates)** once you're comfortable with this automation.

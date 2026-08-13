# 03 App Dashboard & Work Logger — Spec

**Purpose:** The main interface Eikko uses daily to see all clients, log work, track tasks, and view yesterday's recap. Single HTML/data-driven app (no images, text/data only).

**Users:** Eikko only (private).

**Platform:** Web-based (desktop primary), data-only format.

---

## App Views

### View 1: Yesterday's Recap (Dashboard Home)

**What it shows:** When Eikko opens the app, first thing is yesterday's summary.

**Layout:**
```
YESTERDAY'S RECAP — [Date]

✓ CHRIS CAFFERA
  Tasks completed: [3 items]
  Missed messages: [2 messages from Chris]
  Campaign performance:
    • Hubspot: 12% open rate, 3 replies
    • Lemlist: 8% open rate, 1 reply
  Reminder: Monday 10am meeting
  Meeting summary: [Link to full summary if meeting occurred]

✓ CHRIS DREW
  Tasks completed: [2 items]
  Missed messages: None
  Campaign performance:
    • PlusVibe inbox health: 87% (healthy)
    • Active campaign: 156 opens, 12 clicks
  Reminder: None

✓ YONI
  Tasks completed: [5 items: 8 prospects tagged, 3 moved to Pipedrive, 1 Calendly booking logged]
  Missed messages: [1 message]
  Hours logged: 5 hours (TimeDoctors)
  Reminder: Follow up on 3 warm leads

✓ KRISHNA
  Status: [No active work this week]

✓ CHRIS SORIANO
  Status: [Waiting for task assignment]
```

**Interaction:**
- Click on client name → see full details for that client
- Click on meeting link → open meeting summary
- Click on campaign → open campaign metrics detail

---

### View 2: Work Logger (Current Work Tracker)

**What it shows:** Eikko's current task and goal; gets logged when completed.

**Layout:**
```
CURRENTLY WORKING ON...

Client: [Dropdown: Chris Caffera / Chris Drew / Yoni / Krishna / Chris Soriano]
Task: [Text input: What am I doing?]
Goal: [Text input: What do I want to accomplish?]
Start time: [Auto-filled with current time]

[WORK IN PROGRESS...]

Status: Working
Elapsed: [Auto-updated timer]
Pause | Stop | Cancel

---

WHEN DONE:

Stop working button clicked...

What did you accomplish? [Text area]
Time spent: [Auto-calculated from start time]
Save

✓ LOGGED
[Confirmation with the work entry]
```

**Data saved:**
- Client
- Task
- Goal
- Accomplishment
- Time spent
- Timestamp

**This data feeds into Yesterday's Recap.**

---

### View 3: Client Details

**When Eikko clicks on a client, they see:**

```
CLIENT: [Client Name]

CONTACT INFO
- Email: [email]
- WhatsApp: [link]
- Timezone: [timezone]
- Rate: [contract type]
- Working hours: [hours]

CURRENT PROJECTS
- [Project 1]
- [Project 2]

TODAY'S CHECKLIST
☐ [Task 1]
☐ [Task 2]
☐ [Task 3]
[Check/uncheck boxes]

MESSAGES TO CHECK
- Email: [# unread]
- WhatsApp: [# unread]
- Slack: [# unread if applicable]
[Button: Mark checked]

ACTIVE CAMPAIGNS
| Campaign | Tool | Status | Open Rate | Replies |
|----------|------|--------|-----------|---------|
| [Campg 1] | [tool] | Sending | 12% | 3 |
| [Campg 2] | [tool] | Drafting | - | - |

WORK LOG (Last 7 days)
| Date | Task | Goal | Accomplished | Time |
|------|------|------|---------------|------|
| Aug 5 | [Task] | [Goal] | [Done] | 45 min |
| Aug 4 | [Task] | [Goal] | [Done] | 60 min |

MEETINGS & SUMMARIES
- Next meeting: [Date & time, if scheduled]
- Last meeting: [Link to summary]
- [Earlier meeting]: [Link]

[Back to Dashboard]
```

---

### View 4: Campaign Performance

**When Eikko clicks on a campaign, they see:**

```
CAMPAIGN DETAILS: [Campaign Name]

BASIC INFO
- Client: [Client]
- Tool: [Hubspot/Lemlist/PlusVibe/etc]
- Date started: [Date]
- Target: [# contacts]

CURRENT METRICS
- Sent: [#]
- Opens: [#] ([%])
- Clicks: [#] ([%])
- Replies: [#] ([%])
- Bounces: [#]
- Status: [Drafting/Sending/In-progress/Completed]

TREND (if applicable)
Day 1: [Opens: X, Clicks: Y, Replies: Z]
Day 2: [Opens: X, Clicks: Y, Replies: Z]
Day 3: [Opens: X, Clicks: Y, Replies: Z]

NEXT STEPS
- [Action 1]
- [Action 2]

NOTES
[Any special notes about this campaign]

[Back to Client] [Back to Dashboard]
```

---

### View 5: Meetings & Summaries

**When Eikko clicks on a meeting link or views meeting section:**

```
MEETING SUMMARY: [Client] — [Date & Time]

ATTENDEES: [Names]
DURATION: [Minutes]
PLATFORM: [Zoom/Google Meet/Phone/etc]

SUMMARY
[2-3 sentences of what was discussed]

ACTION ITEMS
- [ ] [Action] — Owner: [Name] — Due: [Date]
- [ ] [Action] — Owner: [Name] — Due: [Date]

KEY DECISIONS
- [Decision 1]
- [Decision 2]

QUESTIONS & ANSWERS
- Q: [Question]
  A: [Answer]

BLOCKERS
- [Blocker 1]
- [Blocker 2]

FOLLOW-UP
- Next meeting: [Date & time, if scheduled]
- Tasks pending: [List]

[Back to Client] [Back to Dashboard]
```

---

### View 6: Task Deadline Tracker

**Optional overview of all pending tasks across clients:**

```
TASK DEADLINES

DUE TODAY
- [Task for Chris Caffera] — Chris
- [Task for Yoni] — Yoni

DUE THIS WEEK
- [Task for Chris Drew] — Chris (Due: Wed)
- [Task for Krishna] — Krishna (Due: Fri)

OVERDUE
- [Task for Chris Caffera] — Chris (Due: Aug 3)

[Clients menu] [Refresh] [Add Task]
```

---

## Data Schema (What the App Stores)

```
CLIENTS
├── Name
├── Email
├── WhatsApp
├── Timezone
├── Rate/Contract
├── Role
├── Status (Active/Paused)
├── Working hours
└── Projects (array)

PROJECTS (per client)
├── Name
├── Description
├── Status
├── Tools used
└── Key contacts

WORK LOG ENTRIES
├── Client
├── Date
├── Task
├── Goal
├── Accomplishment
├── Time spent
└── Status (Completed/Pending)

CAMPAIGNS (per client)
├── Name
├── Tool
├── Date started
├── Target contacts
├── Status
├── Metrics (sent, open rate, click rate, reply rate, bounces)
└── Trend (daily data if tracked)

MESSAGES (per client)
├── Date
├── Source (Email/WhatsApp/Slack)
├── Summary
├── Action required? (Yes/No)
└── Timestamp

MEETINGS (per client)
├── Date & time
├── Attendees
├── Platform
├── Summary
├── Action items (array)
├── Key decisions (array)
└── Transcript link (if available)

TASKS/REMINDERS
├── Client
├── Task
├── Due date
├── Owner
└── Status (Pending/Completed)
```

---

## How Data Flows

```
1. MORNING: Eikko opens app
   ↓
2. APP LOADS: Shows yesterday's recap
   (pulled from work logs, campaign metrics, messages, meetings)
   ↓
3. EIKKO REVIEWS: Recap, upcoming tasks, client details
   ↓
4. WORK STARTS: Eikko logs "Working on X → Goal: Y"
   (app records start time)
   ↓
5. WORK ENDS: Eikko logs "Accomplished Z"
   (app calculates time spent, saves entry)
   ↓
6. WORK LOG ENTRY SAVED
   ↓
7. NEXT MORNING: New recap generated from yesterday's logs
```

---

## Implementation Notes

### Data Capture
- **Manual entry:** Work logs, meeting summaries, task notes
- **Auto-capture:** Campaign metrics (if APIs connected), meeting times (if calendar connected), TimeDoctors hours (Yoni)
- **Hybrid:** Message counts pulled from platforms, summaries written by Eikko

### Display Format
- **Text-based only** — no charts, images, or heavy visualizations
- **Tables and lists** for easy scanning
- **Clean layout:** One client view at a time, navigation back to dashboard

### Storage
- Data stored as JSON or similar simple format (not database)
- Can be exported to CSV for backup
- Can be integrated with external tools later (Notion, Airtable, etc.)

### Timezone Handling
- Display times in Eikko's local timezone (PHT)
- Show Yoni's 9pm-5am PHT hours clearly
- Display client timezones for scheduling awareness

---

## Features to Build First (MVP)

**Phase 1 (Essential):**
1. Yesterday's recap view
2. Work logger (start → stop → log accomplishment)
3. Client details view
4. Basic campaign metrics view

**Phase 2 (Nice to have):**
5. Meeting summaries storage
6. Task deadline tracker
7. Message check tracking
8. Trend analysis (multi-day campaign metrics)

**Phase 3 (Future):**
9. API integration for auto-metric pulling
10. Calendar sync for meetings
11. Export/backup features
12. Mobile version

---

## Questions for Eikko

1. Should the app store data locally (browser) or sync to a cloud file?
2. How often should campaign metrics update? (Manual pull or automatic?)
3. Should messages show count only or actual message text?
4. Do you want task reminders/notifications, or just the dashboard view?
5. Any preferred color scheme or styling? (Or keep it minimal?)

---

**Status:** Spec written. Ready for HTML/app development.

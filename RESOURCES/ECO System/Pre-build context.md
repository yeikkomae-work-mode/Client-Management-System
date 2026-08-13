# Client Management System — Pre-build Context

## Project Overview
Personal client management system for Eikko Ybanez handling 5 active clients (3 full-time, 2 part-time) across multiple outbound sales workflows. System provides centralized tracking of daily tasks, missed communications, campaign metrics, meetings, and work logging.

---

## Client Portfolio

### Full-Time Clients (Weekdays)

#### 1. Chris Caffera — Personal Assistant
- **Role:** ICP builder, lead generation, CRM manager, campaign creator, LinkedIn manager
- **Tools:** Apollo, Hubspot, Lemlist, MillionVerifier, LinkedIn
- **Key tasks (daily):**
  - Check: emails, Outlook, Slack, WhatsApp (Chris + Fatin)
  - Create/update task list
  - Schedule LinkedIn posts (Chris & Fatin)
  - Monitor Hubspot & Lemlist campaigns
- **Sub-client:** Fatin (same workflow)
- **Meetings:** Monday 10am + ad-hoc during week
- **Communication:** Email, Slack, WhatsApp, in-person meetings
- **Working hours:** Weekdays (timezone TBD)

#### 2. Chris Drew — Lead Gen Specialist @ Satlas
- **Role:** Lead generation, campaign setup, email sequences, data enrichment
- **Tools:** Apollo, Instantly, Zapmail, Inboxkit, PlusVibe, Notion, MillionVerifier
- **Key tasks (daily):**
  - Check: emails, WhatsApp for updates
  - Monitor PlusVibe campaigns & inbox health
  - Record campaign data
- **Meetings:** As-needed (urgent only)
- **Communication:** WhatsApp group chat
- **Working hours:** Weekdays

#### 3. Yoni Lebovits — Outreach Specialist @ albertscott
- **Role:** Outreach campaign manager, prospect tagger, CRM updater
- **Tools:** Smartlead, Pipedrive, TimeDoctors
- **Key tasks (daily):**
  - Check: emails, WhatsApp for updates
  - Open Smartlead: tag prospects based on replies
  - Open Pipedrive: add tagged prospects, follow-up
  - Check emails for Calendly bookings → add to Pipedrive → add to Smartlead blocklist
- **Workflow detail:** Smartlead has built-in tagging rules; follow those for prospect classification and Pipedrive routing
- **Time tracking:** TimeDoctors logs hours (9pm-3/4am PHT, 5 hours/day, break 11pm-12am)
- **Communication:** WhatsApp
- **Working hours:** Weekdays only, 9pm-5am PHT (with 1hr break)

### Part-Time Clients

#### 1. Krishna Nainani — 3 hours/week
- **Role:** Lead generation
- **Tools:** Apollo
- **Key tasks:**
  - Build ICP, create email sequences, create campaigns
- **Meetings:** Rare
- **Communication:** WhatsApp

#### 2. Chris Soriano — As-needed
- **Role:** Data entry specialist, researcher
- **Tools:** Google search, spreadsheet
- **Key tasks:**
  - List building: search for brands, contact emails, social links for movie production
- **Meetings:** None
- **Communication:** WhatsApp
- **Task frequency:** Sporadic, not regular

---

## Daily Workflow by Client

### Chris Caffera
```
1. Check messages (emails, Outlook, Slack, WhatsApp from Chris & Fatin)
2. Review/update task list
3. Schedule LinkedIn posts
4. Monitor Hubspot campaign performance
5. Monitor Lemlist campaign performance & sequences
6. Handle ad-hoc tasks
```

### Chris Drew
```
1. Check emails & WhatsApp updates
2. Monitor PlusVibe campaigns
3. Check PlusVibe inbox health
4. Record data from tools
```

### Yoni
```
1. Check emails & WhatsApp for updates
2. Open Smartlead → tag prospects per workflow rules
3. Open Pipedrive → move tagged prospects, log follow-ups
4. Check emails for Calendly bookings → add to Pipedrive & Smartlead blocklist
```

### Krishna
```
(3x per week, not daily)
1. Build/refine ICP
2. Run Apollo searches
3. Create or manage sequences
```

### Chris Soriano
```
(As requested)
1. Google search for brands/contacts
2. Compile list in spreadsheet
3. Share with Chris
```

---

## Recap Data (Yesterday's Work)

**What to capture per client:**
- Tasks completed
- Missed messages while sleeping (with context)
- Client reminders/updates
- Campaign metrics (open rate, reply rate, clicked, bounced, etc. — varies by client's tools)
- Meeting summaries (if meeting occurred: transcript → summary, action items, discussion points)
- Work logged: time spent, what was accomplished

**Format:** Bullet list by client

**Campaign metrics importance:** High — these drive decision-making for all clients

---

## Work Logging

### Current state
- **Chris Caffera & Chris Drew:** No logging tool; manual required
- **Yoni:** Uses TimeDoctors (auto-tracked)
- **Krishna & Chris Soriano:** Minimal logging needed

### Desired feature
App should include: "Currently working on [client] — my goal: [description]" → work → "Done — what I accomplished: [description]"

This replaces manual time/task logging for all clients.

---

## Meeting Handling

**When a meeting occurs:**
- Request transcript (if available)
- Summarize: key points discussed
- Extract: action items (who, what, by when)
- Store: meeting summary in system for future reference

**Clients with regular meetings:**
- Chris Caffera: Monday 10am + ad-hoc

**Clients with on-demand meetings:**
- Yoni: during working hours as needed
- Others: rare

---

## Tools Summary

| Tool | Client(s) | Purpose |
|------|-----------|---------|
| Apollo | Chris Caffera, Chris Drew, Krishna | Lead generation, ICP building |
| Hubspot | Chris Caffera | CRM, campaign management |
| Lemlist | Chris Caffera | Email campaigns, sequences |
| MillionVerifier | Chris Caffera, Chris Drew | Data enrichment |
| LinkedIn | Chris Caffera | Post scheduling, engagement |
| Instantly | Chris Drew | Email outreach |
| Zapmail | Chris Drew | Email outreach |
| Inboxkit | Chris Drew | Inbox management |
| PlusVibe | Chris Drew | Campaign management, inbox health |
| Notion | Chris Drew | Campaign tracking |
| Smartlead | Yoni | Prospect tagging, outreach |
| Pipedrive | Yoni | CRM, prospect management |
| TimeDoctors | Yoni | Time tracking |
| Google Search | Chris Soriano | List building |
| Spreadsheet | Chris Soriano | Data compilation |
| Email | All | Communication |
| WhatsApp | All | Communication |

---

## Blindspots to Address

1. **WhatsApp message piling up** — No centralized view; messages scattered
2. **Calendar conflicts** — Need to see all meetings in one place
3. **Task deadlines slipping** — No unified task deadline tracker
4. **Campaign performance tracking** — Metrics spread across different tools per client

---

## Tools Per Step (Build-out Mapping)

### Automation (Daily Routine)
| Step | Tools | Who Runs It |
|------|-------|------------|
| Check messages (emails, Slack, WhatsApp) | Email client, Slack, WhatsApp, manual check | Claude + User |
| Review/create task list | Task log in app | User input |
| Monitor campaign performance | PlusVibe API (Chris Drew), Hubspot API (Chris Caffera), Pipedrive API (Yoni) | Claude (data pull) |
| Log work in progress | App work logger | User input |
| Generate yesterday's recap | App data aggregation | Claude (compile from logs) |

### Plugin (Reusable Templates)
| Component | Purpose | Who Builds |
|-----------|---------|-----------|
| Client onboarding template | Capture contact, rate, timezone, tools, role for new clients | Claude + User |
| Daily task checklist template | Recurring task framework for any client | Claude |
| Meeting transcript → summary | Converts meeting notes to structured format | Claude |
| Campaign metrics template | Flexible metric tracking per tool type | Claude + User |

### App (Dashboard & Work Logger)
| Feature | Data Source | Who Updates |
|---------|-------------|------------|
| Yesterday's recap view | User work logs + API pulls | Claude aggregates |
| Current work logger | User input (goal → accomplishment) | User input |
| Meeting summary storage | User uploads transcript | Claude processes |
| Upcoming meetings | Calendar API (if connected) | Auto-sync or user input |
| Task deadline tracker | User input or API sync | User input + automatic |
| Campaign performance snapshot | API pulls from tools | Claude queries APIs |

---

## Human vs Claude Per Step

### Chris Caffera Workflow
- **LinkedIn post scheduling:** User decision (creative/timing) → Claude helps schedule
- **ICP building:** User judgment (market knowledge) → Claude assists with research
- **Campaign sequence creation:** User writes copy → Claude structures/optimizes
- **Task prioritization:** User decides what's urgent → Claude tracks deadlines
- **Meeting decisions:** User makes choices → Claude takes notes/summarizes

### Chris Drew Workflow
- **Campaign setup:** User specifies → Claude structures in Notion
- **Email copy review:** User approves copy → Claude formats/sequences
- **Inbox health interpretation:** User assesses what's healthy → Claude logs metrics
- **Data recording:** User provides data → Claude organizes

### Yoni Workflow
- **Prospect tagging rules:** Smartlead rules are set (automated) → Claude tracks results
- **Pipedrive updates:** User reviews Smartlead tags → Claude assists with bulk moves
- **Calendly integration:** User reviews bookings → Claude logs to Pipedrive
- **Time tracking:** TimeDoctors auto-logs → Claude compiles into recap

### General
- **Meeting transcription:** Platform provides transcript → Claude summarizes
- **Task logging:** User logs work → Claude aggregates into recap
- **Campaign metrics:** APIs pull data → Claude interprets trends

---

## Questions for Eikko

(To be answered during project build if details emerge)

1. Are there other projects/clients not mentioned that should be added?
2. Should the app pull directly from APIs (Hubspot, Pipedrive, PlusVibe) or rely on manual metric logging?
3. For meeting transcripts, which platform will provide them? (Calendly, Google Meet, Zoom, other?)
4. Should the app have a mobile component, or desktop-only?
5. Any other tools or workflows used that we missed?

---

## Next Steps

1. Confirm this context is complete and accurate
2. Build out the 3 component folders (Automation, Plugin, App)
3. Create specs for each piece
4. Start development on daily automation

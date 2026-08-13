# Data Schema — App Data Structure

**How the app stores and organizes data.**

---

## OVERVIEW

The app stores data locally in your browser using JSON format. No database, no server — just simple data structures stored on your device.

---

## DATA STRUCTURE

### Work Logs

**What it is:** List of tasks you've logged using the Work Logger.

**Structure:**
```json
{
  "workLogs": [
    {
      "id": 1691404800000,
      "date": "8/7/2026, 2:45:32 PM",
      "client": "Yoni",
      "task": "Smartlead tagging and Pipedrive updates",
      "goal": "Process 30 new replies, move interested to Pipedrive",
      "accomplishment": "Tagged 28 replies, moved 20 to Pipedrive, added 8 to blocklist",
      "timeSpent": "80 min"
    },
    {
      "id": 1691401200000,
      "date": "8/7/2026, 1:30:15 PM",
      "client": "Chris Caffera",
      "task": "Check messages and emails",
      "goal": "Review any urgent updates from Chris or Fatin",
      "accomplishment": "Found 3 messages from Chris, 1 urgent new LinkedIn post request",
      "timeSpent": "20 min"
    }
  ]
}
```

**Fields:**
- `id` — Unique timestamp (used for deleting entries)
- `date` — When the task was logged
- `client` — Which client (Chris Caffera, Chris Drew, Yoni, Krishna, Chris Soriano)
- `task` — What you worked on
- `goal` — What you aimed to accomplish
- `accomplishment` — What you actually got done
- `timeSpent` — How long it took

---

### Recap Data

**What it is:** Yesterday's compiled recap (tasks, metrics, notes per client).

**Structure:**
```json
{
  "recapData": {
    "date": "August 6, 2026",
    "clients": {
      "Chris Caffera": {
        "tasks": [
          "Checked emails and Slack from Chris and Fatin",
          "Reviewed Hubspot campaign performance",
          "Scheduled 2 LinkedIn posts for tomorrow",
          "Updated Lemlist sequence"
        ],
        "missedMessages": "2 messages from Chris (not urgent)",
        "metrics": {
          "hubspot_open_rate": "12%",
          "hubspot_replies": 8,
          "hubspot_bounces": 2,
          "lemlist_open_rate": "8%",
          "lemlist_clicks": 3,
          "lemlist_bounces": 0,
          "linkedin_posts_scheduled": 2,
          "linkedin_engagements": 15
        },
        "notes": "Chris wants to test new subject line tomorrow. Fatin's post performing well (23 impressions)."
      },
      "Chris Drew": {
        "tasks": [
          "Checked emails and WhatsApp for updates",
          "Monitored PlusVibe campaigns and inbox health",
          "Recorded data"
        ],
        "missedMessages": "None",
        "metrics": {
          "plusvibe_inbox_health": "89%",
          "plusvibe_campaign_opens": 156,
          "plusvibe_campaign_clicks": 12
        },
        "notes": "All campaigns performing well"
      },
      "Yoni": {
        "tasks": [
          "Tagged 28 prospects in Smartlead",
          "Moved 20 interested to Pipedrive",
          "Added 8 uninterested to blocklist",
          "Processed 2 Calendly bookings"
        ],
        "missedMessages": "1 message (follow-up on warm lead)",
        "metrics": {
          "smartlead_tagged": 28,
          "smartlead_interested": 20,
          "pipedrive_added": 20,
          "blocklist_additions": 8,
          "calendly_bookings": 2,
          "hours_logged": 5
        },
        "notes": "Strong engagement on latest sequence. Follow up on 3 warm leads tomorrow."
      }
    }
  }
}
```

**Structure:**
- `date` — Date of the recap
- `clients` — Object with each client as key
  - `tasks` — Array of tasks completed
  - `missedMessages` — Summary of messages missed while sleeping
  - `metrics` — Key metrics from various tools
  - `notes` — Important notes, blockers, follow-ups

---

### Clients

**What it is:** Contact info and details for all 5 clients.

**Structure:**
```json
{
  "clients": {
    "Chris Caffera": {
      "email": "chris@example.com",
      "whatsapp": "Link or number",
      "timezone": "EST",
      "role": "Personal Assistant",
      "tools": ["Apollo", "Hubspot", "Lemlist", "MillionVerifier", "LinkedIn"],
      "meetings": "Monday 10am + ad-hoc",
      "status": "Active"
    },
    "Chris Drew": {
      "email": "chris.drew@satlas.com",
      "whatsapp": "Group chat link",
      "timezone": "EST",
      "role": "Lead Gen Specialist",
      "tools": ["Apollo", "Instantly", "Zapmail", "Inboxkit", "PlusVibe", "Notion", "MillionVerifier"],
      "meetings": "As-needed",
      "status": "Active"
    },
    "Yoni": {
      "email": "yoni@albertscott.com",
      "whatsapp": "Number",
      "timezone": "PHT",
      "role": "Outreach Specialist",
      "tools": ["Smartlead", "Pipedrive", "TimeDoctors"],
      "meetings": "During working hours",
      "status": "Active"
    }
  }
}
```

**Fields per client:**
- `email` — Client email
- `whatsapp` — WhatsApp contact
- `timezone` — Client timezone
- `role` — Your role with this client
- `tools` — Tools you use for this client
- `meetings` — Meeting schedule
- `status` — Active, On hold, Completed

---

### Campaigns

**What it is:** Tracking data for all active campaigns.

**Structure:**
```json
{
  "campaigns": {
    "hubspot-summer-launch": {
      "client": "Chris Caffera",
      "name": "Summer Product Launch",
      "tool": "Hubspot",
      "status": "In-progress",
      "dateStarted": "2026-08-01",
      "target": 500,
      "sent": 450,
      "openRate": "12%",
      "clickRate": "3%",
      "replyRate": "8%",
      "bounces": 2,
      "conversions": 12,
      "notes": "Strong performance, on track"
    },
    "lemlist-welcome": {
      "client": "Chris Caffera",
      "name": "Welcome Series",
      "tool": "Lemlist",
      "status": "Active",
      "dateStarted": "2026-07-15",
      "target": 1000,
      "sent": 945,
      "openRate": "8%",
      "clickRate": "2%",
      "replyRate": "5%",
      "bounces": 1,
      "conversions": 5,
      "notes": "Testing new subject lines"
    },
    "smartlead-outreach-wave-1": {
      "client": "Yoni",
      "name": "Outreach Wave 1",
      "tool": "Smartlead",
      "status": "In-progress",
      "dateStarted": "2026-07-20",
      "target": 200,
      "sent": 200,
      "openRate": "35%",
      "clickRate": "8%",
      "replyRate": "12%",
      "bounces": 0,
      "conversions": 8,
      "notes": "High engagement, very positive"
    }
  }
}
```

**Fields per campaign:**
- `client` — Which client
- `name` — Campaign name
- `tool` — Which tool (Hubspot, Lemlist, PlusVibe, Smartlead, etc.)
- `status` — Drafting, Sending, In-progress, Completed, Paused
- `dateStarted` — Launch date
- `target` — Goal (# contacts, $ revenue)
- `sent` — Number sent
- `openRate` — % or count
- `clickRate` — % or count
- `replyRate` — % or count
- `bounces` — Count
- `conversions` — Count or %
- `notes` — Any notes about campaign

---

## HOW DATA FLOWS

### Work Logger Entry

```
1. User logs task in app (client, task, goal, accomplishment, time)
   ↓
2. App saves to localStorage.workLogs
   ↓
3. Entry appears in Work Logger view immediately
   ↓
4. When user says "done for today", I compile work logs + metrics
   ↓
5. Next "good morning", I use work logs to generate recap
```

### Recap Generation

```
1. User says "good morning"
   ↓
2. I pull API data (Smartlead, Pipedrive, TimeDoctors)
   ↓
3. I fetch yesterday's manual metrics (user provided "done for today")
   ↓
4. I compile work logs from app (app.workLogs)
   ↓
5. I create recap JSON with all client data
   ↓
6. I call app.updateRecap(recapDataObj)
   ↓
7. App saves to localStorage.recapData
   ↓
8. Recap view displays the data
```

### Campaign Tracking

```
1. User logs campaign metrics (end of day or via chat)
   ↓
2. I save to campaigns object
   ↓
3. I call app.updateCampaigns(campaignsObj)
   ↓
4. App saves to localStorage.campaigns
   ↓
5. Campaigns view displays all active campaigns
```

---

## DATA STORAGE LIMITS

**Browser localStorage limit:**
- Typically 5-10 MB per website
- At ~500 bytes per work log entry, you can store ~10,000+ entries
- Should last you a year+ easily

**Backup when:**
- Once a month, export data (Settings → Export)
- After major updates to workflows
- Before trying experimental features

**How to backup:**
1. Go to Settings tab
2. Click "Export All Data as JSON"
3. Save the file somewhere safe (Desktop, cloud, etc.)

---

## ADDING NEW DATA PROGRAMMATICALLY

### From Chat/External

When I need to update app data from chat, I call JavaScript functions:

```javascript
// Update recap
updateRecap({
  date: "August 7, 2026",
  clients: { ... }
});

// Update clients
updateClients({
  "Chris Caffera": { ... },
  "Chris Drew": { ... }
});

// Update campaigns
updateCampaigns({
  "campaign-id": { ... }
});
```

These functions save data to localStorage and update the app views.

---

## EXPORTING DATA

**What gets exported:**
- All work logs (everything you logged)
- Recap data (yesterday's summaries)
- Clients info (contact details)
- Campaigns (performance tracking)
- Export timestamp

**Export format:**
```json
{
  "workLogs": [...],
  "recapData": {...},
  "clients": {...},
  "campaigns": {...},
  "exportDate": "2026-08-07T14:30:00.000Z"
}
```

**Use for:**
- Backup
- Analysis (import into Excel, etc.)
- Sharing with team (if needed later)
- Historical reference

---

## PRIVACY

**All data is local:**
- Stored in your browser only
- Not sent to any server
- Not tracked or analyzed
- You can delete anytime

**Access:**
- Only you (whoever has access to your browser)
- Data persists across sessions
- Survives browser restarts

**Security:**
- As secure as your device
- If someone has access to your computer/browser, they can see the data
- Clear cache to remove data completely

---

## EXTENDING DATA

If you want to add custom fields later (e.g., billing notes, client preferences), the data structure can be extended:

```json
{
  "id": 1234567890,
  "date": "8/7/2026",
  "client": "Chris Caffera",
  "task": "...",
  "goal": "...",
  "accomplishment": "...",
  "timeSpent": "60 min",
  "billing": "Bill Chris - 1 hour @ $X/hr",  // New field
  "invoiced": false,                          // New field
  "project": "Project ABC",                   // New field
  "priority": "high"                          // New field
}
```

Just let me know what you want to track and I can update the app.

---

**This is your data. You own it. You control it.**

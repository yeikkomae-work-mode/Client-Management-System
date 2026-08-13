# ECO — API Authentication Checklist
**Get full live data access. Do these in order.**

---

## What ECO Can Do Right Now ✅

- ✅ Route commands (good morning, /comms, client review [name], etc.)
- ✅ Deliver formatted responses
- ✅ Orchestrate agents
- ✅ Work with pre-loaded file data

## What ECO Needs to Do More ⏳

- ⏳ Pull live Gmail data (COMMS agent)
- ⏳ Pull live Google Calendar + Tasks (OPS agent)
- ⏳ Pull live Apollo data (CLIENTS + METRICS agents)
- ⏳ Pull live Hubspot data (CLIENTS + METRICS agents)
- ⏳ Pull live Smartlead + Pipedrive data (CLIENTS agent — Yoni)

---

## Authentication Priority Order

### TIER 1 — CRITICAL (Do These First)

These give you the most immediate value:

#### 1. Google Gmail (COMMS)
**Why:** Email is your most time-sensitive communications channel

**How to Authenticate in Claude Code:**
```bash
claude mcp
```
Then select: `gmail` → Follow OAuth flow → Approve access

**What it unlocks:**
- `/comms` — Check new important emails
- Email drafts in your voice
- Follow-up tracking

**Time to activate:** 2 minutes

---

#### 2. Google Calendar + Tasks (OPS)
**Why:** Your daily schedule and task priorities

**How to Authenticate in Claude Code:**
```bash
claude mcp
```
Then select: `google_calendar` and `google_tasks` → Follow OAuth flow → Approve access

**What it unlocks:**
- `good morning` — Today's calendar + tasks
- `done for today` — Evening wrap-up
- Meeting reminders 15 min before sessions
- `/ops` — Quick calendar/task check

**Time to activate:** 2 minutes

---

#### 3. Apollo (CLIENTS + METRICS)
**Why:** Chris Drew's cold email campaigns + Krishna's Peru campaign

**How to Authenticate in Claude Code:**
```bash
claude mcp
```
Then select: `apollo` → Enter your Apollo API key → Authorize

**Your Apollo API Key:** You said you already authenticated via terminal. Get it from:
```bash
claude mcp --show-config apollo
```

**What it unlocks:**
- `client review chris drew` — Live campaign metrics (opens, replies, bounces)
- `client review krishna` — Peru Silver Chain Wholesalers live tracking
- `/metrics` — Campaign performance data

**Time to activate:** 1 minute (key already exists)

---

### TIER 2 — HIGH PRIORITY (Do After Tier 1)

#### 4. Hubspot (CLIENTS + METRICS)
**Why:** Chris Caffera's campaign tracking + lead management

**How to Authenticate in Claude Code:**
```bash
claude mcp
```
Then select: `hubspot` → Enter your Hubspot API key

**Your Hubspot API Key:** If you already authenticated via terminal:
```bash
claude mcp --show-config hubspot
```

**What it unlocks:**
- `client review chris caffera` — Live Hubspot campaign metrics
- `/metrics` — Email performance data

**Time to activate:** 1 minute

---

#### 5. Smartlead + Pipedrive (CLIENTS)
**Why:** Yoni's lead generation and prospect tracking

**How to Authenticate in Claude Code:**
```bash
claude mcp
```
Then select: `smartlead` and `pipedrive` → Enter API keys for each

**Your API Keys:** If authenticated via terminal:
```bash
claude mcp --show-config smartlead
claude mcp --show-config pipedrive
```

**What it unlocks:**
- `client review yoni` — Live lead count + prospect pipeline
- Campaign metrics from Smartlead

**Time to activate:** 2 minutes total

---

## Quick Authentication Flow

### For Each Tool:

1. **Open terminal:**
   ```bash
   claude mcp
   ```

2. **Select the tool** (Gmail, Calendar, Apollo, Hubspot, Smartlead, Pipedrive)

3. **Follow the prompt:**
   - If OAuth: Browser opens → Click "Approve" → Done
   - If API Key: Paste your key → Done

4. **Verify it worked:**
   ```bash
   claude mcp --list
   ```
   You should see checkmark (✅) next to authenticated tools

---

## Do It Now — Quick Checklist

```
TIER 1 (CRITICAL):
[ ] Gmail authentication (COMMS)
    Command: claude mcp → gmail → Approve OAuth
    
[ ] Google Calendar + Tasks (OPS)
    Command: claude mcp → google_calendar & google_tasks → Approve OAuth
    
[ ] Apollo (CLIENTS + METRICS)
    Command: claude mcp → apollo → Paste API key
    
TIER 2 (HIGH PRIORITY):
[ ] Hubspot (CLIENTS + METRICS)
    Command: claude mcp → hubspot → Paste API key
    
[ ] Smartlead (CLIENTS)
    Command: claude mcp → smartlead → Paste API key
    
[ ] Pipedrive (CLIENTS)
    Command: claude mcp → pipedrive → Paste API key
```

---

## Test After Each Authentication

After you authenticate a tool, test it:

```bash
claude chat eco
```

Then:
```
good morning
```

**If you see live data** (actual calendar events, tasks, emails) → That tool is working.

**If you see "awaiting authentication"** → Re-run `claude mcp` and try again.

---

## Status Tracking

| Tool | Service | Status | Command |
|------|---------|--------|---------|
| Gmail | Google | ⏳ Pending | `claude mcp → gmail` |
| Calendar | Google | ⏳ Pending | `claude mcp → google_calendar` |
| Tasks | Google | ⏳ Pending | `claude mcp → google_tasks` |
| Apollo | Apollo | ⏳ Pending | `claude mcp → apollo` |
| Hubspot | Hubspot | ⏳ Pending | `claude mcp → hubspot` |
| Smartlead | Smartlead | ⏳ Pending | `claude mcp → smartlead` |
| Pipedrive | Pipedrive | ⏳ Pending | `claude mcp → pipedrive` |

---

## Once All Are Authenticated

ECO will deliver:

```
good morning
→ Live calendar + tasks + important emails + what needs decision

done for today
→ Live: still open emails, tasks, tomorrow's first meeting

client review yoni
→ Live: Smartlead lead count + Pipedrive pipeline stage

client review chris caffera
→ Live: Hubspot campaign metrics + email performance

client review chris drew
→ Live: Apollo campaign opens/replies/bounces + Peru campaign

/metrics
→ Live: Campaign metrics + income/expenses/profit per client
```

---

## Next Step Right Now

1. **In terminal, run:**
   ```bash
   claude mcp
   ```

2. **Authenticate Gmail first** (most immediate value)

3. **Then Calendar + Tasks**

4. **Then Apollo, Hubspot, Smartlead, Pipedrive**

5. **After each, test:**
   ```bash
   claude chat eco
   good morning
   ```

6. **Tell me when all are authenticated** — ECO will be fully live.

---

**Time to full activation:** ~10 minutes (2 min per tool × 5 tools)

**Once done:** ECO pulls live data from all 5 clients across all tools. No more waiting.

Ready to authenticate?

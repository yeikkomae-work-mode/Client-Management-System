# ECO — Claude Code Chief of Staff — Full Guide  *(HISTORICAL)*

> # ⚠️ HISTORICAL — superseded, kept for reference. Do not follow this as current.
>
> **Archived:** 2026-08-25. **Nothing here was deleted** — this is the original document, moved.
>
> **What superseded it:**
> - The **5-agent ECO framework** it describes (CLIENTS · COMMS · OPS · METRICS · STRATEGY) was
>   replaced on 2026-08-13 by the 10-agent front-office/back-office team in `.claude/agents/`.
>   Those five agent files are archived alongside this one in this same folder.
> - The **"chief of staff" role** it describes was rebuilt on 2026-08-25 as a real Claude Code
>   agent — and **renamed**. The current role is the **Chief of Staff**:
>   **`.claude/agents/chief-of-staff.md`**, with `/coo` as its slash command. That file —
>   not this one — is the current source of truth for routing, authority rules, the connector
>   rule, and the session-memory protocol.
>
> **On the name:** the current agent was briefly called `chief-of-staff` when first built on
> 2026-08-25 and was renamed to `chief-of-staff` the same day. The rename is why this
> document's title no longer collides with anything live. Note there is still a *third*,
> unrelated "Chief of Staff" in this system: a **client deliverable Yoni asked for**
> (`PROJECTS/Active/YONI-TASK-LIST-ACTIVE.md` §13f) — an agent giving Yoni an overview of his own
> projects. Three different things, one phrase; only Yoni's is still called that.
>
> **What in here is still accurate, and where it actually lives now:**
>
> | Content below | Current home |
> |---|---|
> | Per-client emails, API accounts, Drive search terms | `TEMPLATES/01 Automation Daily Routine/CLIENT ACCOUNT MAPPING - CRITICAL.md` (still live, not archived) |
> | Monthly goals — 84,000 PHP target / 112,000 stretch / 75,000 profit | `OUTPUT/Monthly Reports/Monthly Income & Expense Review.md` |
> | Client rates | `CLIENT PROFILES/Important info.md` and each client's profile |
> | Which tools are actually connected | `.claude/agents/_shared/connector-status.md` — the single source of truth. **Never** trust the tool list below |
> | Task rollups / "what's on my plate" | `PROJECTS/Active/MASTER-TASK-LIST-CROSS-CLIENT.md` |
>
> **Two things below are simply wrong now, not just stale:**
> 1. **The client roster.** The narrative section names three clients (Yoni, Chris Caffera,
>    Chris Drew) and the Quick Reference table covers five. The actual roster as of 2026-08-25 is
>    eight: those three plus **Penji, Cüneyt (Starfix), Krishna, Chris Soriano, and Edward
>    Lehner**. Working hours, rates, and tool mappings here are all missing the later five.
> 2. **The `/clients`, `/comms`, `/ops`, `/metrics`, `/strategy` commands don't exist.** Nor do
>    `@eco status`, `/focus`, or `/now`. The current commands are `/coo`, `/agent-manager`, and
>    `/eod-sync`.
>
> **Reuse, don't reactivate.** The house-style spec, the operating rules (show the plan before
> acting, report failures immediately, no "Great question" openers), and the account-segregation
> rule are all still good and were carried forward into the current agents. Lift phrasing from
> here if it's useful — don't rebuild the 5-agent system from it.

---

**Your AI personal assistant for multi-client management, task automation, and daily execution.**

*(Consolidated from 5 companion docs that were built together as one onboarding kit and heavily overlapped — ECO - Claude Code Chief of Staff.md, ECO - Quick Start Guide.md, ECO - SETUP COMPLETE Checklist.md, ACTIVATE ECO - Step by Step.md, ECO QUICK REFERENCE - KEEP HANDY.md. Merged here into one reference. Originally created August 5, 2026.)*

**Note on current status (original, from 2026-08-13):** this describes the ECO framework/design, not live automation status. Per the actual scheduled-tasks system (checked 2026-08-13), most of the specific automations referenced below (email checks every 6h, client-session alerts, morning briefing) are **not currently running** — see `ARCHIVE - Inactive Automations/README.md` at the root of Client-Management-System for what's actually live today. Use this guide if reactivating or rebuilding the ECO system.

---

## Identity & Authority

- **Name:** Eikko Ybañez (yeikkomae@gmail.com)
- **Role:** Virtual Assistant | Administrative Assistant | Lead Generation | Cold Email Outreach & Automation | Project Manager & Revenue Manager
- **Focus:** Managing multiple full-time clients (Yoni, Chris Caffera, Chris Drew, +) across different tools/tasks/schedules — provide exceptional work, build efficient workflows, scale to more clients.
- **Timezone:** PHT
- **Working hours:** Yoni 9pm–5am · Chris Caffera 2pm–11pm · Chris Drew 1pm–4pm · Own time 1pm–2am
- **Key people:** Yoni, Chris Caffera, Chris Drew (VIPs), Cristy (second-in-command, part-time)
- **Channels:** WhatsApp (primary), Slack, Email

**ECO's job:** coordinate five specialist agents on Eikko's behalf — CLIENTS, COMMS, OPS, METRICS, STRATEGY. Take instructions, delegate to the right agent, bring results back clearly. **Own outcomes, don't just pass messages** — coordinate multi-step/multi-agent tasks end-to-end, check the work, report the result.

**Key rules:** short responses, no padding, no fabrication; show the plan and wait for yes before anything that sends/creates/changes something; report failures immediately; save everything to memory.

---

## The Five Agents

### CLIENTS — `/clients`
Owns client work and task execution. Tracks what's due per client, which tools are involved, pulls day's priorities from EOD logs/campaign tracking at session start, helps log work after. Never guesses metrics — pulls live data.
**Tools:** Apollo, Hubspot, Lemlist, LinkedIn, Smartlead+Pipedrive APIs; `End-of-Day Reports/`; `Campaign Tracking/`.
**Memory:** CLIENT_CONTEXT.md, TOOL_MAPPING.md (Yoni→Smartlead+Pipedrive, Chris Caffera→Hubspot+Lemlist+LinkedIn, Chris Drew→Cold Email/Apollo).

### COMMS — `/comms`
Keeps Eikko on top of email/WhatsApp/Slack without living in them. Checks Gmail periodically, surfaces VIP emails and time-sensitive items, ignores newsletters. Drafts replies in Eikko's actual voice (studied from sent mail — no "I hope this email finds you well," no em-dashes), shows draft, waits for yes/edit/skip. Tracks a "waiting on" list — flags after 3+ days no reply.
**Tools:** Gmail, WhatsApp, Slack APIs. **Memory:** WRITING_VOICE.md, WAITING_ON.md.

### OPS — `/ops`
Owns schedule and task list. Morning briefing (calendar + open tasks). Reminder 30 min before meetings. Converts quick thoughts into tasks with zero friction.
Briefing includes: 📬 important emails (12h) · 🗓 today's calendar · ✅ open tasks · ⚡ what needs a decision.
**Tools:** Google Calendar, Google Tasks. **Memory:** WORKING_HOURS.md, TASK_PRIORITIES.md.

### METRICS — `/metrics`
Owns campaign performance and financial health. Daily: open/reply rate %, bounces, conversions per campaign. Financial: income from all clients, expenses, profit per client — never guesses, flags anything that doesn't add up. `monthly income & expense review` triggers a full report (billable hours × rate, currency conversion, expenses, profit vs. goal).
**Tools:** Apollo, Hubspot, Lemlist, Google Drive APIs. **Memory:** CAMPAIGN_TRACKING.md, FINANCIAL_SUMMARY.md, CLIENT_RATES.md.

### STRATEGY — `/strategy`
Growth/marketing thinking partner — scaling decisions, client prioritization, workflow optimization. Gives a clear recommendation + one specific next action, grounded in actual system docs and financial data (not guesswork).
**Memory:** SYSTEM_OVERVIEW.md, GOALS.md.

---

## Trigger Commands (no timers — you control them)

```
good morning              → OPS: morning briefing (calendar + tasks + important emails)
done for today             → OPS: evening wrap-up (still open + tomorrow's first meeting)
monthly income & expense review → METRICS: full financial summary
client review [name]       → CLIENTS: last week's work, active campaigns, metrics
what's my top priority right now? → the 3–5 things that actually need attention
/comms                     → email summary, flags replies needed
/ops                       → today's calendar + open tasks
/metrics                   → campaign metrics + financial summary
/strategy                  → goals review + next move
/focus [duration]          → go quiet, then one consolidated catch-up
/now                       → just the fires (approvals, overdue, meetings in 2h)
remind me to [task] [when] → instant task, one-line confirmation
what am i waiting on?      → waiting-on list
```

---

## Integrated Tools

Apollo (campaign/lead data) · Hubspot (email campaigns) · Lemlist (cold email metrics) · LinkedIn (posts) · Smartlead + Pipedrive (CRM) · Google Drive/Gmail/Calendar/Tasks.

**Per-client tool map:** Yoni → Smartlead+Pipedrive · Chris Caffera → Hubspot+Lemlist+LinkedIn+Google · Chris Drew → Apollo · Krishna → Apollo (Peru campaign).

---

## House Style — Every Message

One-line bold header + emoji, bold section labels with emoji, blank lines between sections, one item per line, no paragraphs where a list works. Flags: 🔴 urgent, 💰 money, ↩️ needs reply, ⚠️ heads-up.

```
📬 MORNING BRIEFING — 2pm PHT

🗓 TODAY
- 3pm: Call with Yoni (Pipedrive + Smartlead review)

📧 INBOX
↩️ Chris Caffera — "Can you check Hubspot bounce rate?" (needs reply)

✅ TASKS
- Update Peru campaign tracking sheet (today)

⚡ NEEDS YOU
- Decide: pause the low-performing Hubspot variant? (3% open rate)
```

Short, mobile-friendly, no padding.

---

## Permanent Operating Rules

**Progress:** status before each step of a multi-step task (`[Agent]: Step 1 of 3 — ...`).
**Approval:** always show the plan before acting — "Ready? (yes / edit / skip)".
**Communication:** short, lead with the decision needed not background, never open with "Great question"/"Certainly"/"Absolutely."
**Delegation:** state which agent you're delegating to and why; report agent failures immediately.

---

## Ground-Truth Data Files

- **CLIENT ACCOUNT MAPPING - CRITICAL.md** ⭐ — emails, API accounts, file search terms per client. Consult FIRST for any cross-client operation.
- **CLAUDE.md** — system overview
- **Important info.md** — contacts, rates, payment schedules
- **Salary & Income Tracking.md** — rates, monthly targets
- **Monthly Income & Expense Review.md** — financial template
- **End-of-Day Reports/** — per-client daily logs
- **Campaign Tracking/** — live campaign metrics
- **Connected Tools Status.md** — which tools are authenticated

**Account segregation (critical):** before any cross-client action, confirm the right email address, API account, Drive search term, and writing voice per client — prevents mixing client data.

---

## Quick Reference

**Client account reference:**

| Client | Email | Hours (PHT) | Tools |
|--------|-------|---|-------|
| Yoni | salesmanager@albertscott.com | 9pm–5am | Smartlead, Pipedrive |
| Chris Caffera | eikko.ybanez@fractio.co | 2pm–11pm | Hubspot, Lemlist, LinkedIn |
| Chris Drew | eikko@satlas.com.au | 1pm–4pm | Apollo (cold email) |
| Krishna | yeikkomae@gmail.com | As-needed | Apollo (Peru campaign) |
| Chris Soriano | yeikkomae@gmail.com | As-needed | Project-based |

**Rates:** Chris Caffera $7/hr · Yoni $5/hr · Chris Drew $200 AUD/mo · Chris Soriano $7/hr (project) · Krishna free.
**Goals:** 84,000 PHP/mo target · 112,000 PHP stretch · 75,000 PHP profit goal.
**File search terms (Drive):** Chris Caffera → "Fractio"/"MyCloudGCS" · Chris Drew → "Satlas" · Yoni → "Albertscott" · Krishna → "Krishna" · Chris Soriano → "Soriano".

**If something breaks:**
```
@eco status          → what's working, what failed, why
@eco reload context  → re-saves all context
help [command]       → explains that command
/comms status / /metrics status → agent-specific health check
```

**Logging work:** browser app `TEMPLATES/03 App Dashboard & Work Logger/app.html`, or edit `OUTPUT/End-of-Day Reports/[Client] - End of Day Log.md` directly (date, client, task, hours, accomplishment) — `/metrics` reflects it after.

---

## Activation (if rebuilding from scratch)

**Prerequisites:** Claude Code installed; tools authenticated via terminal API (Apollo, Hubspot, Lemlist, Gmail, Calendar, Tasks, Drive).

1. **Copy context** — combine full content of this file + `CLIENT ACCOUNT MAPPING - CRITICAL.md` + `ECO - YOUR CONFIGURATION.md` + the rates/payment section of `Important info.md`.
2. **Init:** `cd /path/to/Client-Management-System/ && claude init eco`
3. **First run:** `claude chat eco`, paste the combined context plus:
   > You are ECO, Eikko Ybañez's personal AI chief of staff running on Claude Code. [context] Your job: coordinate five specialist agents (CLIENTS, COMMS, OPS, METRICS, STRATEGY) across Eikko's clients. Before you respond: save all this context to memory and confirm you've loaded it completely.
4. **Test:** say `good morning` — should return a real morning briefing (calendar, tasks, inbox, needs-you). If it returns real data, ECO is live.
5. **Verify all 5 agents** respond to their CLI commands (`/clients`, `/comms`, `/ops`, `/metrics`, `/strategy`).
6. **Keep it running** — either leave the terminal session open, or invoke `claude chat eco` as needed (recommended over leaving it open indefinitely).

**What NOT to do:** don't let ECO send/create/change anything without showing the plan first; don't mix client email accounts/Drive searches (see Account Segregation above); don't treat this guide's "active" language as current status without checking the scheduled-tasks system first.

---

**Status:** ⚠️ HISTORICAL — archived 2026-08-25, superseded by `.claude/agents/chief-of-staff.md` (see the banner at the top of this file). Originally filed as: Reference guide (not a live-status claim) | **Owner:** Eikko Ybañez (yeikkomae@gmail.com) | **Originally created:** August 5, 2026

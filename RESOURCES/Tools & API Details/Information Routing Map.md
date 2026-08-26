# Information Routing Map

**Owner:** `cio` · **Created:** 2026-08-25 · **Read at runtime by `inbox-triage`.**

This map answers one question: **which account and which sender belong to which client.** `inbox-triage` reads this instead of carrying its own hardcoded list, so the routing lives in one place and one agent owns keeping it true.

Access, scopes, and credential state live in the **[Access & Identity Register](Access%20&%20Identity%20Register.md)** — not here.

---

## ⚠️ What is actually known about senders

Sources cross-read 2026-08-25: `.claude/agents/inbox-triage.md`, `.claude/agents/_shared/connector-status.md`, `CLIENT PROFILES/*.md`.

**The `Email:` field is `(TBD)` for every full-time and part-time client in `CLIENT PROFILES/Important info.md`** — Chris Caffera, Chris Drew, Yoni Lebovits, Krishna Nainani. Individual profiles are no better. Client-side mailbox addresses that *do* appear (`cueneyt@hellostarfix.com`, `tobias@sellervate.net`, and the rest of the Starfix sending pool) are **campaign sending mailboxes, not the addresses clients write to Eikko from.**

So the "internal senders" column below is **⛔ largely unverified.** It records who to expect by *name*, which is what `inbox-triage`'s triage rules actually key on today, and marks the addresses as needing supply. Do not invent an address to fill a cell.

---

## Table 1 — Email routing

| Account | Authoritative for | Internal senders (by name) | Tool / platform mail expected | Feeds |
|---|---|---|---|---|
| `yeikkomae@gmail.com` | **General / catch-all.** Krishna, Chris Soriano, and anything not owned by a client-domain inbox below | Krishna Nainani ⛔ addr TBD · Chris Soriano ⛔ addr TBD | Upwork, Onlinejobs, Wise payments | `PROJECTS/Active/MASTER-TASK-LIST-ACTIVE.md` · `OUTPUT/End-of-Day Reports/` |
| `eikkomaeybanez@gmail.com` | **Personal.** Not client work | Mariette (personal) | — | Nothing client-facing. Triage should surface personal mail to Eikko and file nothing. |
| `eikko@satlas.com.au` | **Chris Drew / Satlas**, Capital Financing | Chris Drew ⛔ addr TBD | Zapmail, InboxKit, PlusVibe — all three are connected apps on this account | `CLIENT PROFILES/Chris Drew - Profile (Satlas).md` · `OUTPUT/Campaign Tracking/` |
| `eikko.ybanez@fractio.co` | **Chris Caffera / Fractio** | Chris Caffera ⛔ addr TBD · Fatin (sub-client, mirrors Chris's workflow) ⛔ addr TBD · HPG-side contacts ⛔ addr TBD | Apollo (shared login on Chris's account — **verification codes are forwarded by Chris**, so expect them here), HubSpot, Lemlist | `CLIENT PROFILES/Chris Caffera - Profile.md` · `PROJECTS/Active/CHRIS-CAFFERA-HPG-WORKSTREAM.md` · `PROJECTS/Active/CHRIS-CAFFERA-TASK-LIST-WEEK-OF-*.md` |
| `salesmanager@albertscott.com` ⚠️ spelling unconfirmed | **Yoni Lebovits / Albert Scott** | Yoni Lebovits ⛔ addr TBD | Smartlead, Pipedrive, Calendly booking notifications, TimeDoctor | `CLIENT PROFILES/Yoni - Profile (Albert Scott).md` · `PROJECTS/Active/YONI-FEEDBACK-UNCATEGORIZED-MESSAGES.md` · `OUTPUT/Campaign Tracking/` |
| `eikko.ybanez@mycloudgcs.com` | **MyCloudGCS** | ⛔ unknown | ⛔ unknown | 🔴 **No access.** Outlook, never connected, no account key. Nothing routes here until it is connected. |
| *(no inbox)* | **Penji** ×2 | Penji team — Joan (warm-reply routing), Oliver (closing) | ⛔ unknown | 🔴 **No access.** ⛔ **No Penji email address appears anywhere in this repo.** Addresses must be supplied by Eikko before a row can be written. |

### Senders needing an inbox assignment

**`cueneyt.nurdogan@sellervate.de`** — named in the build request as a Cüneyt/Sellervate internal sender. ⛔ **This address appears nowhere in this repository** (searched `CLIENT PROFILES/`, `OUTPUT/`, `.claude/`). The Cüneyt profile records `cueneyt@hellostarfix.com` as a *campaign sending mailbox*, which is a different thing.

**It is not assigned to an inbox here.** Cüneyt has no dedicated inbox in the six above, so if he emails, it lands in one of the existing accounts — most plausibly `yeikkomae@gmail.com` as catch-all, but that is a guess and is not recorded as fact. **Ask Eikko which inbox it arrives in.**

### 🔴 Correction owed to `inbox-triage`

`inbox-triage.md` currently states:

> *"Cüneyt/Starfix communicates via WhatsApp, not email — don't expect his threads to show up in any of the 5 inboxes."*

WhatsApp is his primary channel (`CLIENT PROFILES/Cüneyt - Profile (Starfix).md`: **Communication: WhatsApp**), but "not email" is too strong — an email address for him has been raised, and the standing instruction tells the triage agent to actively *not look*. The instruction should soften to "primary channel is WhatsApp; email is possible but no address is confirmed." See the proposed edit in `OUTPUT/Security & Access Reviews/2026-08-25.md` — **not yet applied; `inbox-triage` is a working agent and the edit is awaiting Eikko's yes.**

---

## Table 2 — Manual-intake channels

Channels with no connector. Content reaches this system only when **Eikko pastes it**. Slack is 🟡 not connected per `_shared/connector-status.md`; WhatsApp has no connector at all.

| Channel | Workspace / thread | Client | Ownership | Status |
|---|---|---|---|---|
| Slack | `dotpenji.slack.com` — incl. `#response` channel for warm-reply routing | **Penji** | 🔴 **Client-owned** | 🟡 Not connected. Manual paste only. |
| Slack | Chris Caffera's workspace — `#marketing` channel (LinkedIn image sourcing, post scheduling) | **Chris Caffera / Fractio** | 🔴 **Client-owned** | 🟡 Not connected. Manual paste only. ⛔ Workspace URL not recorded anywhere in this repo. |
| WhatsApp | Direct 1:1 | **Cüneyt / Starfix** | Personal channel, client relationship | ⚫ No connector, by design. Manual paste only. |

### Not on Slack — a new thread is a new row, not an assumption

**Albert Scott (Yoni), Satlas (Chris Drew), Krishna Nainani, Chris Soriano, and Edward Lehner are not on Slack.** No Slack workspace is recorded for any of them.

If a Slack thread appears for one of these clients, that is **new information**: add a row to this table, confirm ownership with Eikko, and note when access was granted. Do not file it as though the channel was always there.

### Other WhatsApp channels — documented, not yet lanes

⚠️ The three channels above are the ones with a `OUTPUT/Conversations/` folder. But WhatsApp is documented for more clients than Cüneyt:

- **Yoni / Albert Scott** — "EOD updates channel," short ✅ bullet format (`Yoni - Profile (Albert Scott).md`)
- **Chris Soriano** — "Via WhatsApp task assignments" (`Chris Soriano - Profile.md`)
- **Chris Caffera** — listed among regularly-checked channels alongside Slack, Outlook, Teams
- **Chris Drew / Satlas** — WhatsApp group chat, address TBD

These are **real channels without a folder.** The three-folder scope is a deliberate starting point, not a claim that the others don't exist. When Eikko pastes from one, create its folder then.

---

## Paste-intake protocol

The order is fixed. `cio` runs it every time.

**1 · Attribution.** Identify the client before anything is written. If the thread doesn't clearly belong to one client, **ask — never guess.** Same rule `meeting-summarizer` follows, which has already caught one real misfile.

**2 · Redaction.** Scan the whole paste for credential-shaped content *before* any of it reaches disk. A secret value never gets written — not to the conversation file, not to the register, not to a scratch file. In its place:

```
[CREDENTIAL REDACTED — <what it is>, see Access & Identity Register]
```

Then tell Eikko in-session what arrived and from whom, and add a **by-reference row** to the register — what it is, where it came from, no value. **Eikko places the actual value himself.** Precedent: Cüneyt's PlusVibe API key arrived exactly this way.

**3 · Filing.**

```
OUTPUT/Conversations/<Client>/YYYY-MM-DD - <Slack|WhatsApp> - <topic>.md
```

Header carries: source · workspace · participants · date range · attributed client. Client folder names mirror `OUTPUT/Meetings/` exactly — `Cüneyt (Starfix)`, not `Cuneyt`.

**4 · Handoff.** `cio` files and redacts, and stops there.

| What's in the thread | Goes to |
|---|---|
| Action items | `meeting-summarizer` |
| Tasks to track | `project-manager` |
| Anything needing an inbox sweep | `inbox-triage` — **never run a second sweep yourself** |
| Folder/naming cleanup | `file-organizer` |

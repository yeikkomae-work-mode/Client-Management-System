# Conversations — pasted Slack & WhatsApp threads

**Owner:** `cio` · **Created:** 2026-08-25 · **Lane starts forward from this date — there is no backfill.**

Slack and WhatsApp have no working connector into this system. Anything here arrived because **Eikko pasted it**. This folder is the filing lane for those pastes, mirroring `OUTPUT/Meetings/`.

---

## 🔴 These files are client data, not Eikko's notes

**Both Slack workspaces are client-owned.**

- `dotpenji.slack.com` — **Penji's** workspace
- Chris Caffera's `#marketing` workspace — **the client's** workspace

A thread pasted out of either one is the client's data sitting in Eikko's repository. That is a different thing from Eikko's own meeting notes about a client, and it deserves a different level of care:

- Nothing from a client workspace gets shared onward, quoted into another client's file, or pasted into a tool without Eikko saying so.
- Participant names stay as they are — but anything a third party said that isn't Eikko's to circulate stays in the file it was filed in.
- **Repository visibility: ✅ verified private, 2026-08-25** (GitHub API — `"private": true`, `"visibility": "private"`, 0 forks). Re-check before that assumption is leaned on again; collaborator access was not enumerated.

WhatsApp with Cüneyt is a personal channel rather than a client-owned workspace, but the same handling applies.

---

## Naming convention

```
OUTPUT/Conversations/<Client>/YYYY-MM-DD - <Slack|WhatsApp> - <topic>.md
```

`<Client>` mirrors `OUTPUT/Meetings/` exactly, parenthetical and accent included — `Cüneyt (Starfix)`, not `Cuneyt`.
`YYYY-MM-DD` is the date of the **most recent message** in the thread; the full span goes in the header.

### File header

```markdown
# <topic>

**Source:** Slack | WhatsApp
**Workspace:** <e.g. dotpenji.slack.com #response — client-owned> | Direct 1:1
**Participants:** <names>
**Date range:** YYYY-MM-DD → YYYY-MM-DD
**Client:** <attributed client>
**Filed:** YYYY-MM-DD by `cio`

---
```

---

## The redaction rule

**A secret value never reaches disk — including this folder.**

Every paste is scanned for credential-shaped content *before* any of it is written. API keys, tokens, passwords, connection strings, recovery codes. Where one appears, the file gets a placeholder and nothing else:

```
[CREDENTIAL REDACTED — PlusVibe API key, see Access & Identity Register]
```

Then: `cio` tells Eikko in-session that a credential arrived and from whom, and adds a **by-reference row** to `RESOURCES/Tools & API Details/Access & Identity Register.md` naming what it is and where it came from — with no value. **Eikko places the actual value himself.**

This is not hypothetical. Cüneyt's PlusVibe API key arrived exactly this way — supplied by the client in chat.

## Attribution

A thread that doesn't clearly belong to one client gets **asked about, never guessed.** An unattributed file here is a drift item the `cio` session opener explicitly looks for.

## Current folders

Three, for the three manual-intake channels that exist today:

| Folder | Channel |
|---|---|
| `Penji/` | Slack — `dotpenji.slack.com` (client-owned) |
| `Chris Caffera/` | Slack — `#marketing` (client-owned) |
| `Cüneyt (Starfix)/` | WhatsApp — direct |

⚠️ Other clients have documented WhatsApp channels without a folder here — Yoni, Chris Soriano, Chris Drew, and Chris Caffera. See `RESOURCES/Tools & API Details/Information Routing Map.md`. Create the folder when the first paste arrives; don't pre-create empty ones.

**A new channel is a new row in the routing map, not an assumption.** Albert Scott, Satlas, Krishna, Chris Soriano, and Edward Lehner are **not** on Slack — if a Slack thread appears for one of them, that is new information to confirm with Eikko, not a folder to quietly add.

# 🔄 Master Sync System — Guide

**Purpose:** One reusable pattern for keeping a per-client "sync tracker" file up to date, so saying `"update"` syncs all completed work into that client's docs instead of manually updating multiple files.

*(This replaces 5 earlier docs that all covered this same concept — MASTER-SYNC-PROMPT-TEMPLATE.md, MASTER-SYNC-SYSTEM-PROMPT.md, SYNC-SYSTEM-CLIENT-EXAMPLES.md, SYNC-SYSTEM-QUICK-REFERENCE.md, SYNC-SYSTEM-QUICK-START.md — consolidated here to remove duplication. Originally created August 5, 2026.)*

---

## The Concept (30 seconds)

Create ONE file per client: `MASTER-SYNC-TRACKER-[ClientName].md`. This file:
- Lists all their files in the system
- Tracks current work & status
- Has an `"update"` command for instant syncing
- Shows team roles & preferences

**Only one of these has actually been built and used:** `MASTER-SYNC-TRACKER.md` (Albert Scott / Yoni). Satlas, Krishna, Chris Soriano, and Rachel were planned but never set up — see Status table below.

---

## Quick Setup (copy-paste, for a new client)

```
I need to set up a comprehensive sync system for [CLIENT_NAME] work.

Requirements:
1. Create a MASTER-SYNC-TRACKER-[CLIENT_NAME].md file as the central hub for ALL [CLIENT_NAME] work
2. It should monitor and document all files related to this client
3. When I say "update", sync all completed work to all relevant [CLIENT_NAME] files
4. Track project status, completed tasks, next steps, and team references

Include:
- List of all [CLIENT_NAME] files
- Current session work status
- Next steps & deployment checklist
- Team reference (key contacts, approvals, preferences)
- File sync status table
- A simple "update" command that triggers instant syncing

Make sure every file mentioned in the tracker actually exists for this client.
```

## File Structure This Creates

```
Client-Management-System/
├── CLIENT PROFILES/[Client] - Profile.md         (reference, don't modify during sync)
├── RESOURCES/Workflows/MASTER-SYNC-TRACKER-[Client].md   (central hub — this pattern)
├── OUTPUT/End-of-Day Reports/[Client] - End of Day Log.md
└── OUTPUT/Campaign Tracking/[Client-specific logs]
```

## Tracker Template

```markdown
# 🔄 MASTER SYNC TRACKER - [CLIENT_NAME] Operations
**Central Hub for All [CLIENT_NAME] Work**

## Quick Sync Command
When you say "update", I will:
1. Sync all completed work to these files
2. Update all [CLIENT_NAME]-related docs
3. Report status for morning briefing
4. Confirm all changes synced

## [CLIENT_NAME] Files in Sync
- ✅ `[Client] Profile.md` — reference (do not modify)
- ✅ `MASTER-SYNC-TRACKER-[Client].md` — this file
- ✅ Project-specific files (list by category)
- ✅ `[Client] - End of Day Log.md`

## Current Session Work
### Task: [Description] — Status: [In Progress/Complete]
- [What was done]

## Sync Status by File
| File | Last Updated | Status | Notes |
|------|--------------|--------|-------|

## Next Steps
1. ...

## Team Reference
- [Contact] — role & responsibilities

**Last Sync:** [Date & Time] | **System Status:** [Summary]
```

## Customization Checklist

- [ ] Replace `[CLIENT_NAME]` with actual client name
- [ ] List all actual files that exist for that client
- [ ] Reference the client's profile document
- [ ] Include client-specific tools (APIs, platforms, credentials)
- [ ] Document team members and roles
- [ ] List important rules/preferences from the client profile
- [ ] Set up monitoring files (status, EOD log, work log)
- [ ] Add project-specific next steps

## Status by Client

| Client | Tracker File | Status |
|--------|--------------|--------|
| Albert Scott (Yoni) | `MASTER-SYNC-TRACKER.md` | ✅ Active, in use |
| Satlas (Chris Drew) | `MASTER-SYNC-TRACKER-Satlas.md` | Not created — would track Apollo, PlusVibe, campaigns, infrastructure |
| Krishna | `MASTER-SYNC-TRACKER-Krishna.md` | Not created |
| Chris Soriano | `MASTER-SYNC-TRACKER-ChrisSoriano.md` | Not created |
| Rachel (Albert Scott — Europe) | `MASTER-SYNC-TRACKER-Rachel.md` | Not created |

## Pro Tips

- One tracker per client, named consistently: `MASTER-SYNC-TRACKER-[ClientName].md`
- Update frequently — say `"update"` after each task block, not just at EOD
- Reference the client's profile file so rules/preferences/team info stay in one place
- Audit trail matters most for clients with multiple concurrent projects

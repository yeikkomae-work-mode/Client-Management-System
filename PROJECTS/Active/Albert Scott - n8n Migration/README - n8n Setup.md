> **⚠️ Retired 2026-08-26 — n8n is no longer the automation platform for Albert Scott.** Eikko pulled it before any of the credentials below were ever created, so neither workflow ever ran live. This doc, and the two workflow JSON files in this folder, stand as a record of what was built, not a live setup guide. Reply-triage across SmartLead and LinkedIn is currently manual — tracked in the Command Center's Automation Log (`dashboard/command-center.html`) — pending a decision on what replaces n8n, if anything.

# Albert Scott — n8n Workflows (Smartlead / Pipedrive / Gmail / Calendly)

Scope: reply triage → CRM sync, and Calendly bookings → CRM sync.
Left out on purpose: the Fathom → Sheets sync and the deliverability check — parked for later.

Two workflows, both in this folder, importable as-is into n8n (Workflows → Import from File):

- `smartlead-reply-triage.json` — the hourly reply classifier + Pipedrive sync + block list. Replaces `scripts/scheduled-inbox-sync-prompt.md`.
- `calendly-booking-to-pipedrive.json` — Calendly's own webhook straight into Pipedrive. Replaces Step 5 of the same prompt (the Gmail-polling version).

Both were hand-built against the real n8n source (cloned from `n8n-io/n8n`) to pin exact node type versions — not guessed from memory. If your n8n instance is on an older version, some `typeVersion`s below may not exist yet; n8n will flag any mismatch on import.

---

## 1. Why Gmail isn't in here

The old Calendly flow searched Gmail because Calendly's webhook wasn't wired up. n8n has a native `calendlyTrigger` node, so `calendly-booking-to-pipedrive.json` uses that directly — Gmail is removed from the loop entirely, not migrated. That also kills the bug class that hit this flow twice (a subject-line filter matching zero emails, then a missing `addLead` call) — there's no subject line to parse anymore.

If Calendly webhooks can't reach your n8n instance (self-hosted behind a firewall, etc.), tell me and I'll swap the trigger for Gmail-polling instead — same logic either way, just a different front door.

## 2. Credentials to create in n8n

**Corrected 2026-08-25** — the plan below (Smartlead as a workflow variable) is what this doc originally said, but it's not what actually got built. Every Smartlead HTTP Request node (`Fetch Replies`, `Set Smartlead Category`, `Check Block List`, `Block Domain`, `Block Domain in Smartlead`) uses `authentication: genericCredentialType` / `genericAuthType: httpTemplatedCustomAuth`, same pattern as Anthropic. `list_credentials` on the live n8n instance returns zero credentials, and none of these nodes have a `credentials` object attached — nothing is wired up yet. There's no MCP tool that can create an n8n credential (only list/attach one that already exists), and raw API keys shouldn't pass through Claude anyway — this section is written so Eikko can do it directly in the n8n UI.

| Name | Type | Where used | Value to paste (as **Custom Auth** JSON — no header/query fields to fill in individually, just this one JSON block) |
|---|---|---|---|
| `Pipedrive - Albert Scott` | Pipedrive API (`pipedriveApi`) — has its own dedicated field, not custom auth | Every `n8n-nodes-base.pipedrive` node | Your Pipedrive API token (Pipedrive → Settings → Personal preferences → API) |
| `Smartlead - Albert Scott` | Custom Auth | `Fetch Replies`, `Set Smartlead Category`, `Check Block List`, `Block Domain`, `Block Domain in Smartlead` | `{"qs": {"api_key": "YOUR_SMARTLEAD_KEY"}}` |
| `Anthropic - Claude` | Custom Auth | `Classify Reply` | `{"headers": {"x-api-key": "YOUR_ANTHROPIC_KEY"}}` |
| `Google Sheets - Albert Scott` | Google Sheets OAuth2 | Both Append Log Row nodes | Sign in with the Google account that owns/can access the run-log sheet |
| `Calendly - Albert Scott` | Calendly API (n8n's built-in Calendly credential) | Calendly Booking trigger | Your Calendly API key or OAuth2 sign-in |

Once these 5 exist in n8n (Settings → Credentials → New — the API tokens themselves should come from wherever they're already kept, e.g. a password manager, never pasted into chat), tell Claude and it'll wire each one into its nodes via `setNodeCredential` in one pass rather than you clicking through 51 nodes by hand.

## 3. Workflow variables to set

n8n → Settings → Variables (or per-workflow if your plan doesn't have global variables):

| Variable | Value | Notes |
|---|---|---|
| `SMARTLEAD_API_KEY` | your Smartlead key | same key as `.env`'s `SMARTLEAD_API_KEY` |
| `SMARTLEAD_BASE_URL` | `https://server.smartlead.ai/api/v1` | matches `.env.example` |
| `PIPEDRIVE_OWNER_ID` | `26939288` | Yoni's owner_id — hardcoded across every Pipedrive write today; kept as a variable so it isn't buried in six nodes |
| `RUN_LOG_SHEET_ID` | the Google Sheet ID you want run logs written to | **new** — see Section 5, this doesn't exist yet |
| `CLASSIFIER_SYSTEM_PROMPT` | see Section 4 | the reply-categorization instructions |
| `WEEKLY_BACKLOG` | `false` | set to `true` on a second scheduled copy of the triage workflow for the weekly 8-day rescan (see Section 6) |

## 4. The classifier prompt

`smartlead-reply-triage.json`'s "Classify Reply" node calls Claude Opus 5 with a JSON schema forcing one of nine categories back — no free text, no parsing ambiguity. It reads its instructions from the `CLASSIFIER_SYSTEM_PROMPT` variable so you can tune wording without touching the workflow. Set it to:

```
You are triaging cold-email replies for Albert Scott's Amazon-US sales outreach.
Read the reply and choose exactly one category:

- interested — real interest in an Amazon US conversation
- meeting_request — explicitly asks to schedule a call
- follow_up — wants more info, hasn't clearly committed
- not_interested — explicit rejection, "not for now," similar
- do_not_contact — "no"/"stop"/unsubscribe/any clear opt-out, even one word, even casually worded
- out_of_office — autoresponder / OOO message
- wrong_person — says they're not the right contact
- unsure — genuinely ambiguous, can't tell intent
- ignore — auto-generated, no human signal either way

Also set names_alternate_contact to true only if the reply is an out-of-office or
wrong-person message that names a specific reachable colleague (a name, or a direct
email/phone for someone else at the company) — this determines whether we're allowed
to block their domain. If no alternate contact is named, set it to false.

Set confidence to low whenever the reply is short, sarcastic, ambiguous, or could
plausibly fit two categories — the workflow treats low-confidence unsure/wrong_person
calls conservatively (no domain block) rather than guessing.

reasoning: one sentence explaining the call, referencing the specific line that decided it.
```

This is a first draft, not gospel — it encodes the category table from the workflow doc but hasn't been shadow-run against real replies yet (see Section 8). Expect to tighten the `unsure` and `do_not_contact` boundaries once you see disagreements.

## 5. The run log — new plumbing this migration needs

The old CSVs (`logs/inbox-sync-log.csv`, a hypothetical `logs/calendly-log.csv`) don't exist in an n8n world — n8n runs server-side, not on a machine with a local `logs/` folder. Both workflows now append to a Google Sheet instead, because `src/googlesheets.js` already has service-account credentials wired up — Claude Code can read this sheet with zero new code once it's created.

**Before first run, create a Google Sheet with two tabs:**

- `inbox-sync-log` — header row: `timestamp, campaign, lead_name, lead_email, category_applied, confidence, pipedrive_action, domain_blocked, reply_excerpt`
- `calendly-log` — header row: `timestamp, lead_name, lead_email, company, event_name, starts_at, person_id, org_id, lead_id, domain_blocked, is_reschedule`

Share it with your Google Sheets OAuth account (or the service account, if you'd rather reuse `.env`'s credentials), grab the sheet ID from its URL, and set `RUN_LOG_SHEET_ID`. Both workflows use `autoMapInputData`, so as long as the header row matches the fields each "Build Log Row" node produces, no per-column mapping is needed.

## 6. Checkpoint state — do not start from zero

`smartlead-reply-triage.json` stores its checkpoint in **n8n workflow static data**, not a file — the direct replacement for `.last-checkpoint`. Two things follow from that:

1. **Static data only persists on production runs.** A manual "Execute workflow" test in the editor reads the checkpoint but never writes it back — that's intentional, so testing doesn't corrupt the real state, but it means you can't "test" your way to advancing the checkpoint.
2. **Seed it before cutover, don't start from zero.** On the day you switch off the Claude Code automation, read the real value out of `/home/user/smartlead-api-client/.last-checkpoint` and either: (a) run the workflow once manually with a temporary Code node that sets `$getWorkflowStaticData('global').lastCheckpoint` to that value, or (b) just let the first run's 24-hour default overlap — every action taken is idempotent-ish (Pipedrive search-before-create, block-list check-before-block) so a day of overlap re-processes rather than duplicates, at worst re-blocking an already-blocked domain (harmless) or logging a lead twice.

**Weekly backlog scan:** the original runs an 8-day rescan at least once a week, ignoring the checkpoint, to catch anything a reply spike caused the hourly poll to miss. Set this up as a **second, separate schedule trigger on a copy of this workflow**, with `WEEKLY_BACKLOG=true` set only in that copy's own environment (or gate it with an IF node reading `$now.weekday`). I left it as a variable rather than building the branching logic in, since it's one clean IF away and depends on which day you want it to run.

## 7. Things that are genuinely different from the old flow, on purpose

- **No prose report at the end.** The old runs ended in a paragraph calling out 403s and odd payloads. n8n gives you per-execution logs and an error workflow instead — wire n8n's "Error Workflow" setting (Settings → Workflow Settings) to a Slack/email node if you want a ping on failure, since nothing here does that yet.
- **Pagination is not implemented — it's guarded.** The original polled with offset increments of 20 until exhausted. This version fetches up to 100 replies per run and **throws an error** if Smartlead reports more were available, rather than silently dropping the overflow. At an hourly cadence this should never fire; if it does, it's telling you the interval needs to be shorter or true pagination needs adding — say the word and I'll add an offset loop.
- **Free-mail domains are never blocked.** Added in the Calendly workflow (`isFreeMail` check) — the original workflow doc doesn't mention this case, but blocking `gmail.com` because one lead used a Gmail address would silence every future campaign to every Gmail user. Worth double-checking whether the Smartlead-reply-triage flow needs the same guard — right now a personal-email domain going through the `block` branch would get blocked, same as any other. Flag if that's wrong for your case and I'll add the same check there.

## 8. Before this touches real leads

1. **Import both workflows, wire the credentials and variables above, leave them Inactive.**
2. **Shadow-run the triage workflow**: point `Set Smartlead Category`, the Pipedrive writes, and `Block Domain` at a disabled/no-op state (or just watch a manual execution against real data without activating the schedule) and compare its category calls against what Claude Code would have done, or against your own read of the same replies. This is the one step I can't shortcut for you — the classifier prompt needs real disagreement data before it's trustworthy unattended.
3. **Seed the checkpoint** per Section 6.
4. **Activate**, watch the first few live hourly runs closely, then turn off the Claude Code scheduled task once you trust it.

## 9. What's not addressed here

Fathom→Sheets and the deliverability check are out of scope for this pass, per your instruction — they still run wherever they run today. HeyReach/LinkedIn and AIOSEO/WordPress are still unbuilt in either system.

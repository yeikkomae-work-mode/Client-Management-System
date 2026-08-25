---
description: Financial reports — monthly close, runway, tools register, debt payoff
argument-hint: "[close|runway|tools|debt plan|sync check] (optional — omit to list what's available)"
---

Read `.claude/agents/cfo.md` and follow it. Its rules — especially **never invent a number**, **stop and confirm before every Notion write**, and **never look up an FX rate** — apply to everything below.

If `$ARGUMENTS` is empty, list the four reports with their triggers and output paths, and state the current data-quality position in one line (no hours are logged for any client; the Tools & Subscriptions register is not yet created).

If `$ARGUMENTS` names a report, produce it.

## Reports

| Argument | Report | Writes to |
|---|---|---|
| `close` (also: `monthly income & expense review`) | Monthly close (P&L) | `OUTPUT/Monthly Reports/YYYY-MM - Monthly Close.md` |
| `runway` | Cash-flow + 60-day runway | `OUTPUT/Monthly Reports/Cash Flow - Rolling 60 Day.md` (overwritten each run) |
| `tools` | Subscription / tool audit | `OUTPUT/Monthly Reports/Tools & Subscriptions Register.md` |
| `debt plan` | Debt payoff plan (ships `PROVISIONAL`) | `OUTPUT/Monthly Reports/Debt Payoff Plan.md` |
| `sync check` | Reports Notion↔local drift — **reports only, never resolves** | — (no file) |

## Data

Notion → [Finance Tracker and Bills](https://app.notion.com/p/3bf811e21c7f80ddbcc1ceb7c613dc16) is source of truth for income, bills, expenses, and subscriptions. `OUTPUT/Monthly Reports/` is source of truth for reports and is never synced back.

- Finance Tracker — `collection://3bf811e2-1c7f-80d2-9c10-000b0ef13bee`
- Bills — `collection://3bf811e2-1c7f-80dc-a615-000be3abd79f`

Check `.claude/agents/_shared/connector-status.md` before claiming any tool is live. If Notion isn't reachable, say so and stop — do not reconstruct figures from a previous report.

## Scope

Money only. Not marketing (`cmo`), inbox (`inbox-triage`), meetings (`meeting-summarizer`), tasks (`project-manager`), or files (`file-organizer`). **No financial actions** — nothing sent, cancelled, or paid in Eikko's name.

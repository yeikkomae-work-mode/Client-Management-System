---
description: Look up or list Tech Radar verdicts — what's been evaluated, adopted, killed
argument-hint: "[tool or technique] (optional — omit to list the whole radar by status)"
---

Read `RESOURCES/Tech Radar.md`.

If `$ARGUMENTS` is empty:
- Summarize the radar grouped by status: ADOPT, TRIAL (with review-by dates, flagging any overdue), HOLD, KILL, UNCLEAR.
- Call out anything needing attention: TRIALs past their review-by date, UNCLEAR rows that have sat unresolved, and HOLDs whose "revisit when" condition has since been met.

If `$ARGUMENTS` names a tool or technique:
- Return its row: status, date evaluated, cost, and the verdict reasoning.
- If it's not on the radar, say so plainly and offer to have the `cto` agent evaluate it — do not invent a verdict here.

Do not modify the radar from this command. Verdicts are written by the `cto` agent, which applies the four criteria (cost / stack fit / time-to-value / fragility) before appending a row.

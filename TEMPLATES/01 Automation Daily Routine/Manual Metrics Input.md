# Manual Metrics Input — Daily End-of-Day Log

**Use this:** At the end of your work day, log metrics from tools that don't have API/connector access.

---

## TOOLS THAT NEED MANUAL INPUT

- **Hubspot** (Chris Caffera) — Cannot be automated; manual input needed
- **Lemlist** (Chris Caffera) — Cannot be automated; manual input needed
- **LinkedIn** (Chris Caffera) — Cannot be automated; manual input needed
- **Anything else** not listed below

## TOOLS WITH API/CONNECTOR ACCESS (Auto-pulled)

- **Smartlead** (Yoni) ✓ Connected
- **Pipedrive** (Yoni) ✓ Connected
- **PlusVibe** (Chris Drew) — [Status: To be confirmed]
- **Apollo** (Chris Caffera, Chris Drew, Krishna) — [Status: To be confirmed]
- **Instantly** (Chris Drew) — [Status: To be confirmed]
- **Zapmail** (Chris Drew) — [Status: To be confirmed]
- **Inboxkit** (Chris Drew) — [Status: To be confirmed]
- **Notion** (Chris Drew) — [Status: To be confirmed]
- **TimeDoctors** (Yoni) ✓ Connected

**Note:** Once you test APIs for other tools, update this list.

---

## END-OF-DAY METRIC COLLECTION

**Do this at the end of your work day (before 5am PHT):**

Collect numbers for tools without API access and paste them here.

### TEMPLATE

```
END-OF-DAY METRICS — [Date]

CHRIS CAFFERA
Hubspot campaigns:
  - Campaign name: [Name]
  - Open rate: [%]
  - Reply rate: [%] or Replies: [#]
  - Bounces: [#]
  - Status: [Drafting/Sending/In-progress/Completed]

Lemlist sequences:
  - Sequence name: [Name]
  - Open rate: [%]
  - Click rate: [%]
  - Bounces: [#]
  - Status: [Active/Paused]

LinkedIn:
  - Posts scheduled today: [#]
  - Posts published: [#]
  - Engagements (likes/comments/shares): [#]
  - Notes: [Any important updates]

Other notes:
  - [Any ad-hoc updates or blockers]

---

CHRIS DREW
(PlusVibe and other tools — fill in if not auto-pulled)
  - [Metric 1]: [Value]
  - [Metric 2]: [Value]

Other notes:
  - [Any updates]

---

YONI
(Smartlead & Pipedrive auto-pull; add notes if needed)
Notes:
  - [Any manual updates]

---

KRISHNA
Apollo:
  - Sequences created: [#]
  - Leads added: [#]
  - Status: [Active/Paused this week]

Other notes:
  - [Any updates]

---

CHRIS SORIANO
Status: [Waiting for assignment / Completed task X]
Notes:
  - [Any updates]
```

---

## EXAMPLE (FILLED IN)

```
END-OF-DAY METRICS — 2026-08-05

CHRIS CAFFERA

Hubspot campaigns:
  - Campaign: "Summer Product Launch"
  - Open rate: 12%
  - Reply rate: 8%
  - Bounces: 2
  - Status: In-progress
  
  - Campaign: "Cold outreach wave 2"
  - Open rate: 10%
  - Reply rate: 6%
  - Bounces: 1
  - Status: Sending

Lemlist sequences:
  - Sequence: "Welcome series"
  - Open rate: 8%
  - Click rate: 3%
  - Bounces: 0
  - Status: Active
  
  - Sequence: "Engagement nurture"
  - Open rate: 11%
  - Click rate: 5%
  - Bounces: 1
  - Status: Active

LinkedIn:
  - Posts scheduled today: 2
  - Posts published: 1
  - Engagements: 15 (likes/comments)
  - Notes: Fatin's post performed well, 23 impressions

Other notes:
  - Chris wants to test new subject line tomorrow

---

CHRIS DREW
PlusVibe inbox health: 89% (healthy)
Active campaigns running, monitoring continues

Other notes:
  - Data recorded in Notion

---

YONI
(Smartlead & Pipedrive auto-pulling)
Notes:
  - Strong response rate today, 20+ new replies
  - No blockers

---

KRISHNA
Apollo:
  - Sequences created: 0 (no active work this week)
  - Leads added: 0
  - Status: Paused (awaiting assignment)

Other notes:
  - Waiting for new project from Krishna

---

CHRIS SORIANO
Status: Waiting for assignment
Notes:
  - None
```

---

## HOW IT FLOWS

1. **End of your work day** (before 5am):
   - Review Hubspot, Lemlist, LinkedIn (and any other manual tools)
   - Collect the numbers
   - Paste the filled template here (just update the section, not the whole prompt)

2. **Example message to me:**
   ```
   END-OF-DAY METRICS — 2026-08-05
   
   CHRIS CAFFERA
   Hubspot campaigns:
   - Campaign "Summer Launch": Open 12%, Replies 8%, Bounces 2
   ...
   [rest of metrics]
   ```

3. **Next morning (~1pm)** when you say "good morning":
   - I'll use these metrics from yesterday
   - Combine with API data
   - Generate your recap

---

## CHECKLIST (Before logging off)

- [ ] Checked Hubspot campaigns?
- [ ] Checked Lemlist sequences?
- [ ] Checked LinkedIn analytics?
- [ ] Checked any other manual tools?
- [ ] Pasted end-of-day metrics here?
- [ ] Ready to say "good morning" tomorrow?

---

## IF YOU CAN'T REMEMBER EXACT NUMBERS

That's okay! Approximate is fine:
- "Around 10% open rate"
- "About 5 replies"
- "Maybe 2-3 bounces"

I'll note estimates in the recap so you can verify later.

---

**Ready? Paste your end-of-day metrics before logging off.**

# ECO — Chrome Profile Access Guide
**Last Updated:** 2026-08-06  
**Purpose:** Reference for which Chrome profile to use for which account/platform, and how to switch.

---

## Known Chrome Profiles

| Profile Name | Icon | Associated Email | Logged Into |
|---|---|---|---|
| **VA Profile** | Purple "e" | yeikkomae@gmail.com | LinkedIn (as **Chris Caffera** — personal account), Outlook, Gmail |
| **Fractio** | Pink "E" | eikko.ybanez@fractio.co | LinkedIn (as Fatin Kwasny — Fractio company account), Lemlist, Lemwarm, Apollo |
| **Albertscott** | Blue "S" | Sales Manager | Smartlead, Pipedrive, TimeDoctors (Yoni's tools) |
| **Personal** | Photo avatar | yeikkomae@gmail.com (Google account) | General/personal browsing |
| **satlas.com.au** | Orange "W" | Eikko Ybañez | Chris Drew / Satlas tools, Apollo |

**Important correction (2026-08-06):** The "VA Profile" logs into LinkedIn as **Chris Caffera's own personal account** — not Fatin/Fractio. For Fractio company posts (as Fatin Kwasny), use the **Fractio** Chrome profile instead.

**Important correction (2026-08-08):** "Personal" and "VA Profile" both sign into the same Google account (yeikkomae@gmail.com) — checking the signed-in Google account alone is **not enough** to tell them apart, since it matches both. Don't assume which profile is active from the Google account name/email. If it's unclear which Chrome profile a connected browser session is on, ask Eikko directly rather than inferring from the account shown at myaccount.google.com.

---

## How Profile Switching Works (Limitation Notice)

- Chrome is granted to computer-use tools at **read-only tier** — clicks and typing are blocked for browser apps as a safety restriction.
- The native Chrome profile picker ("Who's using Chrome?") is outside normal webpage content, so the Claude-in-Chrome browser-automation tool can't reach it either.
- **Result: switching Chrome profiles always requires a manual click from Eikko.** ECO cannot do this step itself.

**Workflow:**
1. Eikko clicks the Chrome dock icon → clicks the profile avatar (top-right of Chrome window) → selects the target profile from "Who's using Chrome?"
2. Once the correct profile's window is open and frontmost, tell ECO which profile you're on (or just say "go to LinkedIn" / "open X").
3. ECO picks up from there using the Claude-in-Chrome browser tool — navigating, reading, and clicking within the page itself.

### Multiple Connected Browser Extensions
If ECO's browser tool reports "multiple Chrome browsers connected," it means more than one Chrome profile has the Claude-in-Chrome extension active at once. ECO will ask which one to use, or send a connect prompt to all of them so Eikko can approve the correct one directly in Chrome. Once selected, ECO names the connection (e.g. "Personal VA Chrome") for that session.

---

## Quick Reference: "Open this profile chrome" → What ECO Does

When Eikko says "open [X] profile chrome":
1. ECO explains it needs Eikko to manually switch (per limitation above) — OR if a browser connection already matches, ECO uses it directly.
2. ECO confirms via a fresh navigation + screenshot that the correct account is logged in before proceeding.
3. ECO proceeds with the requested task (LinkedIn, email, etc.) using the Claude-in-Chrome tool.

---

## Session Log

**2026-08-06:** Confirmed VA Profile → LinkedIn logs in as Chris Caffera (personal), not Fatin/Fractio. Used for scheduling Chris's personal LinkedIn posts going forward, distinct from the Fractio company page workflow (which uses the Fractio profile + Fatin's account).

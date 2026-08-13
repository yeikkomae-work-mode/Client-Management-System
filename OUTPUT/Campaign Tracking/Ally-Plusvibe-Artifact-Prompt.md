# Setting up your own live Plusvibe tracker in Claude

## One-time setup

1. In Claude, go to **Settings → Connectors** (or the connector/MCP settings menu).
2. Connect **Plusvibe**, and when it asks you to log in, use the Satlas Plusvibe login (eikko@satlas.com.au) — not a personal account. This is what makes the tracker "live."
3. Once it shows as connected, start a new chat (Cowork mode if you have it) and paste the prompt below.

## Prompt to paste into Claude

```
Connect to my Plusvibe account and build me two live, persisted artifacts I can reopen anytime:

1. Campaign tracker — a sortable/searchable table of all our active and draft campaigns, showing: campaign name, status (active/draft/completed), total leads, contacted %, replied %, positive reply %, and bounced %. Put summary metric cards at the top (total leads, total contacted, replied %, positive reply %, bounced %) pulled from the account-wide analytics. Exclude any test/internal campaigns.

2. Inbox & replies tracker — a second artifact showing: total email accounts, total domains, warmup/error/alert counts at the top, then a table of inbox health (account, status, warmup %, DNS record status), and a second table of the most recent replies (from, email, subject, campaign, category like Interested/Not interested/Out of office/Automatic reply, and when).

Before building, call the relevant Plusvibe tools once to confirm you're on the right account (check that email accounts and campaign names match Satlas domains, not any other client), then wire the artifacts to refresh live from the connector each time I open them — don't hardcode static numbers.
```

## What to expect

Claude will check a few things first, then build two artifact cards. Once created, they'll show up in your sidebar and refresh automatically with current Plusvibe data every time you open them — no need to re-run the prompt or ask Eikko for an updated file.

## If something looks off

If the campaign or inbox names Claude shows don't match Satlas (wrong domains, unfamiliar client names), stop and flag it — it likely means the wrong Plusvibe account got connected in step 2. Reconnect with the correct login and try again.

# Google Accounts OAuth Configuration

## 1. VA Personal Account
- **Email:** yeikkomae@gmail.com
- **Use Case:** Work email - main client communication
- **Services:** Gmail, Google Drive, Google Sheets, Google Calendar
- **Client ID Env Var:** `GOOGLE_VA_CLIENT_ID`
- **Client Secret Env Var:** `GOOGLE_VA_CLIENT_SECRET`
- **Status:** Configured ✓

## 2. Satlas Account
- **Email:** eikko@satlas.com.au
- **Use Case:** Satlas company communications, collaboration, and campaign monitoring
- **Services:** Gmail, Google Drive, Google Sheets, Google Calendar
- **Connected Apps:**
  - Zapmail (app.zapmail.ai) - Email infrastructure management
  - InboxKit (app.inboxkit.com) - Mailbox warmup & management
  - Plusvibe (app.plusvibe.ai) - Outbound campaign tracking
- **Client ID Env Var:** `GOOGLE_SATLAS_CLIENT_ID`
- **Client Secret Env Var:** `GOOGLE_SATLAS_CLIENT_SECRET`
- **Status:** Configured ✓
- **Campaign Monitoring:** Active across 3 platforms

## 3. Fractio Account
- **Email:** eikko.ybanez@fractio.co
- **Use Case:** Fractio company emails and communications
- **Services:** Gmail, Google Drive, Google Sheets, Google Calendar
- **Client ID Env Var:** `GOOGLE_FRACTIO_CLIENT_ID`
- **Client Secret Env Var:** `GOOGLE_FRACTIO_CLIENT_SECRET`
- **Status:** Configured ✓

## 4. Albertscott Account
- **Email:** salesmanager@albertscott.com
- **Use Case:** Albertscott sales and company management
- **Services:** Gmail, Google Drive, Google Sheets, Google Calendar
- **Client ID Env Var:** `GOOGLE_ALBERTSCOTT_CLIENT_ID`
- **Client Secret Env Var:** `GOOGLE_ALBERTSCOTT_CLIENT_SECRET`
- **Status:** Configured ✓

## 5. Personal Account (eikkomaeybanez)
- **Email:** eikkomaeybanez@gmail.com
- **Use Case:** Personal inbox — currently expecting a reschedule invite from Mariette
- **Services:** Gmail
- **Credential file:** `Personal_eikkomaeybanez_client_secret_1080807478962-2schsr021rg9eb1tcg3gu4frln8nta00.apps.googleusercontent.com.json` (project `boxwood-sandbox-505400-q3`)
- **Status:** ✅ Connected (2026-08-13) — via custom OAuth script, not claude.ai's native connector (that's locked to yeikkomae@gmail.com only). See section 6 below.
- **Note:** A separate, older `Personal_client_secret_2_...json` (project `hermes-personal-access-504417`) also sits in this folder — unused, superseded by this one. Flagged for Eikko to confirm it's safe to delete.

---

## 6. Custom Gmail Multi-Account Client (Satlas, Albertscott, Fractio, Personal)

claude.ai's Gmail connector only supports **one** account (yeikkomae@gmail.com). The other four are connected via a self-built OAuth + REST client instead:

- **Location:** `RESOURCES/Tools & API Details/Gmail Multi-Account Client/`
  - `gmail_auth.py <account_key>` — one-time browser-based authorization (run once per account; you log in yourself, script never sees your password)
  - `gmail_client.py <account_key> <list-unread|get-thread|create-draft> ...` — the working client
- **Account keys:** `personal`, `satlas`, `albertscott`, `fractio`
- **Scopes:** `gmail.readonly` + `gmail.compose` only — **no `gmail.send`**, so nothing can ever be sent through this client
- **Tokens stored at:** `RESOURCES/Tools & API Details/OAuth Credentials/<account_key>_token.json` (chmod 600, gitignored-equivalent — not committed anywhere since this isn't a tracked git repo at the top level)
- **Status (2026-08-13):** All four authorized and confirmed reading live inbox data — satlas, albertscott, fractio, personal
- **Known quirk:** `albertscott`'s OAuth client is registered as a "Web application" type (the other three are "Desktop app"), which requires an exact `http://localhost:8080/callback` redirect match — handled automatically by the script, no action needed going forward.

---

## OAuth 2.0 Authentication Flow

### Using with Claude Code

To use these accounts with Claude Code, you need to authenticate each one:

```bash
# The OAuth flow will open a browser for you to authorize
# Claude Code will handle the OAuth token exchange automatically
```

### Accessing Google Services

Once authenticated, you can use:

**Gmail:**
```bash
curl -H "Authorization: Bearer $GOOGLE_VA_ACCESS_TOKEN" \
  https://www.googleapis.com/gmail/v1/users/me/messages
```

**Google Drive:**
```bash
curl -H "Authorization: Bearer $GOOGLE_VA_ACCESS_TOKEN" \
  https://www.googleapis.com/drive/v3/files
```

**Google Sheets:**
```bash
curl -H "Authorization: Bearer $GOOGLE_VA_ACCESS_TOKEN" \
  https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}
```

**Google Calendar:**
```bash
curl -H "Authorization: Bearer $GOOGLE_VA_ACCESS_TOKEN" \
  https://www.googleapis.com/calendar/v3/calendars/primary/events
```

---

## OAuth Tokens (Generated After Authentication)

After authentication, access tokens are stored and managed by Claude Code. You don't need to manage them manually.

- Access tokens expire after ~1 hour
- Refresh tokens are stored securely for automatic refresh
- Claude Code handles token refresh automatically

---

## Next Steps

1. **Start Claude Code** - The first time you try to use a Google service, it will prompt for authentication
2. **Authorize Each Account** - You'll be redirected to Google login for each account
3. **Grant Permissions** - Approve the requested scopes (Gmail, Drive, Sheets, Calendar)
4. **Ready to Use** - Claude Code will now have access to all your Google services

---

**Last Updated:** August 5, 2026
**Configured in:** ~/.claude/settings.json

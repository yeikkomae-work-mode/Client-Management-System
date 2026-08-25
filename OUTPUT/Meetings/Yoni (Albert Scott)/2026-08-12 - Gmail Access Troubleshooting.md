# Gmail Access Troubleshooting

**Date:** 2026-08-12
**Client:** Yoni (Albert Scott)
**Fathom recording:** https://fathom.video/calls/782978256
**Recorded by:** eikko mae ybanez
**Transcript:** Not pulled — fetch on request via the recording link above (Fathom `get_meeting_transcript`, recording_id 172789351)

---

## Summary

**Meeting Purpose:** Troubleshoot Claude's inability to access Yoni's Gmail history.

**Key Takeaways:**
- Claude couldn't find Yoni's email history with Jessica Early because its Gmail connector was linked to the `Sales Manager` account, not Yoni's.
- **Solution:** Switched the Claude Gmail connector to `yoni@albertscott.com` and set permissions to "Always Allow" for full access.
- **Blocker:** The `albertscottventures.com` domain is likely blacklisted, causing email bounces and killing deliverability for Smartlead campaigns.

## Action Items

- [ ] Investigate AlbertScottVentures.com email deliverability/blacklist; resolve bounce issues — assigned to Sales Manager ([timestamp](https://fathom.video/calls/782978256?timestamp=106))
- [ ] Update Claude prompt: capture CC'd leads; update Pipedrive — assigned to Yoni Lebovits ([timestamp](https://fathom.video/calls/782978256?timestamp=164))
- [ ] Add Sales Manager Gmail API to Claude connectors — assigned to Sales Manager ([timestamp](https://fathom.video/calls/782978256?timestamp=414))

/* Agents roster (CLAUDE.md), connector status (.claude/agents/_shared/connector-status.md, verified 2026-08-24),
   Tech Radar summary (RESOURCES/Tech Radar.md), resource links (Notion VA Command Center). Synced 2026-09-02. */
window.CC_META = {
  updated: "2026-09-02",
  agents: {
    front: [
      { name:"inbox-triage", desc:"Email triaging & reply drafting across all accounts" },
      { name:"copywriter", desc:"Cold email sequences, LinkedIn posts, campaign copy" },
      { name:"lead-prospector", desc:"Apollo searches, campaign create/pause, list building" },
      { name:"reply-handler", desc:"Inbound campaign replies, objections, Calendly bookings" },
      { name:"market-scout", desc:"Competitor research, industry trends" }
    ],
    back: [
      { name:"project-manager", desc:"Task rollups, tracking, daily/weekly management" },
      { name:"billing-auditor", desc:"Time tracking, invoices, monthly P&L" },
      { name:"onboarding-guide", desc:"New client setup, folders, onboarding checklist" },
      { name:"file-organizer", desc:"Folder structure, deduplication, file hygiene" },
      { name:"meeting-summarizer", desc:"Call transcripts → minutes & action items" }
    ],
    strategy: [
      { name:"cto", desc:"Evaluates tools vs the real stack (ADOPT/TRIAL/HOLD/KILL), designs builds, writes PRDs — builds only after sign-off. Owns the Tech Radar." }
    ],
    logs: {
      front:"https://app.notion.com/p/3ba811e21c7f8151ae20d4410907f860",
      back:"https://app.notion.com/p/3ba811e21c7f814496c4fd51a873f8a4"
    }
  },
  connectors: [
    { name:"Apollo", s:"ok", note:"Raw API keys (Satlas + Krishna) — not the MCP connector" },
    { name:"Smartlead", s:"ok", note:"Albert Scott account only" },
    { name:"PlusVibe (Satlas)", s:"ok", note:"Raw key + workspace_id — MCP connector is the WRONG account, never use for Satlas" },
    { name:"Instantly (Starfix)", s:"ok", note:"Separate from Satlas's dead account" },
    { name:"Pipedrive", s:"ok", note:"Albert Scott CRM" },
    { name:"Gmail (yeikkomae)", s:"ok", note:"Native connector — Calendar + Drive live too" },
    { name:"Gmail ×4 (work accts)", s:"ok", note:"Custom OAuth script — read + draft only" },
    { name:"Notion", s:"ok", note:"This workspace (VA Command Center)" },
    { name:"Fathom", s:"ok", note:"Meeting recordings — replaced Fireflies" },
    { name:"Porkbun", s:"ok", note:"25-domain Satlas inventory verified Aug 22" },
    { name:"Zapmail", s:"ok", note:"⚠ health 22.65/100, 0/30 warmed — live problem" },
    { name:"InboxKit", s:"ok", note:"15 domains / 30 mailboxes (Satlas)" },
    { name:"Hostinger (Starfix)", s:"ok", note:"3 domain tokens, not independently tested" },
    { name:"Satlas team Notion", s:"todo", note:"Different workspace — needs access" },
    { name:"HubSpot", s:"todo", note:"Needs authorizing in claude.ai settings" },
    { name:"Slack", s:"todo", note:"Needs authorizing" },
    { name:"Fireflies", s:"off", note:"Not needed — Fathom covers it (KILL on radar)" },
    { name:"Instantly (Satlas)", s:"off", note:"Deprecated — migrated off, key dead" },
    { name:"MillionVerifier", s:"off", note:"Manual 2FA by design" },
    { name:"Lemlist / LinkedIn", s:"off", note:"Browser-only, no API path" }
  ],
  techRadar: {
    adopt:["Apollo","Smartlead","PlusVibe","Instantly (Starfix)","Pipedrive","Notion","Fathom","Gmail ×5","Claude Code + 11 agents","Porkbun","InboxKit","Zapmail","Hostinger","MillionVerifier (manual)"],
    hold:["Higgsfield (0 credits, no use case)","HubSpot (until a client runs on it)","Slack"],
    kill:["Fireflies (Fathom won)","Instantly Satlas (dead key)"],
    expenseBase:"₱7,600/mo total — Claude ₱7,000 + iCloud ₱600; every client tool is client-paid"
  },
  resources: [
    { name:"🎛 VA Command Center (hub)", url:"https://app.notion.com/p/3ba811e21c7f8000b6a5f7952cb0c76b", group:"Notion" },
    { name:"📡 Tech Radar", url:"https://app.notion.com/p/3c7811e21c7f81d2814bef36e02b62f4", group:"Notion", local:"RESOURCES/Tech Radar.md" },
    { name:"🔌 Connector Status", url:"https://app.notion.com/p/3ba811e21c7f8193a87fd0e68c38987a", group:"Notion", local:".claude/agents/_shared/connector-status.md" },
    { name:"Upskill Materials", url:"https://app.notion.com/p/3c8811e21c7f80daa30efe94c3510a5c", group:"Notion" },
    { name:"Penji — Signal & ICP Tracker", url:"https://app.notion.com/p/3ca811e21c7f8152965be78cf622506e", group:"Notion" },
    { name:"SEO Prompt", url:"https://app.notion.com/p/3c5811e21c7f808d817ae41041bc3494", group:"Prompts" },
    { name:"Marketing Agent Prompt", url:"https://app.notion.com/p/3c4811e21c7f80aa9ed1f699922a4136", group:"Prompts" },
    { name:"Outbound Outreach", url:"https://app.notion.com/p/3c5811e21c7f80e4a17cc9a1685680fd", group:"Prompts" },
    { name:"Trading Agent Prompt", url:"https://app.notion.com/p/3c4811e21c7f80519116e4f715df0230", group:"Prompts" }
  ]
};

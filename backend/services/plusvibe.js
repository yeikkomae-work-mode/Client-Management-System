// PlusVibe REST client — one instance per workspace (Satlas, Sellervate, ...).
// Endpoint names below (account/list, campaign/list, etc.) come from this
// repo's own "Plusvibe Mailbox Health" notes (direct API pulls Eikko already
// runs manually) — verify against current PlusVibe API docs if they 404,
// since PlusVibe doesn't publish a single canonical reference the way
// Smartlead does.
const DEFAULT_BASE_URL = 'https://api.plusvibe.ai/api/v1';

async function plusvibeGet(baseUrl, apiKey, path, params = {}) {
  const url = new URL(baseUrl + path);
  url.searchParams.set('api_key', apiKey);
  for (const [k, v] of Object.entries(params)) {
    if (v !== undefined && v !== null) url.searchParams.set(k, v);
  }
  const res = await fetch(url, { signal: AbortSignal.timeout(15000) });
  if (!res.ok) {
    throw new Error(`PlusVibe ${path} failed: ${res.status} ${res.statusText}`);
  }
  return res.json();
}

/**
 * Pull a workspace-wide snapshot: campaign list + aggregate lead/reply totals.
 */
async function syncPlusVibeWorkspace({ apiKey, baseUrl, label, client }) {
  if (!apiKey) {
    return {
      label, client, connected: false, lastSynced: null,
      reason: `No API key configured for ${label}. Add it to backend/.env, then click Sync Now.`,
      totals: null, campaigns: [],
    };
  }

  const base = baseUrl || DEFAULT_BASE_URL;
  const campaignList = await plusvibeGet(base, apiKey, '/campaign/list');
  const campaigns = campaignList?.data || campaignList?.campaigns || campaignList || [];

  const totals = campaigns.reduce((acc, c) => {
    acc.leads += Number(c.total_leads ?? c.leads ?? 0);
    acc.contacted += Number(c.contacted ?? c.sent ?? 0);
    acc.replied += Number(c.replied ?? 0);
    acc.positive += Number(c.positive_reply ?? c.interested ?? 0);
    acc.bounced += Number(c.bounced ?? 0);
    return acc;
  }, { leads: 0, contacted: 0, replied: 0, positive: 0, bounced: 0 });

  return {
    label, client, connected: true, lastSynced: new Date().toISOString(),
    totals,
    campaigns: campaigns.slice(0, 25).map((c) => ({
      id: c.id ?? c.campaign_id, name: c.name ?? c.campaign_name, status: c.status,
    })),
  };
}

export { syncPlusVibeWorkspace };

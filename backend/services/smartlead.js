// Smartlead REST client — one instance per workspace (e.g. Albert Scott).
// Docs: https://server.smartlead.ai/api/v1 — auth via ?api_key= query param.
const BASE_URL = 'https://server.smartlead.ai/api/v1';

async function smartleadGet(apiKey, path, params = {}) {
  const url = new URL(BASE_URL + path);
  url.searchParams.set('api_key', apiKey);
  for (const [k, v] of Object.entries(params)) {
    if (v !== undefined && v !== null) url.searchParams.set(k, v);
  }
  const res = await fetch(url, { signal: AbortSignal.timeout(15000) });
  if (!res.ok) {
    throw new Error(`Smartlead ${path} failed: ${res.status} ${res.statusText}`);
  }
  return res.json();
}

/**
 * Pull a workspace-wide snapshot: campaign list + status counts + 30-day totals.
 * apiKey / label / client identify which workspace this is for in the merged response.
 */
async function syncSmartleadWorkspace({ apiKey, label, client }) {
  if (!apiKey) {
    return {
      label, client, connected: false, lastSynced: null,
      reason: `No API key configured for ${label}. Add it to backend/.env, then click Sync Now.`,
      totals: null, campaigns: [],
    };
  }

  const campaigns = await smartleadGet(apiKey, '/campaigns');
  const counts = { active: 0, paused: 0, completed: 0, drafted: 0, stopped: 0, total: campaigns.length };
  for (const c of campaigns) {
    const key = String(c.status || '').toLowerCase();
    if (key === 'active') counts.active++;
    else if (key === 'paused') counts.paused++;
    else if (key === 'completed') counts.completed++;
    else if (key === 'drafted') counts.drafted++;
    else if (key === 'stopped') counts.stopped++;
  }

  const end = new Date();
  const start = new Date(end.getTime() - 30 * 24 * 60 * 60 * 1000);
  const fmt = (d) => d.toISOString().slice(0, 10);

  let totals = null;
  try {
    const stats = await smartleadGet(apiKey, '/campaigns/overall-stats', {
      start_date: fmt(start), end_date: fmt(end),
    });
    const s = stats?.data?.overall_stats || stats?.overall_stats;
    if (s) totals = { sent: s.sent || 0, opened: s.opened || 0, replied: s.replied || 0, bounced: s.bounced || 0 };
  } catch (e) {
    console.warn(`[smartlead] overall-stats fetch failed for ${label}: ${e.message}`);
  }

  const activeFirst = [...campaigns].sort((a, b) => {
    const rank = (s) => (s === 'ACTIVE' ? 0 : s === 'PAUSED' ? 1 : s === 'DRAFTED' ? 2 : 3);
    return rank(a.status) - rank(b.status);
  });

  return {
    label, client, connected: true, lastSynced: new Date().toISOString(),
    range: { start: fmt(start), end: fmt(end) },
    totals, campaignCounts: counts,
    campaigns: activeFirst.slice(0, 25).map((c) => ({ id: c.id, name: c.name, status: c.status })),
  };
}

export { syncSmartleadWorkspace };

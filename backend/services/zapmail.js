// Zapmail REST client — domains + mailboxes for a workspace.
// Docs: https://docs.zapmail.ai (Bearer token auth). This is separate from
// the Zapmail Claude connector Eikko already has — the connector only works
// inside a Claude session, so the dashboard's own "Sync Now" button needs
// its own API key stored server-side.
const BASE_URL = 'https://api.zapmail.ai/api/v1';

async function zapmailGet(apiKey, path, params = {}) {
  const url = new URL(BASE_URL + path);
  for (const [k, v] of Object.entries(params)) {
    if (v !== undefined && v !== null) url.searchParams.set(k, v);
  }
  const res = await fetch(url, {
    headers: { Authorization: `Bearer ${apiKey}` },
    signal: AbortSignal.timeout(15000),
  });
  if (!res.ok) {
    throw new Error(`Zapmail ${path} failed: ${res.status} ${res.statusText}`);
  }
  return res.json();
}

/**
 * Pull domain + mailbox health for a workspace.
 */
async function syncZapmailWorkspace({ apiKey, label, client, workspace }) {
  if (!apiKey) {
    return {
      label, client, connected: false, lastSynced: null,
      reason: `No API key configured for ${label}. Add it to backend/.env, then click Sync Now.`,
      workspace, totalDomains: 0, totalMailboxes: 0, domains: [],
    };
  }

  const res = await zapmailGet(apiKey, '/domains', { limit: 100 });
  const domains = res?.data?.domains || res?.domains || [];

  const summarized = domains.map((d) => ({
    domain: d.domain,
    healthScore: Number(d.healthScore ?? 0),
    healthLabel: d.healthLabel || 'unknown',
    status: d.status,
    mailboxCount: Number(d.assignedMailboxesCount ?? (d.mailboxes || []).length),
    isWarmedUp: !!d.isWarmedUp,
  }));

  return {
    label, client, connected: true, lastSynced: new Date().toISOString(),
    workspace,
    totalDomains: summarized.length,
    totalMailboxes: summarized.reduce((s, d) => s + d.mailboxCount, 0),
    domains: summarized,
  };
}

export { syncZapmailWorkspace };

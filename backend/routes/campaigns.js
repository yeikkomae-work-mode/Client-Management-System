import express from 'express';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import { syncSmartleadWorkspace } from '../services/smartlead.js';
import { syncPlusVibeWorkspace } from '../services/plusvibe.js';
import { syncZapmailWorkspace } from '../services/zapmail.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const DASHBOARD_DIR = path.resolve(__dirname, '..', '..', '.claude-dashboard');
const JSON_FILE = path.join(DASHBOARD_DIR, 'campaigns-data.json');
const JS_FILE = path.join(DASHBOARD_DIR, 'campaigns-data.js');

const router = express.Router();

async function readCache() {
  try {
    const raw = await fs.readFile(JSON_FILE, 'utf8');
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

async function writeCache(data) {
  const payload = JSON.stringify(data, null, 2);
  await fs.writeFile(JSON_FILE, payload, 'utf8');
  await fs.writeFile(JS_FILE, `window.__CAMPAIGNS_DATA__ = ${payload};\n`, 'utf8');
}

// GET /api/campaigns/data — serve the last synced snapshot without hitting
// any external API. Cheap, used on page load.
router.get('/data', async (req, res) => {
  const cached = await readCache();
  if (!cached) {
    return res.status(404).json({ success: false, error: 'No campaign data synced yet' });
  }
  res.json({ success: true, data: cached });
});

// POST /api/campaigns/sync — live pull from every configured source. Sources
// without an API key in .env come back as connected:false with a plain-text
// reason instead of failing the whole sync.
router.post('/sync', async (req, res) => {
  try {
    const [smartleadAlbertScott, plusvibeSatlas, plusvibeSellervate, zapmailSatlas] = await Promise.all([
      syncSmartleadWorkspace({
        apiKey: process.env.SMARTLEAD_ALBERTSCOTT_API_KEY,
        label: 'Smartlead — Albert Scott (Yoni)',
        client: 'Yoni (Albert Scott)',
      }).catch((e) => ({ label: 'Smartlead — Albert Scott (Yoni)', client: 'Yoni (Albert Scott)', connected: false, reason: e.message, totals: null, campaigns: [] })),
      syncPlusVibeWorkspace({
        apiKey: process.env.PLUSVIBE_SATLAS_API_KEY,
        baseUrl: process.env.PLUSVIBE_SATLAS_BASE_URL,
        label: 'PlusVibe — Satlas',
        client: 'Chris Drew (Satlas)',
      }).catch((e) => ({ label: 'PlusVibe — Satlas', client: 'Chris Drew (Satlas)', connected: false, reason: e.message, totals: null, campaigns: [] })),
      syncPlusVibeWorkspace({
        apiKey: process.env.PLUSVIBE_SELLERVATE_API_KEY,
        baseUrl: process.env.PLUSVIBE_SELLERVATE_BASE_URL,
        label: 'PlusVibe — Sellervate',
        client: 'Cüneyt (Starfix)',
      }).catch((e) => ({ label: 'PlusVibe — Sellervate', client: 'Cüneyt (Starfix)', connected: false, reason: e.message, totals: null, campaigns: [] })),
      syncZapmailWorkspace({
        apiKey: process.env.ZAPMAIL_API_KEY,
        label: 'Zapmail — Domains & Mailboxes (Satlas)',
        client: 'Chris Drew (Satlas)',
        workspace: 'Satlas',
      }).catch((e) => ({ label: 'Zapmail — Domains & Mailboxes (Satlas)', client: 'Chris Drew (Satlas)', connected: false, reason: e.message, workspace: 'Satlas', totalDomains: 0, totalMailboxes: 0, domains: [] })),
    ]);

    const data = {
      generatedAt: new Date().toISOString(),
      syncMode: 'live',
      sources: {
        smartlead_albertscott: smartleadAlbertScott,
        plusvibe_satlas: plusvibeSatlas,
        plusvibe_sellervate: plusvibeSellervate,
        zapmail_domains: zapmailSatlas,
      },
    };

    await writeCache(data);
    res.json({ success: true, data });
  } catch (err) {
    console.error('[campaigns] sync failed:', err);
    res.status(500).json({ success: false, error: err.message || 'Sync failed' });
  }
});

export default router;

"""
Pull campaign stats from Dripify's Open API for the accounts documented in
RESOURCES/Tools & API Details/OAuth Credentials/dripify-api-keys-credentials.json.

API docs: https://help.dripify.com/en/articles/16664719-open-api
Base URL: https://api.dripify.com/v1/open-api
Auth: header "X-Api-Key: <key>"
Rate limit: 60 requests/min, 5000/day, per key.

Usage as a library:
    from dripify_stats import list_campaigns, campaign_statistics, campaign_lead_lists
    list_campaigns(api_key)
"""
import json
import os
import urllib.request

BASE = "https://api.dripify.com/v1/open-api"
DEFAULT_KEYFILE = os.path.join(
    os.path.dirname(__file__), "..", "OAuth Credentials",
    "dripify-api-keys-credentials.json",
)


def _get(path, api_key):
    # Cloudflare (fronting api.dripify.com) bans the default Python-urllib/x.x
    # User-Agent outright (error 1010, browser_signature_banned) -- always
    # send a normal one.
    req = urllib.request.Request(
        f"{BASE}{path}",
        headers={
            "X-Api-Key": api_key,
            "Accept": "application/json",
            "User-Agent": "curl/8.5.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def list_campaigns(api_key):
    return _get("/campaigns", api_key)["items"]


def campaign_statistics(api_key, campaign_id):
    return _get(f"/campaigns/{campaign_id}/statistics", api_key)


def campaign_lead_lists(api_key, campaign_id):
    return _get(f"/campaigns/{campaign_id}/lead-lists", api_key)["items"]


def load_accounts(keyfile=None):
    keyfile = keyfile or os.environ.get("DRIPIFY_KEYFILE", DEFAULT_KEYFILE)
    return json.load(open(keyfile))["accounts"]


def report_all(keyfile=None):
    """Print a quick status line per account, per campaign."""
    for name, info in load_accounts(keyfile).items():
        key = info["api_key"]
        try:
            campaigns = list_campaigns(key)
        except Exception as e:
            print(f"{name}: ERROR {e}")
            continue
        if not campaigns:
            print(f"{name}: no campaigns")
            continue
        for c in campaigns:
            stats = campaign_statistics(key, c["id"])
            print(
                f"{name} — {c['name']} (id {c['id']}, {c['status']}): "
                f"{stats['totalLeads']} leads, {stats['contactedLeads']} contacted, "
                f"acceptance {stats['acceptanceRate']:.1f}% ({stats['acceptanceRateLeads']}), "
                f"reply {stats['replyRate']:.1f}% ({stats['replyRateLeads']}), "
                f"breakdown={stats['leadStatusBreakdown']}"
            )


if __name__ == "__main__":
    report_all()

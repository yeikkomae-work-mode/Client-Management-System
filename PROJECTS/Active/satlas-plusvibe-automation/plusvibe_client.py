"""Thin client for the PlusVibe API used by the Satlas reporting scripts.

PlusVibe sits behind Cloudflare, which blocks requests carrying no/default
User-Agent (e.g. plain urllib or requests without headers) with a bare 403.
Every call here sends a normal browser-shaped User-Agent to avoid that.
"""
import os
import time
import requests

BASE = "https://api.plusvibe.ai/api/v1"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) SatlasReportingScript/1.0"}


class PlusVibeError(RuntimeError):
    pass


class PlusVibeClient:
    def __init__(self, api_key: str | None = None, workspace_id: str | None = None):
        self.api_key = api_key or os.environ["PLUSVIBE_API_KEY"]
        self.workspace_id = workspace_id or os.environ["PLUSVIBE_WORKSPACE_ID"]

    def _get(self, path: str, **params):
        params = {"api_key": self.api_key, "workspace_id": self.workspace_id, **params}
        for attempt in range(3):
            resp = requests.get(f"{BASE}/{path}", params=params, headers=UA, timeout=20)
            if resp.status_code == 200:
                return resp.json()
            if attempt < 2:
                time.sleep(1.5 * (attempt + 1))
        raise PlusVibeError(f"GET {path} failed: {resp.status_code} {resp.text[:300]}")

    def campaigns(self) -> list[dict]:
        """All campaigns in the workspace, any status."""
        return self._get("campaign/list")

    def active_campaigns(self) -> list[dict]:
        return [c for c in self.campaigns() if c.get("status") == "ACTIVE"]

    def campaign_stats(self, campaign_id: str, start_date: str, end_date: str) -> dict:
        """start_date/end_date as YYYY-MM-DD. Returns {} if no data for the range."""
        data = self._get(
            "campaign/stats",
            campaign_id=campaign_id,
            start_date=start_date,
            end_date=end_date,
        )
        if isinstance(data, list):
            return data[0] if data else {}
        return data or {}

    def accounts(self) -> list[dict]:
        """All mailbox accounts in the workspace (id, email, status, warmup_status, ...)."""
        data = self._get("account/list")
        return data.get("accounts", data if isinstance(data, list) else [])

    def inbox_health_summary(self) -> dict:
        accounts = self.accounts()
        total = len(accounts)
        active = sum(1 for a in accounts if a.get("status") == "ACTIVE")
        warmup_active = sum(1 for a in accounts if a.get("warmup_status") == "ACTIVE")
        return {
            "total": total,
            "active": active,
            "warmup_active": warmup_active,
            "summary": f"{active}/{total} accounts active, {warmup_active}/{total} warmup active",
        }

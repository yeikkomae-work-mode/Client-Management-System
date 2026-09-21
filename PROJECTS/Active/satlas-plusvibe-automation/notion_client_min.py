"""Minimal Notion client for the monthly KPI row write.

Needs its own internal integration secret (NOTION_TOKEN in .env) —
this is separate from any Claude/Notion chat connector, since a headless
script can't reuse a chat session's connector auth. Create one at
notion.so/my-integrations, then add it to the "Satlas" page and the
"Apollo Email Performance" database via Connections before this will work.
"""
import os
import requests

NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"


class NotionError(RuntimeError):
    pass


class NotionMinClient:
    def __init__(self):
        self.token = os.environ["NOTION_TOKEN"]
        self.data_source_id = os.environ["NOTION_EMAIL_KPI_DATA_SOURCE_ID"]
        self.client_page_url = os.environ["NOTION_SATLAS_CLIENT_PAGE_URL"]
        self.service_engagement_url = os.environ["NOTION_SERVICE_ENGAGEMENT_URL"]

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def create_email_kpi_row(self, *, title: str, date_start: str, date_end: str,
                              total_sent: int, total_contacted: int, total_replies: int,
                              positive_replies: int, bounce_rate: float, inbox_health: str,
                              mailboxes_live: int, notes: str,
                              apollo_credits: float | None = None,
                              plusvibe_credits: float | None = None,
                              millionverifier_credits: float | None = None) -> dict:
        properties = {
            "Email KPI": {"title": [{"text": {"content": title}}]},
            "Date": {"date": {"start": date_start, "end": date_end}},
            "Total sent": {"number": total_sent},
            "Total contacted": {"number": total_contacted},
            "Total replies": {"number": total_replies},
            "Positive replies": {"number": positive_replies},
            "Bounce rate": {"number": bounce_rate},
            "Inbox health": {"rich_text": [{"text": {"content": inbox_health}}]},
            "Mailboxes live": {"number": mailboxes_live},
            "Notes": {"rich_text": [{"text": {"content": notes}}]},
            "🏢 Client": {"relation": [{"id": self._url_to_id(self.client_page_url)}]},
            "Service Engagement": {"relation": [{"id": self._url_to_id(self.service_engagement_url)}]},
        }
        if apollo_credits is not None:
            properties["Apollo credits"] = {"number": apollo_credits}
        if plusvibe_credits is not None:
            properties["PlusVibe credits"] = {"number": plusvibe_credits}
        if millionverifier_credits is not None:
            properties["MillionVerifier credits"] = {"number": millionverifier_credits}

        payload = {
            "parent": {"data_source_id": self.data_source_id},
            "properties": properties,
        }
        resp = requests.post(f"{API_BASE}/pages", json=payload, headers=self._headers(), timeout=20)
        if resp.status_code >= 300:
            raise NotionError(f"create page failed: {resp.status_code} {resp.text[:500]}")
        return resp.json()

    @staticmethod
    def _url_to_id(url: str) -> str:
        """Extracts a bare Notion page/database id (with dashes) from a notion.so URL."""
        raw = url.rstrip("/").split("/")[-1].split("?")[0].split("-")[-1]
        raw = raw[-32:]
        return f"{raw[0:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:32]}"

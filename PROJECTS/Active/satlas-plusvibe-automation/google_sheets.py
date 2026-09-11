"""Minimal Google Sheets client: refreshes the stored OAuth token and does
value reads/writes via the raw REST API. No google-api-python-client
dependency needed for what these scripts do.
"""
import os
import urllib.parse
import requests

TOKEN_URL = "https://oauth2.googleapis.com/token"
SHEETS_BASE = "https://sheets.googleapis.com/v4/spreadsheets"


class SheetsClient:
    def __init__(self):
        self.client_id = os.environ["GOOGLE_CLIENT_ID"]
        self.client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
        self.refresh_token = os.environ["GOOGLE_REFRESH_TOKEN"]
        self.spreadsheet_id = os.environ["SATLAS_SHEET_ID"]
        self._access_token = None

    def _token(self) -> str:
        if self._access_token:
            return self._access_token
        resp = requests.post(TOKEN_URL, data={
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token",
        }, timeout=15)
        resp.raise_for_status()
        self._access_token = resp.json()["access_token"]
        return self._access_token

    def _headers(self):
        return {"Authorization": f"Bearer {self._token()}", "Content-Type": "application/json"}

    def read(self, a1_range: str) -> list[list]:
        rng = urllib.parse.quote(a1_range, safe="")
        url = f"{SHEETS_BASE}/{self.spreadsheet_id}/values/{rng}"
        resp = requests.get(url, headers=self._headers(), timeout=20)
        resp.raise_for_status()
        return resp.json().get("values", [])

    def write(self, a1_range: str, values: list[list]):
        """Overwrites the given range with values (USER_ENTERED, so formulas/% work)."""
        rng = urllib.parse.quote(a1_range, safe="")
        url = f"{SHEETS_BASE}/{self.spreadsheet_id}/values/{rng}?valueInputOption=USER_ENTERED"
        resp = requests.put(url, json={"values": values}, headers=self._headers(), timeout=20)
        resp.raise_for_status()
        return resp.json()

    def append(self, a1_range: str, values: list[list]):
        """True append — finds the next empty row itself, never overwrites."""
        rng = urllib.parse.quote(a1_range, safe="")
        url = f"{SHEETS_BASE}/{self.spreadsheet_id}/values/{rng}:append?valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS"
        resp = requests.post(url, json={"values": values}, headers=self._headers(), timeout=20)
        resp.raise_for_status()
        return resp.json()

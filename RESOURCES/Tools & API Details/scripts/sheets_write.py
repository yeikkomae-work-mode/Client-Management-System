"""
Append rows to a Google Sheet via the service-account credential documented
in RESOURCES/Tools & API Details/Connected Tools Status.md.

Requires: pip install google-auth google-api-python-client
Requires: the target sheet shared as Editor with the service account's
client_email (see the credential JSON).

Usage as a library:
    from sheets_write import append_rows
    append_rows(spreadsheet_id, "Tab Name", [[...], [...]])
"""
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build

DEFAULT_KEYFILE = os.path.join(
    os.path.dirname(__file__), "..", "OAuth Credentials",
    "google-service-account-cms-sheets-writer-credentials.json",
)
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def _service(keyfile=None):
    keyfile = keyfile or os.environ.get("GOOGLE_SHEETS_SA_KEYFILE", DEFAULT_KEYFILE)
    creds = service_account.Credentials.from_service_account_file(keyfile, scopes=SCOPES)
    return build("sheets", "v4", credentials=creds, cache_discovery=False)


def get_tabs(spreadsheet_id, keyfile=None):
    svc = _service(keyfile)
    meta = svc.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    return [
        {"gid": s["properties"]["sheetId"], "title": s["properties"]["title"]}
        for s in meta.get("sheets", [])
    ]


def append_rows(spreadsheet_id, tab_name, rows, value_range="A:Z", keyfile=None):
    """rows: list of lists, one per row. Appends after the last row with data."""
    svc = _service(keyfile)
    return svc.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"'{tab_name}'!{value_range}",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body={"values": rows},
    ).execute()

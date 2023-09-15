import json
import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import SPREADSHEET_ID, SHEET_RANGE, SCOPES


def authenticate_google_sheets():
    creds_data = json.loads(os.getenv('TOKEN'))
    creds = Credentials.from_authorized_user_info(creds_data, SCOPES)
    return creds


def write_to_google_sheet(creds, data):
    service = build('sheets', 'v4', credentials=creds)

    body = {
        'values': data
    }

    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_RANGE,
        valueInputOption='RAW',
        body=body
    ).execute()

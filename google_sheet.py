import gspread
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

CREDENTIALS_FILE = 'credentials.json'
TOKEN_PICKLE = 'token.pickle'

def authenticate_google_sheets():
    creds = None
    if os.path.exists(TOKEN_PICKLE):
        with open(TOKEN_PICKLE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open(TOKEN_PICKLE, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def save_emails_to_sheet(emails):
    try:
        creds = authenticate_google_sheets()
        client = gspread.authorize(creds)
        spreadsheet = client.open("Email List")
        worksheet = spreadsheet.get_worksheet(0)
        current_data = worksheet.get_all_values()
        next_row = len(current_data) + 1
        for email in emails:
            worksheet.update_cell(next_row, 1, email)
            next_row += 1
    except Exception as e:
        print(f"Error saving to Google Sheet: {e}")

def delete_emails_from_sheet(emails):
    try:
        creds = authenticate_google_sheets()
        client = gspread.authorize(creds)
        spreadsheet = client.open("Email List")
        worksheet = spreadsheet.get_worksheet(0)
        existing_emails = worksheet.col_values(1)  # Assuming emails are in the first column
        for email in emails:
            if email in existing_emails:
                cell = worksheet.find(email)
                worksheet.delete_rows(cell.row)
    except Exception as e:
        print(f"Error deleting from Google Sheet: {e}")

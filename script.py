from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle

# The scope of the access request, which corresponds to the actions you want to perform
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The path to your credentials.json file
CREDENTIALS_FILE = 'credentials.json'

# Token file to store the user's access and refresh tokens
TOKEN_PICKLE = 'token.pickle'

creds = None

# Check if the token file exists
if os.path.exists(TOKEN_PICKLE):
    with open(TOKEN_PICKLE, 'rb') as token:
        creds = pickle.load(token)

# If no valid credentials, authenticate the user
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=8080)  # Ensure this matches the registered URI

    # Save the credentials for the next run
    with open(TOKEN_PICKLE, 'wb') as token:
        pickle.dump(creds, token)

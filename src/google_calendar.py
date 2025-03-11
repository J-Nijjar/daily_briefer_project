from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import datetime
import os
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    creds = None
    token_path = 'src/token.json'
    credentials_path = 'src/credentials.json'  # Adjust this if needed

    # Load existing token
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If credentials are invalid or missing, re-authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=8080, prompt='consent')

        # Save credentials for future use
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds


def get_meetings():
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    tdelta = datetime.timedelta(days=1)
    tomorrow = datetime.datetime.utcnow() + tdelta
    form_tomorrow = tomorrow.isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='primary',
        timeMin = now,
        timeMax = form_tomorrow,
        singleEvents = True,
        orderBy='startTime'
    ).execute()

    event = events_result.get('items', [])

    events_list = []

    if not event:
        events_list.append('You have no events scheduled today.')
    else:
        for events in event:
            start = events['start'].get('dateTime', events['start'].get('date'))
            events_list.append([start, events['summary']])

    return events_list

# get_meetings()

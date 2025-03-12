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
            # Parse the ISO datetime string and convert it to a more readable format
            start_time = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z")
            readable_time = start_time.strftime("%I:%M %p")  # e.g., 10:30 AM
            events_list.append([readable_time, events['summary']])

    events_str = "\n".join([
        f"{begin}: {title}" for begin, title in events_list
    ])

    return events_list

def get_meetings_as_plain_text():
    events_result = get_meetings()

    events_text = ""

    if not events_result:
        events_text = "- You have no events scheduled for today."
    
    else:
        events_str = "\n".join([
        f"{begin}: {title}" for begin, title in events_result])
        
    return events_str

def get_meetings_as_html():
    events_result = get_meetings()

    events_html = ""

    if not events_result:
        events_html = "<li>You have no events scheduled for today.</li>"
    else:
        for event in events_result:
            start = event[0]
            title = event[1]
            events_html += f"<li><strong>{start}</strong>: {title}</li>"

    return events_html
   
# get_meetings()
# print(get_meetings_as_html())
# print(get_meetings_as_plain_text())

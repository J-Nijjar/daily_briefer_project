import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def fetch_todays_events():
    """Fetches the the start, name, and ending of the day's events from the
    user's calendar.
    """
    creds = None

    # Token.json file stores user's access and refresh token, and is created
    # automatically when the authorization flow complets for the first time.

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json", SCOPES
        )
    # If there are no (valid) credentials available, the user logs in.

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the credentials for the new run
        with open("token.json", 'w') as token:
            token.write(creds.to_json())
    
    try:
        service = build("calendar", 'v3', credentials=creds)

        # Call the calendar API
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = (
            service.events().list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        ).execute()

        )
        events = events_result.get("items", [])

        if not events:
          print("No upcoming events found.")
          return

        for event in events:
            start = event['start'].get("datetime", event['start'].get("date"))
            print(start, event['summary'])
    
    except HttpError as error:
        print(f"An error has occurred: {error}")


fetch_todays_events()
        

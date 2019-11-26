# If modifying these scopes, delete the file token.pickle.
from __future__ import print_function
import datetime
import pickle
import os.path
from Event import Event
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import tkinter as tk

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def getAPI():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    #if os.path.exists('token.pickle'):
     #   with open('token.pickle', 'rb') as token:
      #      creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def printEvents(service, numOfEvents, outputBox):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    outputBox.append('Getting the upcoming ' + str(numOfEvents) + ' events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=numOfEvents, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    #  if not events:
    #     outputBox.insert(tk.END, links.get_text())
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        outputBox.append(event['summary'])


def AddEvent(service, outputBox, Event, startDateTime):
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.
    # startDateTime = Event.date + 'T' + Event.startTime
    # endDateTime = Event.date + 'T' + Event.endTime
    Event.description = Event.description + '\n' + Event.link
    event = {
        'summary': Event.name,
        'location': Event.location,
        'description': Event.description,
        'start': {
            # 'dateTime': '2019-11-30T09:00:00-07:00',
            'dateTime': startDateTime,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': startDateTime,
            # 'dateTime': '2019-11-30T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    outputBox.append('Event created: %s' % (event.get('htmlLink')))
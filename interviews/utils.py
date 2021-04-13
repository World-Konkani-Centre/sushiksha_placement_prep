import pickle
import datetime
import os
from smtplib import SMTPException

from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

from django.core.mail import send_mail


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    cred = None

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print(e)
        return None


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt


CLIENT_SECRET_FILE = 'interviews/secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']


# service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

def google_calendar_set_interview1v1(interview):
    # service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    credentials = pickle.load(open('interviews/token_calendar_v3.pickle', 'rb'))
    service = build(API_NAME, API_VERSION, credentials=credentials)
    timezone = 'Asia/Kolkata'
    event = {
        'summary': f'{interview.heading}--{interview.type}',
        'location': interview.link,
        'description': interview.description,
        'start': {
            'dateTime': interview.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': interview.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'attendees': [
            {'email': interview.participant_1.email},
            {'email': interview.participant_2.email},
        ],
        'reminders': {
            'useDefault': True,
        },
    }
    respone = service.events().insert(calendarId='primary', body=event).execute()
    return respone['id']


def google_calendar_cancel_interview1v1(interview):
    # service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    credentials = pickle.load(open('interviews/token_calendar_v3.pickle', 'rb'))
    service = build(API_NAME, API_VERSION, credentials=credentials)
    service.events().delete(calendarId='primary', eventId=interview.event_id).execute()


def send_interview_cancel_email(interview):
    try:
        send_mail(
            subject = 'Cancelled -- Mock Interview with sushiksha mentor',
            message=f'{interview.heading} -- {interview.description}',
            from_email=None,
            recipient_list = [f'{interview.participant_2.email}', f'{interview.participant_1.email}'],
            fail_silently=False,
        )
    except SMTPException:
        send_mail(
            subject='Cancelled -- Mock Interview with sushiksha mentor ',
            message=f'{interview.heading} -- {interview.description}',
            from_email=None,
            recipient_list = [f'{interview.participant_1.email}'],
            fail_silently=False,
        )

def send_interview_set_email(interview):
    send_mail(
        subject='Interview set up -- Mock Interview with sushiksha mentor',
        message=f'{interview.heading} -- {interview.description}',
        from_email=None,
        recipient_list=[f'{interview.participant_2.email}', f'{interview.participant_1.email}'],
        fail_silently=False,
    )
import datetime
import os
import pickle

from django.contrib.sites.models import Site


from django.core.mail import send_mail
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

from sushiksha_placement_prep.settings import BASE_DIR

pickle_file = os.path.join(BASE_DIR, 'interviews/token_calendar_v3.pickle')


def Create_Service(client_secret_file, api_name, api_version, *scopes):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    cred = None

    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = Flow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            flow.redirect_uri = "http://localhost:8000/callback"
            cred = flow.credentials

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


CLIENT_SECRET_FILE = os.path.join(BASE_DIR, 'interviews/secret.json')
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']


# service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

def google_calendar_set_interview1v1(interview):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    # credentials = pickle.load(open(pickle_file, 'rb'))
    # service = build(API_NAME, API_VERSION, credentials=credentials)
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
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    # credentials = pickle.load(open(pickle_file, 'rb'))
    # service = build(API_NAME, API_VERSION, credentials=credentials)
    if interview.event_id:
        service.events().delete(calendarId='primary', eventId=interview.event_id).execute()


def send_interview_cancel_email(interview):
    if interview.participant_2:
        send_mail(
            subject='Cancelled -- Mock Interview with sushiksha mentor',
            message=f'{interview.heading} -- {interview.description}',
            from_email=None,
            recipient_list=[f'{interview.participant_2.email}', f'{interview.participant_1.email}'],
            fail_silently=False,
        )
    else:
        send_mail(
            subject='Cancelled -- Mock Interview with sushiksha mentor ',
            message=f'{interview.heading} -- {interview.description}',
            from_email=None,
            recipient_list=[f'{interview.participant_1.email}'],
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


def send_gd_cancel_email(interview):
    li = []
    if interview.participant_1 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_2 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_3 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_4 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_5 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_6 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_7 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_8 is not None:
        li.append(interview.participant_1.email)
    if interview.participant_9 is not None:
        li.append(interview.participant_1.email)
    send_mail(
        subject='GD Interview cancelled up -- Mock Interview with sushiksha mentor',
        message=f'{interview.heading} -- {interview.description}',
        from_email=None,
        recipient_list=li,
        fail_silently=False,
    )


def send_gd_set_email(interview, user):
    send_mail(
        subject='GD Interview set up -- Mock Interview with sushiksha mentor',
        message=f'{interview.heading} -- {interview.description}',
        from_email=None,
        recipient_list=[f'{user.email}'],
        fail_silently=False,
    )


def set_gd_event(interview, user):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    # credentials = pickle.load(open(pickle_file, 'rb'))
    # service = build(API_NAME, API_VERSION, credentials=credentials)
    timezone = 'Asia/Kolkata'
    event = {
        'summary': f'{interview.heading}--GD',
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
            {'email': user.email},
        ],
        'reminders': {
            'useDefault': True,
        },
    }
    response = service.events().insert(calendarId='primary', body=event).execute()
    return response['id']


def update_gd_event(interview, user):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    # credentials = pickle.load(open(pickle_file, 'rb'))
    # service = build(API_NAME, API_VERSION, credentials=credentials)
    event = service.events().get(calendarId='primary', eventId=interview.event_id).execute()
    attendees = event['attendees']
    attendees.append({'email': user.email})
    event['attendees'] = attendees
    updated_event = service.events().update(calendarId='primary', eventId=interview.event_id, body=event).execute()
    return updated_event['updated']

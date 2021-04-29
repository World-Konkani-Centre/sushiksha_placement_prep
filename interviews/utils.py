import os

import httplib2
from django.core.mail import send_mail
from django.template import loader
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

from sushiksha_placement_prep import settings


from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from google.oauth2 import service_account


service_account_email = settings.SERVICE_EMAIL

from sushiksha_placement_prep.settings import BASE_DIR

CLIENT_SECRET_FILE = os.path.join(BASE_DIR, 'interviews/secret.json')
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']


def Create_Service():
    credentials = service_account.Credentials. \
        from_service_account_file(CLIENT_SECRET_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(service_account_email)
    service = discovery.build('calendar', 'v3', credentials=delegated_credentials)
    return service


def google_calendar_set_interview1v1(interview):
    service = Create_Service()
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
    service = Create_Service()
    if interview.event_id:
        service.events().delete(calendarId='primary', eventId=interview.event_id).execute()


def send_interview_cancel_email(interview):
    if interview.type == 'HR':
        interview_type = 'hr'
    else:
        interview_type = 'tech'

    html_message = loader.render_to_string(
        'mail/template.html',
        {
            'name': interview.participant_1.profile.name,
            'content': 'The Below Interview has been canceled',
            'interview_type': f'{interview.heading} -- {interview.type}',
            'interview_date': f'{interview.start_time.strftime("%I:%M %p")} -- {interview.end_time.strftime("%I:%M %p")} ({interview.end_time.strftime("%A, %x")})',
            'interview_description': interview.description,
            'interview_location': interview.link,
            'interview_time': 'Asia/Kolkata',
            'link': f'https://scopea.konkanischolarship.com/interview/{interview_type}/view/{interview.id}'
        }
    )

    subject = f'CANCELED : {interview.heading} - {interview.start_time.strftime("%I:%M %p, %A, %x")} - {interview.type}'

    if interview.participant_2:
        html_message = loader.render_to_string(
        'mail/template.html',
        {
            'content': 'The Below Interview has been canceled',
            'interview_type': f'{interview.heading} -- {interview.type}',
            'interview_date': f'{interview.start_time.strftime("%I:%M %p")} -- {interview.end_time.strftime("%I:%M %p")} ({interview.end_time.strftime("%A, %x")})',
            'interview_description': interview.description,
            'interview_location': interview.link,
            'interview_time': 'Asia/Kolkata',
            'link': f'https://scopea.konkanischolarship.com/interview/{interview_type}/view/{interview.id}'
        }
    )
        send_mail(
            subject=subject,
            message=subject,
            from_email=None,
            recipient_list=[f'{interview.participant_2.email}', f'{interview.participant_1.email}'],
            html_message=html_message,
            fail_silently=False,
        )
    else:
        send_mail(
            subject=subject,
            message=subject,
            from_email=None,
            recipient_list=[f'{interview.participant_1.email}'],
            html_message=html_message,
            fail_silently=False,
        )


def send_interview_set_email(interview):
    if interview.type == 'HR':
        interview_type = 'hr'
    else:
        interview_type = 'tech'

    html_message = loader.render_to_string(
        'mail/template.html',
        {
            'content': 'A new Mock Interview has been scheduled.',
            'interview_type': f'{interview.heading} -- {interview.type}',
            'interview_date': f'{interview.start_time.strftime("%I:%M %p")} -- {interview.end_time.strftime("%I:%M %p")} ({interview.end_time.strftime("%A, %x")})',
            'interview_description': interview.description,
            'interview_location': interview.link,
            'interview_time': 'Asia/Kolkata',
            'link': f'https://scopea.konkanischolarship.com/interview/{interview_type}/view/{interview.id}'
        }
    )

    subject = f'NEW INTERVIEW : {interview.heading} -- {interview.start_time.strftime("%I:%M %p, %A, %x")} -- {interview.type}'

    send_mail(
        subject=subject,
        message=subject,
        from_email=None,
        recipient_list=[f'{interview.participant_2.email}', f'{interview.participant_1.email}'],
        html_message=html_message,
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

    html_message = loader.render_to_string(
        'mail/template.html',
        {
            'content': 'The Below GD Interview has been canceled',
            'interview_type': f'{interview.heading} -- GD',
            'interview_date': f'{interview.start_time.strftime("%I:%M %p")} -- {interview.end_time.strftime("%I:%M %p")} ({interview.end_time.strftime("%A, %x")})',
            'interview_description': interview.description,
            'interview_location': interview.link,
            'interview_time': 'Asia/Kolkata',
            'link': f'https://scopea.konkanischolarship.com/interview/hr/view/{interview.id}'
        }
    )

    subject = f'CANCELED : {interview.heading} -- {interview.start_time.strftime("%I:%M %p, %A, %x")} -- GD'
    

    send_mail(
        subject=subject,
        message=subject,
        from_email=None,
        recipient_list=li,
        html_message=html_message
        fail_silently=False,
    )


def send_gd_set_email(interview, user):

    html_message = loader.render_to_string(
        'mail/template.html',
        {
            'name': f'{user.profile.name}',
            'content': 'A new GD Interview has been scheduled. ',
            'interview_type': f'{interview.heading} -- GD',
            'interview_date': f'{interview.start_time.strftime("%I:%M %p")} -- {interview.end_time.strftime("%I:%M %p")} ({interview.end_time.strftime("%A, %x")})',
            'interview_description': interview.description,
            'interview_location': interview.link,
            'interview_time': 'Asia/Kolkata',
            'link': f'https://scopea.konkanischolarship.com/interview/hr/view/{interview.id}'
        }
    )

    subject = f'NEW GD INTERVIEW : {interview.heading} -- {interview.start_time.strftime("%I:%M %p, %A, %x")} -- GD'

    send_mail(
        subject=subject,
        message=subject,
        from_email=None,
        recipient_list=[f'{user.email}'],
        html_message=html_message,
        fail_silently=False,
    )


def set_gd_event(interview, user):
    service = Create_Service()
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
    service = Create_Service()
    event = service.events().get(calendarId='primary', eventId=interview.event_id).execute()
    attendees = event['attendees']
    attendees.append({'email': user.email})
    event['attendees'] = attendees
    updated_event = service.events().update(calendarId='primary', eventId=interview.event_id, body=event).execute()
    return updated_event['updated']

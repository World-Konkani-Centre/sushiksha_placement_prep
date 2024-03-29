from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from datetime import datetime


from interviews.models import Branch, Interview, GD
from interviews.utils import google_calendar_set_interview1v1, google_calendar_cancel_interview1v1, \
    send_interview_cancel_email, send_interview_set_email, send_gd_set_email, update_gd_event, send_gd_cancel_email
from resume_builder.models import Resume
# from .tables import InterviewTable
from badge.models import Badge, Reward
from sushiksha_placement_prep.settings import APTITUDE_BADGE_ID, RESUME_BADGE_ID, HR_BADGE_ID, GD_BADGE_ID, \
    TECHNICAL_BADGE_ID


@login_required
def hr_interview_list(request):
    interviews_completed = Interview.objects.filter(
        Q(participant_2=request.user) | Q(participant_1=request.user) & Q(complete=True), type='HR')
    interviews_scheduled = Interview.objects.filter(Q(type="HR") & Q(start_time__gte = datetime.now())).order_by('start_time')
    context = {
        'interviews_completed': interviews_completed,
        'interviews_scheduled': interviews_scheduled,
        'heading': "HR interviews",
        'whatIS': 'hr'
    }
    return render(request, 'interviews/list.html', context)


@login_required
def hr_interview_details(request, intId):
    interview = Interview.objects.get(id=intId)
    technical = Reward.objects.filter(badge=Badge.objects.get(id=TECHNICAL_BADGE_ID), user=request.user.profile)
    gd = Reward.objects.filter(badge=Badge.objects.get(id=GD_BADGE_ID), user=request.user.profile)
    if request.POST:
        val = request.POST.get('hidden_option')
        if val == '0':
            send_interview_cancel_email(interview)
            google_calendar_cancel_interview1v1(interview)
            if request.user == interview.participant_1:
                messages.success(request, f'The interview has been cancelled and same is informed to the other')
                interview.delete()
            else:
                interview.participant_2 = None
                interview.complete = False
                interview.event_id = None
                messages.success(request, f'The interview has been cancelled and same is informed to the other')
                interview.save()
        elif val == '1':
            #  if len(technical) == 0 or len(gd) == 0:
            #   messages.error(request,
            #                 f'Please complete your your technical and gd interviews for eligibility of HR interviews')
            #   return redirect('hr-interviews-list')
            interview.participant_2 = request.user
            interview.complete = True
            interview.save()
            send_interview_set_email(interview)
            eventId = google_calendar_set_interview1v1(interview)
            interview.event_id = eventId
            interview.save()
            messages.success(request,
                             f'The interview has been set up and same is informed to the other along with the google '
                             f'calendar, accept the google calendar link for further notification')
        return redirect('interviews-list')
    context = {
        'interview': interview,
        'heading': "HR interview detail"
    }
    return render(request, 'interviews/single.html', context)


@login_required
def interview_list(request):
    interviews_completed = Interview.objects.filter(
        Q(participant_2=request.user) | Q(participant_1=request.user) & Q(complete=True), type="Technical")
    interviews_scheduled = Interview.objects.filter(Q(type="Technical") & Q(start_time__gte = datetime.now())).order_by('start_time')  
    context = {
        'interviews_completed': interviews_completed,
        'interviews_scheduled': interviews_scheduled,
        'heading': "Technical interviews",
        'whatIS': 'tech',
    }
    return render(request, 'interviews/list.html', context)


@login_required
def interview_details(request, intId):
    interview = Interview.objects.get(id=intId)
    res = Reward.objects.filter(user=request.user.profile, badge=Badge.objects.get(id=RESUME_BADGE_ID))
    aptitude = Reward.objects.filter(user=request.user.profile, badge=Badge.objects.get(id=APTITUDE_BADGE_ID))
    if request.POST:
        val = request.POST.get('hidden_option')
        if val == '0':
            send_interview_cancel_email(interview)
            google_calendar_cancel_interview1v1(interview)
            if request.user == interview.participant_1:
                messages.success(request, f'The interview has been cancelled and same is informed to the other')
                interview.delete()
            else:
                interview.participant_2 = None
                interview.complete = False
                interview.event_id = None
                messages.success(request, f'The interview has been cancelled and same is informed to the other')
                interview.save()
        elif val == '1':
            if len(res) == 0 or len(aptitude) == 0:
                messages.error(request,
                               f'Please complete your your resume and aptitude test for being eligible for Technical '
                               f'interviews')
                return redirect('interviews-list')
            interview.participant_2 = request.user
            interview.complete = True
            interview.save()
            send_interview_set_email(interview)
            eventId = google_calendar_set_interview1v1(interview)
            interview.event_id = eventId
            interview.save()
            messages.success(request,
                             f'The interview has been set up and same is informed to the other along with the google '
                             f'calendar, accept the google calendar link for further notification')
        return redirect('interviews-list')
    context = {
        'interview': interview,
        'heading': "Technical Interview details"
    }
    return render(request, 'interviews/single.html', context)


@login_required
def gd_apply(request):
    gd_completed = GD.objects.filter(
        Q(participant_2=request.user) | Q(participant_1=request.user) | Q(participant_3=request.user) | Q(
            participant_4=request.user) | Q(participant_5=request.user) | Q(participant_6=request.user) | Q(
            participant_7=request.user) | Q(participant_8=request.user) | Q(participant_9=request.user), complete=True)
    gd_scheduled = GD.objects.filter(complete=False)
    context = {
        'interviews_completed': gd_completed,
        'interviews_scheduled': gd_scheduled,
    }
    return render(request, 'interviews/gd-list.html', context)


@login_required
def gd_interview_details(request, intId):
    interview = GD.objects.get(id=intId)
    context = {
        'interview': interview
    }
    res = Reward.objects.filter(user=request.user.profile, badge=Badge.objects.get(id=RESUME_BADGE_ID))
    aptitude = Reward.objects.filter(user=request.user.profile, badge=Badge.objects.get(id=APTITUDE_BADGE_ID))
    if request.POST:
        val = request.POST.get('hidden_option')
        if val == '0':
            if request.user == interview.participant_1:
                send_gd_cancel_email(interview)
                google_calendar_cancel_interview1v1(interview)
                messages.success(request, f'The interview has been cancelled and same is informed to the other')
                interview.delete()
            else:
                messages.error(request, "invalid operation by non mentor")
        elif val == '1':
            if len(res) == 0 or len(aptitude) == 0:
                messages.error(request,
                               f'Please complete your your resume and aptitude test for being eligible for interviews')
                return redirect('gd-interviews-list')
            if interview.count == 10:
                messages.error(request, "slot is full")
                return redirect('gd-interviews-list')
            if interview.participant_2 is None:
                interview.participant_2 = request.user
            elif interview.participant_3 is None:
                interview.participant_3 = request.user
            elif interview.participant_4 is None:
                interview.participant_4 = request.user
            elif interview.participant_5 is None:
                interview.participant_5 = request.user
            elif interview.participant_6 is None:
                interview.participant_6 = request.user
            elif interview.participant_7 is None:
                interview.participant_7 = request.user
            elif interview.participant_8 is None:
                interview.participant_8 = request.user
            elif interview.participant_9 is None:
                interview.participant_9 = request.user
            else:
                messages.error(request, f'Slot is full please try some other slot')
                return redirect('gd-interviews-list')
            interview.count = interview.count + 1
            if interview.count == 10:
                interview.complete = True
            interview.save()
            send_gd_set_email(interview, request.user)
            update_gd_event(interview, request.user)
            messages.success(request,
                             f'The interview has been set up')
        return redirect('gd-interviews-list')
    return render(request, 'interviews/gd-single.html', context)


def interview_home(request):
    return render(request, 'interviews/interviews-home.html')


def counselling_home(request):
    return render(request, 'interviews/counselling-home.html')


@login_required
def counselling_list(request):
    interviews_completed = Interview.objects.filter(
        (Q(participant_2=request.user) | Q(participant_1=request.user)) & Q(complete=True) &
        ~(Q(type="HR") | Q(type="Technical")))
    interviews_scheduled = Interview.objects.filter(Q(complete=False) & ~(
            Q(type="HR") | Q(type="Technical")))
    context = {
        'interviews_completed': interviews_completed,
        'interviews_scheduled': interviews_scheduled,
        'heading': "Counselling Sessions",
        'whatIS': 'counsel',
        'counselling': True
    }
    return render(request, 'interviews/list.html', context)


@login_required
def counselling_details(request, intId):
    interview = Interview.objects.get(id=intId)
    if request.POST:
        val = request.POST.get('hidden_option')
        if val == '0':
            send_interview_cancel_email(interview)
            google_calendar_cancel_interview1v1(interview)
            if request.user == interview.participant_1:
                messages.success(request, f'The interview has been cancelled and same is informed to the other')
                interview.delete()
            else:
                interview.participant_2 = None
                interview.complete = False
                interview.event_id = None
                messages.success(request, f'The interview has been cancelled and same is informed to the other')
                interview.save()
        elif val == '1':
            interview.participant_2 = request.user
            interview.complete = True
            interview.save()
            send_interview_set_email(interview)
            eventId = google_calendar_set_interview1v1(interview)
            interview.event_id = eventId
            interview.save()
            messages.success(request,
                             f'The interview has been set up and same is informed to the other along with the google '
                             f'calendar, accept the google calendar link for further notification')
        return redirect('interviews-list')
    context = {
        'interview': interview,
        'heading': "Counselling session details",
        'counselling': True
    }
    return render(request, 'interviews/single.html', context)

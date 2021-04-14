from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from interviews.forms import GDCreationForm, GDParticipationForm
from interviews.models import Interview, GDList
from interviews.utils import google_calendar_set_interview1v1, google_calendar_cancel_interview1v1, \
    send_interview_cancel_email, send_interview_set_email


@login_required
def interview_list(request):
    interviews_completed = Interview.objects.filter(Q(participant_2=request.user) | Q(participant_1=request.user) & Q(complete=True))
    interviews_scheduled = Interview.objects.filter(complete=False)
    context = {
        'interviews_completed': interviews_completed,
        'interviews_scheduled': interviews_scheduled,
    }
    return render(request, 'interviews/list.html', context)


@login_required
def interview_details(request, intId):
    interview = Interview.objects.get(id=intId)
    if request.POST:
        val = request.POST.get('hidden_option')
        if val == '0':
            send_interview_cancel_email(interview)
            google_calendar_cancel_interview1v1(interview)
            if request.user.profile.is_mentor:
                messages.success(request,f'The interview has been cancelled and same is informed to the other')
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
            messages.success(request, f'The interview has been set up and same is informed to the other along with '
                                      f'the google calendar, accept the google calendar link for further notification')
        return redirect('interviews-list')
    context = {
        'interview': interview
    }
    return render(request, 'interviews/single.html', context)


@login_required
def gd_apply(request):
    form = None
    lists = GDList.objects.filter(complete=False)
    if request.POST:
        if request.user.profile.is_mentor:
            form = GDCreationForm(request.POST)
            if form.is_valid():
                heading = form.heading
                start = form.start_time
                end = form.end_time
                description = form.description
                link = form.link
                attendees = form.attendees
                print(heading)
                print(start)
                print(end)
                print(description)
                print(link)
                print(attendees)
                return redirect('gd-interviews-list')
        else:
            form = GDParticipationForm(request.POST)
            if form.is_valid():
                s = form.save(commit=False)
                s.participants = request.user
                s.save()
                return redirect('gd-interviews-list')
    else:
        if request.user.profile.is_mentor:
            form = GDCreationForm()
        else:
            form = GDParticipationForm()
    context = {
        'form': form,
        'lists':lists,
        }
    return render(request, 'interviews/list.html', context)


@login_required
def gd_interview_details(request, intId):
    interview = GDList.objects.get(id=intId)
    context = {
        'interview': interview
    }
    return render(request, 'interviews/single.html', context)

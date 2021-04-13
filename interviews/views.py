from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from interviews.forms import InterviewRegisterForm, GDCreationForm, GDParticipationForm
from interviews.models import Interview, GDList

from interviews.utils import google_calendar


@login_required
def interview_list(request):
    form = None
    lists = Interview.objects.filter(complete=False)
    if request.POST:
        if request.user.profile.is_mentor:
            form = InterviewRegisterForm(request.POST)
            if form.is_valid():
                interview = form.save(commit=False)
                interview.participant_1 = request.user
                interview.save()
                return redirect('interviews-list')
    else:
        if request.user.profile.is_mentor:
            form = InterviewRegisterForm()
    context = {
        'form': form,
        'lists': lists,
    }
    return render(request, 'interviews/list.html', context)


@login_required
def interview_details(request, intId):
    interview = Interview.objects.get(id=intId)
    if request.POST:
        interview.participant_2 = request.user
        interview.complete = True
        interview.save()
        eventId = google_calendar(interview)
        # google_calendar(interview)
        interview.event_id = eventId
        interview.save()
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

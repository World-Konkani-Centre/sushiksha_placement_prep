from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from interviews.forms import InterviewRegisterForm
from interviews.models import Interview

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
        interview.event_id = eventId
        interview.save()
        return redirect('interviews-list')
    context = {
        'interview': interview
    }
    return render(request, 'interviews/single.html', context)

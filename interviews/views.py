from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


from interviews.models import Interview, GD
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
    gd_completed = GD.objects.filter(Q(participant_2=request.user) | Q(participant_1=request.user) | Q(participant_3=request.user) | Q(participant_4=request.user) | Q(participant_5=request.user) | Q(participant_6=request.user) | Q(participant_7=request.user) | Q(participant_8=request.user) | Q(participant_9=request.user))
    gd_scheduled = GD.objects.filter(~Q(participant_2=request.user) & ~Q(participant_1=request.user) & ~Q(participant_3=request.user) & ~Q(participant_4=request.user) & ~Q(participant_5=request.user) & ~Q(participant_6=request.user) & ~Q(participant_7=request.user) & ~Q(participant_8=request.user) & ~Q(participant_9=request.user))
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
    if request.POST:
        return HttpResponse('Service not available now', status=401)
    return render(request, 'interviews/gd-single.html', context)

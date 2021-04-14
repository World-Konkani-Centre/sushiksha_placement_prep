from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from interviews.forms import InterviewRegisterForm
from interviews.utils import send_interview_cancel_email, send_interview_set_email, google_calendar_set_interview1v1, \
    google_calendar_cancel_interview1v1
from resume_builder.forms import ResumeModelForm, CommentModelForm
from resume_builder.models import Resume, Comments
from users.models import Profile
from interviews.models import Interview


@login_required
def resume_list(request):
    query = Resume.objects.all()
    context = {
        'query': query,
        'heading': 'Resumes',
    }
    return render(request, 'mentors-panel/resume-list.html', context=context)


@login_required
def resume_view_user(request):
    resume = Resume.objects.filter(user=request.user).first()
    if resume:
        return redirect('resume-view', resumeId=resume.id)
    else:
        return HttpResponseNotFound("You have not submitted any resume for review")


@login_required
def resume_view(request, resumeId):
    resume = Resume.objects.get(id=resumeId)
    p = Profile.objects.get(user=request.user)
    if request.method == 'GET':
        comments = Comments.objects.filter(resume=resume).order_by('-id')
        if p.is_mentor:
            form_r = ResumeModelForm(instance=resume)
            form_c = CommentModelForm()
            context = {
                'resume': resume,
                'form_r': form_r,
                'form_c': form_c,
                'heading': 'Resume',
                'comments': comments
            }
            return render(request, 'mentors-panel/resume-single.html', context=context)
        else:
            form_c = CommentModelForm()
            context = {
                'resume': resume,
                'form_c': form_c,
                'heading': 'Resume',
                'comments': comments
            }
            return render(request, 'mentors-panel/resume-single.html', context=context)
    elif request.method == 'POST':
        if p.is_mentor:
            form_r = ResumeModelForm(request.POST, instance=resume)
            form_c = CommentModelForm(request.POST)
            if form_r.is_valid():
                form_r.save()
                messages.success(request, f'Resume has been changed successfully')
            if form_c.is_valid():
                comm = form_c.save(commit=False)
                comm.resume = resume
                comm.user = request.user
                comm.save()
                messages.success(request, f'comment has been posted successfully')
            return redirect('resume-list')
        else:
            form_c = CommentModelForm(request.POST)
            if form_c.is_valid():
                comm = form_c.save(commit=False)
                comm.resume = resume
                comm.user = request.user
                comm.save()
                messages.success(request, f'comment has been posted successfully')
            else:
                messages.error(request, f'something wrong in the input')
                return redirect('resume-view', resumeId=resumeId)


def interview_list(request):
    form = None
    interviews_completed = Interview.objects.filter(Q(participant_2=request.user) | Q(participant_1=request.user),
                                                    complete=True)
    interviews_scheduled = Interview.objects.filter(Q(participant_2=request.user) | Q(participant_1=request.user),
                                                    complete=False)
    if request.POST:
        if request.user.profile.is_mentor:
            form = InterviewRegisterForm(request.POST)
            if form.is_valid():
                interview = form.save(commit=False)
                interview.participant_1 = request.user
                interview.save()
                messages.success(request, f'New Interview has been scheduled successfully')
                return redirect('interview-list-mentor')
            else:
                messages.error(request, f'something wrong in the input')
    else:
        if request.user.profile.is_mentor:
            form = InterviewRegisterForm()
    context = {
        'form': form,
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
                             f'The interview has been set up and same is informed to the other along with the google calendar, accept the google calendar link for further notification')
        return redirect('interviews-list')
    context = {
        'interview': interview
    }
    return render(request, 'interviews/single.html', context)

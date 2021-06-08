from datetime import datetime
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

# from interviews.forms import InterviewRegisterForm
from interviews.utils import send_interview_cancel_email, send_interview_set_email, google_calendar_set_interview1v1, \
    google_calendar_cancel_interview1v1, send_gd_cancel_email, send_gd_set_email, update_gd_event, set_gd_event
from mentors_panel.forms import MultiInterviewScheduleForm
from mentors_panel.utils import create_schedule
from resume_builder.forms import ResumeModelForm, CommentModelForm
from resume_builder.models import Resume, Comments
from users.models import Profile
from interviews.models import Interview, GD
from interviews.forms import GDCreationForm
from users.models import Profile
from badge.models import Reward, Badge
from sushiksha_placement_prep.settings import APTITUDE_BADGE_ID, RESUME_BADGE_ID


@login_required
def resume_list(request):
    if request.user.profile.is_mentor:
        query = Resume.objects.all().filter(user__profile__is_mentor=False)
        context = {
            'query': query,
            'heading': 'Resumes',
        }
        return render(request, 'mentors-panel/resume-list.html', context=context)
    else:
        return HttpResponse("Unauthorized", 401)


@login_required
def resume_view_user(request):
    resume = Resume.objects.filter(user=request.user).first()
    if resume:
        return redirect('resume-view', resumeId=resume.id)
    else:
        messages.error("You have not submitted any resume for review.")
        return redirect('resume-home')


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
                'comments': comments,
                'user': resume.user,
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
                if form_r.cleaned_data.get('status') == "3":
                    if len(Reward.objects.filter(user=resume.user.profile,
                                                 badge_id=RESUME_BADGE_ID)) == 0:
                        badge_obj = get_object_or_404(Badge, id=RESUME_BADGE_ID)
                        Reward.objects.create(user=resume.user.profile,
                                              description="A badge for your completed Resume",
                                              awarded_by="ADMIN", badge=badge_obj)
                messages.success(request, f'Resume review has been submitted')

            if form_c.is_valid():
                comm = form_c.save(commit=False)
                comm.resume = resume
                comm.user = request.user
                comm.save()
                messages.success(request, f'Review has been posted successfully')
            return redirect('resume-list')
        else:
            form_c = CommentModelForm(request.POST)
            if form_c.is_valid():
                comm = form_c.save(commit=False)
                comm.resume = resume
                comm.user = request.user
                comm.save()
                messages.success(request, f'Comment has been posted successfully')
            else:
                messages.error(request, f'something wrong in the input')
                return redirect('resume-view', resumeId=resumeId)


@login_required
def interview_list(request):
    if request.user.profile.is_mentor:
        form = None
        interviews_completed = Interview.objects.filter(Q(participant_1=request.user),
                                                        complete=True)
        interviews_scheduled = Interview.objects.filter(Q(participant_1=request.user),
                                                        complete=False)
        if request.POST:
            if request.user.profile.is_mentor:
                form = MultiInterviewScheduleForm(request.POST)
                if form.is_valid():
                    branch = form.cleaned_data['branch']
                    int_type = form.cleaned_data['type']
                    link = form.cleaned_data['link']
                    start_date = form.cleaned_data['start_date']
                    end_date = form.cleaned_data['end_date']
                    start_time = form.cleaned_data['st_start_time']
                    end_time = form.cleaned_data['st_end_time']
                    schedule = create_schedule(start_date, end_date, start_time, end_time)
                    for s in schedule:
                        Interview.objects.create(type=int_type, branch=branch,
                                                 link=link, participant_1=request.user, start_time=s[0], end_time=s[1])
                    messages.success(request, f'New Interview has been scheduled successfully')
                    return redirect('interview-list-mentor')
                else:
                    messages.error(request, f'something wrong in the input')
        else:
            if request.user.profile.is_mentor:
                form = MultiInterviewScheduleForm()
        context = {
            'form': form,
            'heading': 'Interviews',
            'interviews_completed': interviews_completed,
            'interviews_scheduled': interviews_scheduled,

        }
        return render(request, 'interviews/list.html', context)
    else:
        return HttpResponse("Unauthorized", 401)


@login_required
def interview_details(request, intId):
    if request.user.profile.is_mentor:
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
                                 f'The interview has been set up and same is informed to the other along with the '
                                 f'google calendar, accept the google calendar link for further notification')
            return redirect('interview-list-mentor')
        context = {
            'interview': interview,
            'heading': "Technical Interview details"
        }
        if interview.type == 'Counselling':
            context = {
                'interview': interview,
                'heading': "Counselling session details",
                'counselling': True
            }
        return render(request, 'interviews/single.html', context)
    else:
        return HttpResponse("Unauthorized", 401)


@login_required
def gd_list(request):
    if request.user.profile.is_mentor:
        form = GDCreationForm(request.POST or None)
        gd_completed = GD.objects.filter(Q(participant_1=request.user), complete=True)
        gd_scheduled = GD.objects.filter(Q(participant_1=request.user), complete=False)
        if request.POST:
            if form.is_valid():
                gd_obj = form.save(commit=False)
                gd_obj.participant_1 = request.user
                gd_obj.end_time = gd_obj.start_time + timedelta(hours=1)
                gd_obj.count = gd_obj.count + 1
                eventId = set_gd_event(gd_obj, request.user)
                gd_obj.event_id = eventId
                gd_obj.save()
                messages.success(request, f'New GD Interview has been scheduled successfully')
                return redirect('gd-list-mentor')
            else:
                messages.error(request, f'something wrong in the input')
        context = {
            'form': form,
            'interviews_completed': gd_completed,
            'interviews_scheduled': gd_scheduled,
        }
        return render(request, 'interviews/gd-list.html', context)
    else:
        return HttpResponse("Unauthorized", 401)


@login_required
def gd_details(request, intId):
    if request.user.profile.is_mentor:
        interview = GD.objects.get(id=intId)
        context = {
            'interview': interview
        }
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
                    messages.error(request, "slot is full")
                interview.count = interview.count + 1
                if interview.count == 10:
                    interview.complete = True
                interview.save()
                send_gd_set_email(interview, request.user)
                update_gd_event(interview, request.user)
                messages.success(request,
                                 f'The interview has been set up and same is informed to the other along with the '
                                 f'google calendar, accept the google calendar link for further notification')
            return redirect('gd-list-mentor')
        return render(request, 'interviews/gd-single.html', context)
    else:
        return HttpResponse("Unauthorized", 401)


@login_required
def mentors_home(request):
    if not request.user.profile.is_mentor:
        messages.error(request, "You don't have access to view this page :)")
        return redirect('index')

    return render(request, 'mentors-panel/mentors-home.html')


@login_required
def profile_list(request):
    if not request.user.profile.is_mentor:
        messages.error(request, "You don't have access to view this page :)")
        return redirect('index')

    data = Profile.objects.all().filter(is_mentor=False)
    context = {
        'data': data,
    }
    return render(request, 'mentors-panel/profile-list.html', context=context)


@login_required
def profile_detail(request, id):
    if not request.user.profile.is_mentor:
        messages.error(request, "You don't have access to view this page :)")
        return redirect('index')

    user = get_object_or_404(Profile, id=id)
    badges = Reward.objects.filter(user=user).values('badge__title', 'badge__image').annotate(Count('badge__title'))
    context = {
        'user': user,
        'badges': badges,
    }
    return render(request, 'mentors-panel/profile-detail.html', context=context)

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from interviews.forms import InterviewRegisterForm
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
            if form_c.is_valid():
                comm = form_c.save(commit=False)
                comm.resume = resume
                comm.user = request.user
                comm.save()
            return redirect('resume-list')
        else:
            form_c = CommentModelForm(request.POST)
            if form_c.is_valid():
                comm = form_c.save(commit=False)
                comm.resume = resume
                comm.user = request.user
                comm.save()
                return redirect('resume-view', resumeId=resumeId)


def interview_list(request):
    form = None
    interviews = Interview.objects.filter(Q(participant_1=request.user) | Q(participant_2=request.user) | Q(complete=False))
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
        'lists': interviews,
    }
    return render(request, 'interviews/list.html', context)
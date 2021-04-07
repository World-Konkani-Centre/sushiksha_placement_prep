from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from resume_builder.forms import ResumeModelForm, CommentModelForm
from resume_builder.models import Resume, Comments
from users.models import Profile


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

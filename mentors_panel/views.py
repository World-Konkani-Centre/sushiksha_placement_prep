from django.http import HttpResponse
from django.shortcuts import redirect, render

from resume_builder.forms import ResumeModelForm, CommentModelForm
from resume_builder.models import Resume, Comments
from users.models import Profile

count = 14


def resume_list(request):
    if request.user.profile.is_mentor:
        query = Resume.objects.all()
        context = {
            'query': query,
            'heading': 'Resumes',
        }
        return render(request, 'mentors-panel/resume-list.html', context=context)
    else:
        return HttpResponse('Unauthorized', status=401)


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
                'form_c':form_c,
                'heading': 'Resume',
                'comments': comments
            }
            return render(request, 'mentors-panel/resume-single.html', context=context)
        else:
            return HttpResponse('Unauthorized', status=401)
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
            return HttpResponse('Unauthorized', status=401)

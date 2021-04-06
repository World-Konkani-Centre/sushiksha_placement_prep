from django.http import HttpResponse
from django.shortcuts import redirect, render

from resume_builder.forms import ResumeModelForm
from resume_builder.models import Resume
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
        if p.is_mentor or resume.user == request.user:
            form = ResumeModelForm(instance=resume)
            context = {
                'resume': resume,
                'form': form,
                'heading': 'Resume',
            }
            return render(request, 'mentors-panel/resume-single.html', context=context)
    elif request.method == 'POST':
        form = ResumeModelForm(request.POST,instance=resume)
        if form.is_valid():
            form.save()
            return  redirect('resume-list')
    else:
        return HttpResponse('Unauthorized', status=401)

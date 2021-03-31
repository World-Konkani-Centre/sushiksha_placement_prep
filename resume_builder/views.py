import json

from django.shortcuts import render, redirect

# Create your views here.
from resume_builder.forms import EducationFormSet, InternshipJobFormSet, ProjectFormSet, AchievementFormSet, \
    OtherFormSet, SkillFormSet
from resume_builder.utils import education_is_valid, skills_is_valid, internships_job_is_valid, projects_is_valid, \
    achievement_is_valid, other_is_valid


def test(request):
    education = None
    skills = None
    internships_job = None
    projects = None
    achievement = None
    other = None
    if request.method == 'GET':
        education = EducationFormSet(request.GET or None)
        skills = SkillFormSet(request.GET or None)
        internships_job = InternshipJobFormSet(request.GET or None)
        projects = ProjectFormSet(request.GET or None)
        achievement = AchievementFormSet(request.GET or None)
        other = OtherFormSet(request.GET or None)
    elif request.method == 'POST':
        val = dict(request.POST.lists())
        counts = [int(val['edFormCount'][0]), int(val['skFormCount'][0]), int(val['prFormCount'][0]),
                  int(val['ijFormCount'][0]),
                  int(val['achFormCount'][0]), int(val['othFormCount'][0])]
        start = 5
        end = start + (4 * int(counts[0]))
        education_is_valid(request.POST, start, end)
        skills_is_valid(val['form-0-sk_name'], val['form-0-sk_expertise'])
        projects_is_valid(val['form-0-p_name'], val['form-0-p_start_date'], val['form-0-p_end_date'], val['form-0'
                                                                                                          '-p_description'])
        internships_job_is_valid(val['form-0-ij_role'], val['form-0-ij_company'], val['form-0-ij_description'])
        achievement_is_valid(val['form-0-a_name'])
        other_is_valid(val['form-0-o_name'])
        return redirect("test")
    context = {
        'heading': "Build the Resume",
        'education': education,
        'skills': skills,
        'internships_job': internships_job,
        'projects': projects,
        'achievement': achievement,
        'other': other,
    }
    return render(request, 'resume-builder/test.html', context=context)

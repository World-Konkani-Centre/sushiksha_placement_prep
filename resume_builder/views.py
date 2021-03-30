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
        counts = request.POST['form-TOTAL_FORMS']
        education = EducationFormSet(request.POST)
        education_is_valid(education)
        internships_job = InternshipJobFormSet(request.POST)
        projects = ProjectFormSet(request.POST)
        achievement = AchievementFormSet(request.POST)
        other = OtherFormSet(request.POST)
        skills_is_valid(skills)
        internships_job_is_valid(internships_job)
        projects_is_valid(projects)
        achievement_is_valid(achievement)
        other_is_valid(other)
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

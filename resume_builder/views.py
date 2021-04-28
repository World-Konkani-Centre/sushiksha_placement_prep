from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from resume_builder.forms import ContactModelForm, SkillModelForm, EducationModelForm, \
    InternshipFormExperienceForm, TrainingCertificationForm, ProjectForm, ExtraModelForm, LanguageModelForm, \
    AchievementModelForm
from resume_builder.models import Contact, Skill, Education, InternshipExperience, TrainingCertification, \
    Project, Extra, Language, Achievement, Template, Resume

count = 10


@login_required
def contact(request):
    try:
        contact = Contact.objects.get(user=request.user)
    except Contact.DoesNotExist:
        contact = None
    if request.method == 'GET':
        form = ContactModelForm(instance=contact)
        context = {
            'heading': "Update the Contact Information",
            'form': form,
            'next': 'resume-skills',
            'width': 100 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ContactModelForm(request.POST, instance=contact)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your contact information has been updated')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-contact')

#
# @login_required
# def obj(request):
#     obj = Objective.objects.filter(user=request.user)
#     if request.method == 'GET':
#         form = ObjectiveModelForm()
#         context = {
#             'heading': "Add new Objective Information",
#             'form': form,
#             'obj': obj,
#             'prev': 'resume-contact',
#             'next': 'resume-skills',
#             'width': 200 / count,
#         }
#         return render(request, 'resume-builder/one_entry.html', context=context)
#     elif request.method == 'POST':
#         form = ObjectiveModelForm(request.POST)
#         if form.is_valid():
#             row = form.save(commit=False)
#             row.user = request.user
#             form.save()
#             messages.success(request, f'Your objectives information has been created')
#         else:
#             messages.error(request, f'Something is wrong in your input')
#         return redirect('resume-obj')
#
#
# @login_required
# def obj_edit(request, id):
#     skill = Objective.objects.get(user=request.user, id=id)
#     if request.method == 'GET':
#         form = ObjectiveModelForm(instance=skill)
#         context = {
#             'heading': "Update the Objectives Information",
#             'form': form,
#         }
#         return render(request, 'resume-builder/one_entry.html', context=context)
#     elif request.method == 'POST':
#         form = ObjectiveModelForm(request.POST, instance=skill)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your objectives information has been updated')
#         else:
#             messages.error(request, f'Something is wrong in your input')
#         return redirect('resume-obj')
#
#
# @login_required
# def obj_delete(request, id):
#     skill = Objective.objects.get(id=id, user=request.user).delete()
#     messages.success(request, f'Your objectives information has been deleted')
#     return redirect('resume-obj')
#

@login_required
def skills(request):
    skill = Skill.objects.filter(user=request.user)
    if request.method == 'GET':
        form = SkillModelForm()
        context = {
            'heading': "Add new Skills Information",
            'form': form,
            'skills': skill,
            'prev': 'resume-contact',
            'next': 'resume-education',
            'width': 300 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = SkillModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your skill information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-skills')


@login_required
def skills_edit(request, id):
    skill = Skill.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = SkillModelForm(instance=skill)
        context = {
            'heading': "Update the Skills Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = SkillModelForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your skill information has been updated')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-skills')


@login_required
def skills_delete(request, id):
    skill = Skill.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your skill information has been deleted')
    return redirect('resume-skills')


@login_required
def education(request):
    ed = Education.objects.filter(user=request.user)
    if request.method == 'GET':
        form = EducationModelForm()
        context = {
            'heading': "Add new Education Information",
            'form': form,
            'education': ed,
            'prev': 'resume-skills',
            'next': 'resume-internship',
            'width': 400 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = EducationModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your education information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-education')


@login_required
def education_edit(request, id):
    educaiton = Education.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = EducationModelForm(instance=educaiton)
        context = {
            'heading': "Update the Education Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = EducationModelForm(request.POST, instance=educaiton)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your education information has been updated')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-education')


@login_required
def education_delete(request, id):
    education_obj = Education.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your education information has been deleted')
    return redirect('resume-education')


@login_required
def internship(request):
    ie = InternshipExperience.objects.filter(user=request.user)
    if request.method == 'GET':
        form = InternshipFormExperienceForm()
        context = {
            'heading': "Add new Internship Information",
            'form': form,
            'internship': ie,
            'prev': 'resume-education',
            'next': 'resume-training',
            'width': 500 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = InternshipFormExperienceForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your internship information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-internship')


@login_required
def internship_edit(request, id):
    internship = InternshipExperience.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = InternshipFormExperienceForm(instance=internship)
        context = {
            'heading': "Update the Education Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = InternshipFormExperienceForm(request.POST, instance=internship)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your internship information has been updated')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-internship')


@login_required
def internship_delete(request, id):
    intern = InternshipExperience.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your internship information has been deleted')
    return redirect('resume-internship')


@login_required
def training(request):
    train = TrainingCertification.objects.filter(user=request.user)
    if request.method == 'GET':
        form = TrainingCertificationForm()
        context = {
            'heading': "Add new Training Information",
            'form': form,
            'training': train,
            'prev': 'resume-internship',
            'next': 'resume-project',
            'width': 600 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = TrainingCertificationForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your training information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-training')


@login_required
def training_edit(request, id):
    train = TrainingCertification.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = TrainingCertificationForm(instance=train)
        context = {
            'heading': "Update the training Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = TrainingCertificationForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your training information has been edited')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-training')


@login_required
def training_delete(request, id):
    intern = TrainingCertification.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your training information has been deleted')
    return redirect('resume-training')


@login_required
def project(request):
    proj = Project.objects.filter(user=request.user)
    if request.method == 'GET':
        form = ProjectForm()
        context = {
            'heading': "Add new Project Information",
            'form': form,
            'projects': proj,
            'prev': 'resume-training',
            'next': 'resume-extra',
            'width': 700 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your project information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-project')


@login_required
def project_edit(request, id):
    proj = Project.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = ProjectForm(instance=proj)
        context = {
            'heading': "Update the Project Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your project information has been edited')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-project')


@login_required
def project_delete(request, id):
    proj = Project.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your project information has been deleted')
    return redirect('resume-project')


def extra(request):
    if request.method == 'GET':
        extra_obj = Extra.objects.filter(user=request.user)
        form = ExtraModelForm()
        context = {
            'heading': "Update the Extra Curricular Information",
            'form': form,
            'extra': extra_obj,
            'prev': 'resume-project',
            'next': 'resume-language',
            'width': 800 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ExtraModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your extra curricular information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-extra')


@login_required
def extra_edit(request, id):
    lang = Extra.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = ExtraModelForm(instance=lang)
        context = {
            'heading': "Update the Extra Curricular Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = ExtraModelForm(request.POST, instance=lang)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your extra curricular information has been edited')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-extra')


@login_required
def extra_delete(request, id):
    lang = Extra.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your extra curricular information has been deleted')
    return redirect('resume-extra')


@login_required
def language(request):
    lang = Language.objects.filter(user=request.user)
    if request.method == 'GET':
        form = LanguageModelForm()
        context = {
            'heading': "Add new Language Information",
            'form': form,
            'lang': lang,
            'prev': 'resume-extra',
            'next': 'resume-achievement',
            'width': 900 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = LanguageModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your language information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-language')


@login_required
def language_edit(request, id):
    lang = Language.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = LanguageModelForm(instance=lang)
        context = {
            'heading': "Update the Language Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = LanguageModelForm(request.POST, instance=lang)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your language information has been edited')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-language')


@login_required
def language_delete(request, id):
    lang = Language.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your language information has been deleted')
    return redirect('resume-language')


@login_required
def achievement(request):
    if request.method == 'GET':
        ach = Achievement.objects.filter(user=request.user)
        form = AchievementModelForm()
        context = {
            'heading': "Update the Achievements Information",
            'form': form,
            'ach': ach,
            'prev': 'resume-language',
            'width': 1000 / count,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = AchievementModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your achievement information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-achievement')


@login_required
def achievement_edit(request, id):
    lang = Achievement.objects.get(user=request.user, id=id)
    if request.method == 'GET':
        form = AchievementModelForm(instance=lang)
        context = {
            'heading': "Update the Achievement Information",
            'form': form,
        }
        return render(request, 'resume-builder/one_entry.html', context=context)
    elif request.method == 'POST':
        form = AchievementModelForm(request.POST, instance=lang)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your achievement information has been edited')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('resume-achievement')


@login_required
def achievement_delete(request, id):
    lang = Achievement.objects.get(id=id, user=request.user).delete()
    messages.success(request, f'Your achievement information has been deleted')
    return redirect('resume-achievement')


@login_required
def preview(request):
    if request.method == 'POST':
        tid = request.POST.get('ip')
        temp = Template.objects.get(id=tid)
        res, created = Resume.objects.get_or_create(user=request.user)
        res.template = temp
        res.status = '1'
        res.save()
        messages.success(request, f'Resume has been sent to review stay tuned for the update')
        return redirect('resume-preview')
    if request.method == 'GET':
        query = Template.objects.all()
        return render(request, 'resume-builder/view.html', context={'query': query})


@login_required
def preview_template(request):
    if request.is_ajax():
        templateId = (request.headers.get('templateId'))
        userId = (request.headers.get('userId'))
        try:
            resumeId = request.headers.get('resumeId')
            resume = Resume.objects.get(id=resumeId)
            userId = resume.user.id
            templateId = resume.template.id
        except Resume.DoesNotExist:
            pass
        template = Template.objects.get(id=templateId)
        user = User.objects.get(id=userId)
        contact_obj = Contact.objects.filter(user=user).first()
        # objectives_obj = Objective.objects.filter(user=user)
        skills_obj = Skill.objects.filter(user=user)
        education_obj = Education.objects.filter(user=user)
        ie_obj = InternshipExperience.objects.filter(user=user)
        training_obj = TrainingCertification.objects.filter(user=user)
        proj_obj = Project.objects.filter(user=user)
        extra_obj = Extra.objects.filter(user=user)
        lang_obj = Language.objects.filter(user=user)
        achievement_obj = Achievement.objects.filter(user=user)
        loc = f'resume-builder/{template.template}'
        context = {
            'contact': contact_obj,
            # 'objectives': objectives_obj,
            'skills': skills_obj,
            'education': education_obj,
            'ie': ie_obj,
            'training': training_obj,
            'projects': proj_obj,
            'extras': extra_obj,
            'language': lang_obj,
            'achievement': achievement_obj,
        }
        return render(request, loc, context=context)


def resume_home(request):
    return render(request, 'resume-builder/resume-home.html')
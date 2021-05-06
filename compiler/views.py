import json

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponse
import sushiksha_placement_prep.settings as se
from compiler.models import Question, DSACategory,  SubCategory
from django.shortcuts import get_object_or_404

API_ENDPOINT = "https://api.jdoodle.com/v1/execute"

LANG_CODE = {'c': 1, 'java': 3, 'cpp14': 3, 'python3': 3, 'go': 3, 'php': 3, 'perl': 3, 'ruby': 3, 'scala': 3,
             'bash': 3, 'r': 3,
             'csharp': 3, 'dart': 3, 'nodejs': 3, 'kotlin': 2}


@login_required
def q_all(request):
    questions = Question.objects.all()
    cat = DSACategory.objects.all()
    context = {
        'heading': "DSA Question list",
        'questions': questions,
        'cat': cat,
    }
    return render(request, 'compiler/all_questions.html', context=context)


@login_required
def question_single(request, qid):
    question = get_object_or_404(Question, id=qid)
    context = {
        'heading': "Question",
        'question': question,
    }
    return render(request, 'compiler/question.html', context=context)


@login_required
def category(request, cid):
    cat = get_object_or_404(DSACategory, id=cid)
    subcat = SubCategory.objects.filter(category=cat)
    question = Question.objects.filter(sub_cat__category=cat)
    context = {
        'heading': "Category",
        'category': cat,
        'subcat': subcat,
        'questions': question
    }
    return render(request, 'compiler/category.html', context=context)


@login_required
def subcategory(request, scid):
    sc = get_object_or_404(SubCategory, id=scid)
    question = Question.objects.filter(sub_cat=sc)
    context = {
        'heading': "Subcategory",
        'questions': question,
    }
    return render(request, 'compiler/all_questions.html', context=context)

@login_required
def code_editor(request):
    return render(request, 'compiler/code_editor.html')


@login_required
def result(request, id):
    question = get_object_or_404(Question, id=id)
    tc = question.tc
    tc_sol = question.tc_sol
    global json_data
    if request.method == "POST":
        source = request.POST.get("script")
        lang = request.POST.get("lang")
        stdin = request.POST.get("stdin")
        u_id = request.user.id
        data = {'clientId': se.Client_id,
                'clientSecret': se.Client_secret,
                'script': source,
                'stdin': tc,
                'language': lang,
                'versionIndex': LANG_CODE[lang],
                }

        try:
            headers = {'Content-type': 'application/json'}
            r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)
            json_data = r.json()
            status = r.status_code
            output = json_data['output']
            print(output)
            print(tc_sol)
            if output == tc_sol:
                output = "1"
            else:
                output = "Failed at some test cases, check for corner cases"
        except Exception as e:
            output = settings.ERROR_MESSAGE
        return HttpResponse(json.dumps({'output': output}), content_type="application/json")
    else:
        return render(request, 'compiler/code_editor.html', locals())


@login_required
def resultt(request):
    global json_data
    if request.method == "POST":
        source = request.POST.get("script")
        lang = request.POST.get("lang")
        stdin = request.POST.get("stdin")
        u_id = request.user.id
        data = {'clientId': se.Client_id,
                'clientSecret': se.Client_secret,
                'script': source,
                'stdin': stdin,
                'language': lang,
                'versionIndex': LANG_CODE[lang],
                }

        try:
            headers = {'Content-type': 'application/json'}
            r = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)
            json_data = r.json()
            status = r.status_code
            output = json_data['output']
        except Exception as e:
            output = settings.ERROR_MESSAGE
        return HttpResponse(json.dumps({'output': json_data['output']}), content_type="application/json")
    else:
        return render(request, 'compiler/code_editor.html', locals())

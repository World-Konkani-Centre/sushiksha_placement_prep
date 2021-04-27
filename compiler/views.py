import json

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.shortcuts import render, HttpResponse
import sushiksha_placement_prep.settings as se

API_ENDPOINT = "https://api.jdoodle.com/v1/execute"

LANG_CODE = {'c': 1, 'java': 3, 'cpp14': 3, 'python3': 3, 'go': 3,
             'sql': 3, 'csharp': 3, 'dart': 3, 'nodejs': 3, 'kotlin': 2 }


@login_required
def code_editor(request):
    return render(request, 'compiler/code_editor.html')


@login_required
def result(request):
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


# def check_lang(self, lang):
#     lang_array = self.lang.split(",")
#     for lng in lang_array:
#         if lng == lang:
#             return False
#     return True

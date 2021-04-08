from django import forms

from interviews.models import Interview


class InterviewRegisterForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['heading', 'description','start_time','end_time','link']

from django import forms

from interviews.models import Interview, GD


class InterviewRegisterForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['branch', 'type', 'start_time', 'end_time', 'link']


class GDCreationForm(forms.ModelForm):
    class Meta:
        model = GD
        fields = ['heading',  'description', 'start_time', 'end_time', 'link']

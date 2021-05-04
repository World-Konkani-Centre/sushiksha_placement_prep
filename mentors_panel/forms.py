from django import forms
from interviews.models import OPTIONS


class MultiInterviewScheduleForm(forms.Form):
    heading = forms.CharField(max_length=50)
    start_date = forms.DateField()
    end_date = forms.DateField()
    st_start_time = forms.TimeField()
    st_end_time = forms.TimeField()
    description = forms.CharField(widget=forms.Textarea)
    link = forms.URLField(initial="https://tinyurl.com/pair-link")
    type = forms.ChoiceField(choices=OPTIONS)

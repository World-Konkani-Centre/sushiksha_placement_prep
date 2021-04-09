from django import forms

from interviews.models import Interview, GDParticipants


class InterviewRegisterForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['heading', 'description', 'start_time', 'end_time', 'link']


class GDParticipationForm(forms.ModelForm):
    class Meta:
        model = GDParticipants
        fields = ['branch']


class GDCreationForm(forms.Form):
    heading = forms.CharField(max_length=50)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    description = forms.Textarea()
    link = forms.URLField(empty_value='https://tinyurl.com/pair-link')
    attendees = forms.ModelMultipleChoiceField(queryset=GDParticipants.objects.all(), widget=forms.CheckboxSelectMultiple)
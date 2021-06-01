from django import forms
from interviews.models import OPTIONS, Branch


class MultiInterviewScheduleForm(forms.Form):
    heading = forms.CharField(max_length=50, help_text='Heading')
    start_date = forms.DateField(help_text='Starting date for repetitive interview')
    end_date = forms.DateField()
    st_start_time = forms.TimeField(label='Start Time', help_text='Please Note for all interview for above date, this will be its start time.')
    st_end_time = forms.TimeField(label='End Time', help_text='Interview Ending time')
    branch = forms.ModelChoiceField(queryset=Branch.objects.all())
    link = forms.URLField(initial="https://tinyurl.com/sushiksha-meet", label='Meeting link', help_text='If you are conducting the session using different meeting link other than Pair, you can update the link')
    type = forms.ChoiceField(choices=OPTIONS)



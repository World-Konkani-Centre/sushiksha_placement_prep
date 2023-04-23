from django import forms
from interviews.models import Branch

OPTIONS = (
    ('HR', 'HR'),
    ('Technical', 'Technical'),
)

class MultiInterviewScheduleForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), help_text='Branch Name will be heading of the Interview, If Interview is HR, then you can select NULL option for heading.', label='Interview Heading')
    start_date = forms.DateField(help_text="<strong class='text-info'>While Selecting Dates Please follow below timeline</strong> \
                                            <ol><li></li> <li></li></ol>")
    end_date = forms.DateField()
    st_start_time = forms.TimeField(label='Start Time', help_text='Please Note for all interview for above date, this will be its start time.')
    st_end_time = forms.TimeField(label='End Time', help_text='Interview Ending time')
    link = forms.URLField(label='Meeting link', help_text='Please provide your Zoom Link here.')
    type = forms.ChoiceField(choices=OPTIONS, label='Interview type', help_text="<strong class='text-info'></strong> \
                                                                                <ol><li></li> <li></li></ol>")



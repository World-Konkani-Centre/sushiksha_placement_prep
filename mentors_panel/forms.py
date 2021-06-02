from django import forms
from interviews.models import OPTIONS, Branch


class MultiInterviewScheduleForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), help_text='Branch Name will be heading of the Interview', label='Interview Heading')
    start_date = forms.DateField(help_text="<strong class='text-info'>While Selecting Dates Please follow below timeline</strong> \
                                            <ol><li>For Technical Interview from 21st June to 15th July</li><li>For GD from 21st June to 15th July</li><li>For HR from 16th July to 31st July</li></ol>")
    end_date = forms.DateField()
    st_start_time = forms.TimeField(label='Start Time', help_text='Please Note for all interview for above date, this will be its start time.')
    st_end_time = forms.TimeField(label='End Time', help_text='Interview Ending time')
    link = forms.URLField(label='Meeting link', help_text='Please provide your Zoom Link here.')
    type = forms.ChoiceField(choices=OPTIONS, label='Interview type', help_text="<strong class='text-info'>Please check again if your dates is following the timeline </strong> \
                                                                                <ol><li>For Technical Interview from 21st June to 15th July</li><li>For GD from 21st June to 15th July</li><li>For HR from 16th July to 31st July</li></ol>")



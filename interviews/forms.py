from django import forms
from django.utils.translation import gettext_lazy as _


from interviews.models import Interview, GD


class InterviewRegisterForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['branch', 'type', 'start_time', 'end_time', 'link']


class GDCreationForm(forms.ModelForm):
    class Meta:
        model = GD
        fields = ['start_time', 'link']
        help_texts = {
            'link': _(" "),
            'start_time': _("Enter the Date and Time"),
            # 'end_time': _('End Date and Time'),
        }
        labels = {
            'start_time': _('Start Date and Time'),
            # 'end_time': _('End Date and Time'),
            'link': _('Please provide your Zoom Link here.')
        }
        

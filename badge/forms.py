from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Reward
from users.models import Profile


class BadgeForm(forms.ModelForm):

    class Meta:
        model = Reward
        fields = ['user', 'descritpion', 'badge']
        help_texts = {
            'descritpion': _('Add a short description on why you are giving the badge'),
        }
        labels = {
            'descritpion': _('Message to user'),
            'badge': _('Badge to be Awarded'),
            'user':  _('Select the Users')
        }

    def __init__(self, *args, **kwargs):
        super(BadgeForm, self).__init__(*args, **kwargs)
        self.fields['user'] =  forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset=Profile.objects.filter(is_mentor=False))



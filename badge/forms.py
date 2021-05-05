from django import forms
# from django.utils.translation import gettext_lazy as _
from .models import Reward, Badge
from users.models import Profile
from django.contrib.admin import widgets
from django.db.models.functions import Lower



# class BadgeForm(forms.ModelForm):

#     class Meta:
#         model = Reward
#         fields = ['user', 'descritpion', 'badge']
#         help_texts = {
#             'descritpion': _('Add a short description on why you are giving the badge'),
#         }
#         labels = {
#             'descritpion': _('Message to user'),
#             'badge': _('Badge to be Awarded'),
#             'user':  _('Select the Users')
#         }

#     def __init__(self, *args, **kwargs):
#         super(BadgeForm, self).__init__(*args, **kwargs)
#         self.fields['user'] =  forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset=Profile.objects.filter(is_mentor=False))


class BadgeForm(forms.Form):
    badge = forms.ModelChoiceField(queryset=Badge.objects.all(), required=True, label='Badge to be awarded')
    description = forms.CharField(widget=forms.Textarea(), label='Message to user')
    profiles = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Profile.objects.filter(is_mentor=False).order_by(Lower('name')), required=True, label='Select the Profiles')

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(help_text='Please use the email that is given to World Konkani Center, maintain a one email for all konkanischolarship accouts.')

    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True

    class Meta:
        model = Profile
        fields = ['name', 'image']

        help_texts = {
            'image': _('For better Result, Upload a square image, or we will crop for you :)'),
        }
        labels = {
            'image': _('Profile picture'),
            'name': _('Full name')
        }

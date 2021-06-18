from django import forms
from tinymce import TinyMCE
from django.utils.translation import gettext as _



from resume_builder.models import Contact, Skill, Education, InternshipExperience, TrainingCertification, \
    Project, Extra, Language, Achievement, Resume, Comments


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['prefix', 'first_name', 'last_name', 'address_1', 'address_2', 'country', 'state', 'pin',
                  'phone_number', 'email', 'linked_in', 'linked_in_user', 'github', 'github_user']

        help_texts = {
            'github': _('Provide the gihtub profile link, If the account is not there leave it blank'),
            'prefix': _('The tagline <strong>coder, activist, eager to learn</strong> is just for example, please change it according to your need.')
        }

    def __init__(self, *args, **kwargs):
        super(ContactModelForm, self).__init__(*args, **kwargs)
        self.fields['linked_in'].required = False
        self.fields['github'].required = False
        self.fields['github_user'].label = False
        self.fields['github'].label = 'GitHub'
        self.fields['linked_in'].label = 'LinkedIn'
        self.fields['prefix'].label = 'Tagline'
        self.fields['linked_in_user'].label = 'LinkedIn username'
        self.fields['github_user'].label = 'GitHub username'


#
# class ObjectiveModelForm(forms.ModelForm):
#     class Meta:
#         model = Objective
#         fields = ['description']


class SkillModelForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill', 'proficiency']


class EducationModelForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'board', 'degree', 'field_of_study', 'country', 'state', 'city',  'joining_date',
                  'status', 'passing_date', 'grades_type', 'score']

    def __init__(self, *args, **kwargs):
        super(EducationModelForm, self).__init__(*args, **kwargs)
        self.fields['passing_date'].required = False
        self.fields['grades_type'].label = 'Grade Type'


class InternshipFormExperienceForm(forms.ModelForm):
    class Meta:
        model = InternshipExperience
        fields = ['name', 'position', 'country', 'state', 'city', 'date_of_joining', 'i_status', 'date_of_exit',
                  'description']

    def __init__(self, *args, **kwargs):
        super(InternshipFormExperienceForm, self).__init__(*args, **kwargs)
        self.fields['date_of_exit'].required = False
        self.fields['date_of_exit'].label = 'Date of Completion'
        self.fields['name'].label = 'Company name/ Industry name'
        self.fields['i_status'].label = 'Status'


class TrainingCertificationForm(forms.ModelForm):
    class Meta:
        model = TrainingCertification
        fields = ['name', 'provider', 't_status', 'date']

    def __init__(self, *args, **kwargs):
        super(TrainingCertificationForm, self).__init__(*args, **kwargs)
        self.fields['date'].required = False
        self.fields['t_status'].lable = 'Status'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'tech', 'start_date', 'p_status', 'end_date', 'description']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['end_date'].required = False
        self.fields['p_status'].label = 'Status'


class ExtraModelForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = ['name', 'description']


class LanguageModelForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language', 'proficiency']


class AchievementModelForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['description']


class ResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['status']


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CommentModelForm(forms.ModelForm):
    comment = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': True, 'rows': 15},
        )
    )
    class Meta:
        model = Comments
        fields = ['comment']

        

from django import forms

from resume_builder.models import Contact, About, Skill, Education, InternshipExperience, TrainingCertification, \
    Project, Extra, Language, PersonalInterest, Achievement, Declaration, Other, Objective


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['prefix', 'first_name', 'last_name', 'address_1', 'address_2', 'country', 'state', 'pin',
                  'phone_number', 'email', 'linked_in', 'github']

    def __init__(self, *args, **kwargs):
        super(ContactModelForm, self).__init__(*args, **kwargs)
        self.fields['linked_in'].required = False
        self.fields['github'].required = False


class AboutModelForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['summary']

class ObjectiveModelForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ['description']

class SkillModelForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill', 'proficiency']


class EducationModelForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'board', 'country', 'state', 'city', 'degree', 'field_of_study', 'joining_date',
                  'status', 'passing_date', 'score']

    def __init__(self, *args, **kwargs):
        super(EducationModelForm, self).__init__(*args, **kwargs)
        self.fields['passing_date'].required = False


class InternshipFormExperienceForm(forms.ModelForm):
    class Meta:
        model = InternshipExperience
        fields = ['name', 'position', 'country', 'state', 'city', 'date_of_joining', 'i_status', 'date_of_exit',
                  'description']

    def __init__(self, *args, **kwargs):
        super(InternshipFormExperienceForm, self).__init__(*args, **kwargs)
        self.fields['date_of_exit'].required = False


class TrainingCertificationForm(forms.ModelForm):
    class Meta:
        model = TrainingCertification
        fields = ['name', 'provider', 't_status', 'date']

    def __init__(self, *args, **kwargs):
        super(TrainingCertificationForm, self).__init__(*args, **kwargs)
        self.fields['date'].required = False


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'p_status', 'end_date', 'description']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['end_date'].required = False


class ExtraModelForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = ['description']


class LanguageModelForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language', 'proficiency']


class PIModelForm(forms.ModelForm):
    class Meta:
        model = PersonalInterest
        fields = ['description']


class AchievementModelForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['description']


class DeclarationModelForm(forms.ModelForm):
    class Meta:
        model = Declaration
        fields = ['declaration', 'state', 'city', 'date']


class OtherModelForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['heading', 'description']

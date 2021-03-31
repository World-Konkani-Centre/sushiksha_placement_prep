from django import forms

from django.forms import formset_factory


class EducationForm(forms.Form):
    ed_name = forms.CharField(label='College/School Name', widget=forms.TextInput(attrs={'placeholder': 'Enter '
                                                                                                        'college/school '
                                                                                                        'name here',
                                                                                         'required': 'true'}))
    ed_course = forms.CharField(label='Course', widget=forms.TextInput(
        attrs={'placeholder': 'Enter the course studied', 'required': 'true'}))
    ed_passing_year = forms.IntegerField(label='Passing Year',
                                         widget=forms.NumberInput(
                                             attrs={'placeholder': 'Enter the passing year', 'required': 'true'}))
    ed_percentage = forms.DecimalField(label='Percentage/CGPA', widget=forms.NumberInput(
        attrs={'placeholder': 'Enter the the percentage/cgpa scored', 'required': 'true'}))


class ProjectForm(forms.Form):
    p_name = forms.CharField(label='Project Name',
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Enter the project name', 'required': 'true'}))
    p_start_date = forms.CharField(label='project start date', required=True,
                                   widget=forms.TextInput(attrs={'required': 'true'}))
    p_end_date = forms.CharField(label='project end date', widget=forms.TextInput(attrs={'required': 'true'}))
    p_description = forms.CharField(label='Project description', widget=forms.Textarea(attrs={'placeholder': 'Project '
                                                                                                             'Description',
                                                                                              'rows': '10',
                                                                                              'cols': '10',
                                                                                              'required': 'true'}))


class SkillForm(forms.Form):
    sk_name = forms.CharField(label='Skill Name',
                              widget=forms.TextInput(attrs={'placeholder': 'Your Skill', 'required': 'true'}))
    sk_expertise = forms.IntegerField(label='Rate your skill 1-5',
                                      widget=forms.NumberInput(attrs={'placeholder': 'My rating', 'required': 'true'}))


class InternshipJobForm(forms.Form):
    ij_role = forms.CharField(label='Your role as an intern',
                              widget=forms.TextInput(attrs={'placeholder': 'Your Role', 'required': 'true'}))
    ij_company = forms.CharField(label='Where did you intern',
                                 widget=forms.TextInput(attrs={'placeholder': 'Internship '
                                                                              'Company', 'required': 'true'}))
    ij_description = forms.CharField(label='give some description',
                                     widget=forms.Textarea(
                                         attrs={'placeholder': 'Description', 'rows': '10', 'cols': '10',
                                                'required': 'true'}))


class AchievementForm(forms.Form):
    a_name = forms.CharField(label='Something you consider an achievement',
                             widget=forms.TextInput(attrs={'placeholder': 'Achievement', 'required': 'true'}))


class OtherForm(forms.Form):
    o_name = forms.CharField(label='Other particular info you wish to add?',
                             widget=forms.TextInput(attrs={'placeholder': 'Others', 'required': 'true'}))


SkillFormSet = formset_factory(SkillForm, extra=1)
EducationFormSet = formset_factory(EducationForm, extra=1)
InternshipJobFormSet = formset_factory(InternshipJobForm, extra=1)
ProjectFormSet = formset_factory(ProjectForm, extra=1)
AchievementFormSet = formset_factory(AchievementForm, extra=1)
OtherFormSet = formset_factory(OtherForm, extra=1)

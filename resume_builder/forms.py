from django import forms
from django.forms import formset_factory


class EducationForm(forms.Form):
    name = forms.CharField(label='College/School Name', widget=forms.TextInput(attrs={'placeholder': 'Enter '
                                                                                                     'college/school '
                                                                                                     'name here'}))
    course = forms.CharField(label='Course', widget=forms.TextInput(attrs={'placeholder': 'Enter the course studied'}))
    passing_year = forms.IntegerField(label='Passing Year',
                                      widget=forms.NumberInput(attrs={'placeholder': 'Enter the passing year'}))
    percentage = forms.DecimalField(label='Percentage/CGPA', widget=forms.NumberInput(
        attrs={'placeholder': 'Enter the the percentage/cgpa scored'}))


class ProjectForm(forms.Form):
    name = forms.CharField(label='Project Name',
                           widget=forms.TextInput(attrs={'placeholder': 'Enter the project name'}))
    start_date = forms.CharField(label='project start date')
    end_date = forms.CharField(label='project end date')
    description = forms.CharField(label='Project description', widget=forms.Textarea(attrs={'placeholder': 'Project '
                                                                                                           'Description',
                                                                                            'rows': '10',
                                                                                            'cols': '10'}))


class SkillForm(forms.Form):
    name = forms.CharField(label='Skill Name', widget=forms.TextInput(attrs={'placeholder': 'Your Skill'}))
    expertise = forms.IntegerField(label='Rate your skill 1-5',
                                   widget=forms.NumberInput(attrs={'placeholder': 'My rating'}))


class InternshipJobForm(forms.Form):
    role = forms.CharField(label='Your role as an intern', widget=forms.TextInput(attrs={'placeholder': 'Your Role'}))
    company = forms.CharField(label='Where did you intern', widget=forms.TextInput(attrs={'placeholder': 'Internship '
                                                                                                         'Company'}))
    description = forms.CharField(label='give some description',
                                  widget=forms.Textarea(
                                      attrs={'placeholder': 'Description', 'rows': '10', 'cols': '10'}))


class AchievementForm(forms.Form):
    name = forms.CharField(label='Something you consider an achievement',
                           widget=forms.TextInput(attrs={'placeholder': 'Achievement'}))


class OtherForm(forms.Form):
    name = forms.CharField(label='Other particular info you wish to add?',
                           widget=forms.TextInput(attrs={'placeholder': 'Others'}))


SkillFormSet = formset_factory(SkillForm, extra=1)
EducationFormSet = formset_factory(EducationForm, extra=1)
InternshipJobFormSet = formset_factory(InternshipJobForm, extra=1)
ProjectFormSet = formset_factory(ProjectForm, extra=1)
AchievementFormSet = formset_factory(AchievementForm, extra=1)
OtherFormSet = formset_factory(OtherForm, extra=1)

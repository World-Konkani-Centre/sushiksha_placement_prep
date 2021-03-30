from django import forms
from django.forms import formset_factory


class EducationForm(forms.Form):
    name = forms.CharField(
        label='College/School Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter college/school name here'
        })
    )
    course = forms.CharField(
        label='Course',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the course studied'
        })
    )
    percentage = forms.DecimalField(
        label='Percentage/CGPA',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the the percentage/cgpa scored'
        })
    )


EducationFormSet = formset_factory(EducationForm,extra=1)
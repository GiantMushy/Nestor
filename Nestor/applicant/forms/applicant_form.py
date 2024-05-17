from django.forms import ModelForm, widgets
from applicant.models import *


class ApplicantForm(ModelForm):
    '''Class containing the form to create a new applicant'''
    class Meta:
        model = Applicant
        exclude = ['id', 'user']
        widgets = {
                'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ExperienceForm(ModelForm):
    '''Class containing the form to create a new experience'''
    class Meta:
        model = Experience
        exclude = ['id']
        widgets = {
            'workplace_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'role': widgets.TextInput(attrs={'class': 'form-control'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'end_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'})
        }


class CVExperienceForm(ModelForm):
    '''Class containing the form to connects a user with an experience'''
    class Meta:
        model = CVExperience
        fields = ['applicant', 'experience']


class EducationForm(ModelForm):
    '''Class containing the form to create a new education'''
    class Meta:
        model = Education
        exclude = ['id']
        widgets = {
            'school_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'degree': widgets.TextInput(attrs={'class': 'form-control'}),
            'level': widgets.TextInput(attrs={'class': 'form-control'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'end_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'})
        }


class CVEducationForm(ModelForm):
    '''Class containing the form to connects a user with an education'''
    class Meta:
        model = CVEducation
        fields = ['applicant', 'education']


class ReferenceForm(ModelForm):
    '''Class containing the form to create a new reference'''
    class Meta:
        model = References
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'workplace_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'role': widgets.TextInput(attrs={'class': 'form-control'}),
            'is_contactable': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class CVReferenceForm(ModelForm):
    '''Class containing the form to connects a user with a reference'''
    class Meta:
        model = CVReferences
        fields = ['applicant', 'reference']

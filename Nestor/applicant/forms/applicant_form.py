from django.forms import ModelForm, widgets
from applicant.models import *


class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['id', 'user']
        widgets = {
                'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        } 


class ExperienceForm(ModelForm):
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
    class Meta:
        model = CVExperience
        fields = ['applicant', 'experience']


class EducationForm(ModelForm):
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
    class Meta:
        model = CVEducation
        fields = ['applicant', 'education']


class ReferenceForm(ModelForm):
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
    class Meta:
        model = CVReferences
        fields = ['applicant', 'reference']
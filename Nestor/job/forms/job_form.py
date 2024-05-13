from django import forms 
# import ModelForm, widgets
from job.models import Job, FavoriteJob
from django.utils import timezone
from company.models import Employee, Company
from common.models import Country, ZipCode, City


class JobCreateForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ['id', 'date_of_offering', 'num_of_applicants', 'company']
        widgets = {
            'application_due_date': forms.DateInput(attrs={'type':'date', 'format': 'dd-mm-yyyy'}), 
            'starting_date': forms.DateInput(attrs={'type':'date', 'format': 'dd-mm-yyyy'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter job name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write a description for the job', 'col' : '50'}),
            # 'zipcode': forms.ChoiceField(attrs={'empty_label' : 'Select a zipcode'}),
            'job_type': forms.Select(attrs={'placeholder': 'Select a job type'}),
            'job-category': forms.Select(attrs={'placeholder': 'Select a job category'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter the job address'}),
            'job_image': forms.TextInput(attrs={'placeholder': 'Enter a valid image link'}),
            'percentage': forms.NumberInput(attrs={'placeholder': 'Enter job percentage'}),
            # 'is_available': forms.CheckboxInput(attrs={'class': 'checkbox'})
        }


class FavoriteJobCreateForm(forms.ModelForm):
    class Meta:
        model = FavoriteJob
        fields = ['applicant', 'job']

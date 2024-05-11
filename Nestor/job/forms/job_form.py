from django import forms 
# import ModelForm, widgets
from job.models import Job
from django.utils import timezone


class JobCreateForm(forms.ModelForm):
    # date_of_offering = forms.DateField(initial=timezone.now().date())

    class Meta:
        model = Job
        exclude = ['id', 'date_of_offering', 'num_of_applicants']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.Select(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'job-category': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'job_image': forms.TextInput(attrs={'class': 'form-control'}),
            # 'date_of_offering': forms.DateInput(attrs={'class': 'form-control'}),
            'application_due_date': forms.DateInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'checkbox'})
        }

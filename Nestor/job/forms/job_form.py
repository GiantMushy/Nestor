from django.forms import ModelForm, widgets
from job.models import Job


class JobCreateForm(ModelForm):
    class Meta:
        model = Job
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipcode': widgets.Select(attrs={'class': 'form-control'}),
            'job_type': widgets.Select(attrs={'class': 'form-control'}),
            'job-category': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'job_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'date_of_offering': widgets.DateInput(attrs={'class': 'form-control'}),
            'application_due_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'percentage': widgets.NumberInput(attrs={'class': 'form-control'}),
            'is_available': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }
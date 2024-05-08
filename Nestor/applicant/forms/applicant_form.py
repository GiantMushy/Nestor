from django.forms import ModelForm, widgets
from applicant.models import Applicant

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['id', 'user']
        widgets = {
                'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        } 


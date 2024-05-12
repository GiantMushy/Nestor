from django import forms 
# import ModelForm, widgets
from job.models import Job
from django.utils import timezone
from company.models import Employee, Company
from common.models import Country, ZipCode, City


class JobCreateForm(forms.ModelForm):


    # company = forms.ModelChoiceField(queryset=Company.objects.none())
    # company = forms.IntegerField(widget = forms.HiddenInput(), initial=3)
    # company = forms.ModelChoiceField(queryset=Company.objects.none(), widget=forms.HiddenInput(attrs={'value': default_company_id}))

    # def __init__(self, *args, **kwargs):
    #     employee = kwargs.pop('employee', None)
    #     super(JobCreateForm, self).__init__(*args, **kwargs)
    #     self.employee = employee
    #     if self.employee:
    #         def_company = Company.objects.get(id=self.employee.company.id)
    #         print(def_company)
            # self.fields['company'].initial =  def_company
            # self.fields['company'].queryset = Company.objects.filter(id=self.employee.company.id)
            # print(self.fields['company'])
        

    class Meta:
        model = Job
        exclude = ['id', 'date_of_offering', 'num_of_applicants', 'company']
        widgets = {
            'application_due_date': forms.DateInput(attrs={'type':'date', 'format': 'dd-mm-yyyy'}), 
            'starting_date': forms.DateInput(attrs={'type':'date', 'format': 'dd-mm-yyyy'}),
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'description': forms.TextInput(attrs={'class': 'form-control'}),
            # 'zipcode': forms.Select(attrs={'class': 'form-control'}),
            # 'job_type': forms.Select(attrs={'class': 'form-control'}),
            # 'job-category': forms.Select(attrs={'class': 'form-control'}),
            # 'address': forms.TextInput(attrs={'class': 'form-control'}),
            # 'job_image': forms.TextInput(attrs={'class': 'form-control'}),
            # 'percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'is_available': forms.CheckboxInput(attrs={'class': 'checkbox'})
        }

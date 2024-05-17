from django.forms import ModelForm, widgets
from company.models import Company


class CompanyCreateForm(ModelForm):
    '''Class containing the form to create a new company'''
    class Meta:
        model = Company
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'zipcode': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'logo': widgets.TextInput(attrs={'class': 'form-control'}),
            'number_of_employees': widgets.NumberInput(attrs={'class': 'form-control'}),
            'link': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'})
        }
from django.shortcuts import render, get_object_or_404, redirect
from company.forms.company_form import CompanyCreateForm
from company.models import Company
from common.models import JobCategory, City


def index(request):
    context = {'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries': City.objects.all().order_by('name')
               }
    return render(request, 'company/index.html', context)


def get_company_by_id(request, id):
    return render(request, 'company/company_page.html', {
        'company': get_object_or_404(Company, pk=id)
    })


def create_company(request):
    if request.method == 'POST':
        form = CompanyCreateForm(data=request.POST)
        if form.is_valid():
            company = form.save()
            return redirect('company_index')
    else:
        form = CompanyCreateForm()
    return render(request, 'company/create_company.html', {
        'form': form
    })

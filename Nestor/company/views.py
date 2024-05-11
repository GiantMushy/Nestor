from django.shortcuts import render, get_object_or_404, redirect
from company.forms.company_form import CompanyCreateForm
from company.models import Company
from common.models import JobCategory, City
from django.http import JsonResponse


def index(request):

    active_section = get_active_section(request)

    if 'cpn' in request.GET:
        cpn = request.GET['cpn']
        companies = list(Company.objects.filter(name__icontains=cpn).values())
        return JsonResponse({'companies': companies})

    context = {'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries': City.objects.all().order_by('name'),
               'active_section': active_section
               }
    
    return render(request, 'company/index.html', context)


def get_company_by_id(request, id):
    active_section = get_active_section(request)
    return render(request, 'company/company_page.html', {
        'company': get_object_or_404(Company, pk=id),
        'active_section': active_section
    })


def create_company(request):
    active_section = get_active_section(request)
    if request.method == 'POST':
        form = CompanyCreateForm(data=request.POST)
        if form.is_valid():
            company = form.save()
            return redirect('company_index')
    else:
        form = CompanyCreateForm()
    return render(request, 'company/create_company.html', {
        'form': form,
        'active_section': active_section
    })


def get_active_section(request):
    active_section = None
    if request.path.startswith('/jobs/'):
        active_section = 'jobs'
    elif request.path.startswith('/companies/'):
        active_section = 'companies'

    return active_section
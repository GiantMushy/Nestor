from django.shortcuts import render, get_object_or_404, redirect
from company.forms.company_form import CompanyCreateForm
from company.models import Company, Employee
from common.models import JobCategory, City
from django.http import JsonResponse


def index(request):
    companies_qs = Company.objects.all().order_by('name')

    # Getting the query parameters
    com_param = request.GET.get('com')
    cou_params = list(request.GET.getlist('cou'))

    if com_param:
        companies_qs = companies_qs.filter(name__icontains=com_param)
    if cou_params:
        companies_qs = companies_qs.filter(zipcode__city_id__in=cou_params)
    employee = Employee.objects.filter(user=request.user).first()
    # Collecting all data into the context
    context = { "companies": list(companies_qs.values()),
                "active_section": get_active_section(request),
                "countries": City.objects.all().order_by('name'),
                "categories": JobCategory.objects.all().order_by('name'),
                "countries_checked": [int(param_id) for param_id in cou_params],
                "countries_placeholder": ', '.join([city.name for city in City.objects.filter(id__in=cou_params).order_by('name')]),
                "cpn_value": com_param or "",
                "employee": employee
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

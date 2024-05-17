from django.shortcuts import render, get_object_or_404, redirect
from company.forms.company_form import CompanyCreateForm
from company.models import Company, Employee
from common.models import JobCategory, City
from django.utils import timezone
from job.models import Job, FavoriteJob
from django.contrib.auth.decorators import login_required


def index(request):
    '''redirects the user to the list of companies
    context of the render contains all necessary data for
    the company cards on the page'''
    companies_qs = Company.objects.all().order_by('name')

    # Getting the query parameters
    com_param = request.GET.get('com')
    cou_params = list(request.GET.getlist('cou'))

    if com_param:
        companies_qs = companies_qs.filter(name__icontains=com_param)
    if cou_params:
        companies_qs = companies_qs.filter(zipcode__city_id__in=cou_params)
    # Collecting all data into the context
    context = { "companies": list(companies_qs.values()),
                "active_section": get_active_section(request),
                "countries": City.objects.all().order_by('name'),
                "categories": JobCategory.objects.all().order_by('name'),
                "countries_checked": [int(param_id) for param_id in cou_params],
                "countries_placeholder": ', '.join([city.name for city in City.objects.filter(id__in=cou_params).order_by('name')]),
                "cpn_value": com_param or "",
                }

    return render(request, 'company/index.html', context)


def get_company_by_id(request, id):
    '''returns the company object by its id
    renders the specific companies page'''
    active_section = get_active_section(request)
    all_jobs = Job.objects.filter(company_id=id).order_by('name')
    fav_jobs = FavoriteJob.objects.filter(user_id=request.user.id).all()

    jobs = [add_days_left(job) for job in all_jobs]
    filtered_jobs = [job for job in jobs if int(job.days_left) > 0]
    return render(request, 'company/company_page.html', {
        'company': get_object_or_404(Company, pk=id),
        'jobs': filtered_jobs,
        'fav_jobs': [job.job.id for job in fav_jobs],
        'active_section': active_section
    })

# TODO:  blabla
@login_required(redirect_field_name="/login")
def create_company(request):
    '''Creates a company and redirects to the list of companies page
    if all input was verified. Otherwise redirects back to the
    create_company page'''
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
    '''returns the active section of the current user'''
    active_section = None
    if request.path.startswith('/jobs/'):
        active_section = 'jobs'
    elif request.path.startswith('/companies/'):
        active_section = 'companies'

    return active_section


def add_days_left(job):
    '''adds the number of days left of a job offer to the
    job card'''
    days_left = job.application_due_date - timezone.now().date()
    job.days_left = str(days_left).split()[0]
    return job

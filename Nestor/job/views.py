from django.shortcuts import render, get_object_or_404, redirect
from job.forms.job_form import JobCreateForm
from job.models import Job
from django.utils import timezone
from common.models import JobCategory, City
from company.models import Company


def add_days_left(job):
    days_left = job.application_due_date - timezone.now().date()
    job.days_left = str(days_left).split()[0]
    return job


def index(request):
    all_jobs = Job.objects.all().order_by('name')

    # Getting the query parameters
    job_param = request.GET.get('job')
    com_params = list(request.GET.getlist('com'))
    cou_params = list(request.GET.getlist('cou'))
    cat_params = list(request.GET.getlist('cat'))

    if job_param:
        all_jobs = all_jobs.filter(name__icontains=job_param)
    if com_params:
        all_jobs = all_jobs.filter(company__id__in=com_params)
    if cou_params:
        all_jobs = all_jobs.filter(zipcode__city_id__in=cou_params)
    if cat_params:
        all_jobs = all_jobs.filter(job_category_id__in=cat_params)

    context = {'jobs': [add_days_left(job) for job in all_jobs],
               'active_section': get_active_section(request),
               'countries': City.objects.all().order_by('name'),
               'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries_checked': [int(param_id) for param_id in cou_params],
               'countries_placeholder':
                   ', '.join([city.name for city in City.objects.filter(id__in=cou_params).order_by('name')]),
               'categories_checked': [int(param_id) for param_id in cat_params],
               'categories_placeholder':
                   ', '.join([cat.name for cat in JobCategory.objects.filter(id__in=cat_params).order_by('name')]),
               'companies_checked': [int(param_id) for param_id in com_params],
               'companies_placeholder':
                   ', '.join([com.name for com in Company.objects.filter(id__in=com_params).order_by('name')]),
               'job_value': job_param or ""
               }

    return render(request, 'job/index.html', context)


def get_job_by_id(request, id):
    active_section = get_active_section(request)
    return render(request, 'job/job_page.html', {
        'job': get_object_or_404(Job, pk=id),
        'active_section': active_section
    })


def create_job(request):
    active_section = get_active_section(request)
    if request.method == 'POST':
        form = JobCreateForm(data=request.POST)
        if form.is_valid():
            job = form.save()
            return redirect('job_index')
    else:
        form = JobCreateForm()
    return render(request, 'job/create_job.html', {
        'form': form,
        'active_section': active_section
    })


def favorite_jobs(request):
    active_section = get_active_section(request)
    return render(request, 'job/favorite_jobs.html', context={'active_section': active_section})


def applied_jobs(request):
    active_section = get_active_section(request)
    return render(request, 'job/applied_jobs.html', context={'active_section': active_section})


def get_active_section(request):
    active_section = None
    if request.path.startswith('/jobs/'):
        active_section = 'jobs'
    elif request.path.startswith('/companies/'):
        active_section = 'companies'

    return active_section

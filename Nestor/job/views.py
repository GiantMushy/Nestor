from django.shortcuts import render, get_object_or_404, redirect
from job.forms.job_form import JobCreateForm
from job.models import Job, Application, FavoriteJob
from django.utils import timezone
from common.models import JobCategory, City
from company.models import Company, Employee


def add_days_left(job):
    days_left = job.application_due_date - timezone.now().date()
    job.days_left = str(days_left).split()[0]
    return job


def index(request):
    all_jobs = Job.objects.all().order_by('name')
    fav_jobs = FavoriteJob.objects.filter(applicant__user_id=request.user.id).all()

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
               'job_value': job_param or "",
               'fav_jobs': [job.job.id for job in fav_jobs],
               }

    return render(request, 'job/index.html', context)


def get_job_by_id(request, id):
    all_jobs = Job.objects.all().order_by('name')
    fav_jobs = FavoriteJob.objects.filter(applicant__user_id=request.user.id).all()

    return render(request, 'job/job_page.html', {
        'job': get_object_or_404(Job, pk=id),
        'fav_jobs': [job.job.id for job in fav_jobs],
        'active_section': get_active_section(request)
    })


def create_job(request):
    employee = Employee.objects.filter(user=request.user).first()
    active_section = get_active_section(request)
    if request.method == 'POST':
        form = JobCreateForm(data=request.POST, initial= {'company': employee.company})
        if form.is_valid():
            job = form.save(commit=False)
            job.company= employee.company
            job.save()
            return redirect('job_index')
    else:
        form = JobCreateForm()
    return render(request, 'job/create_job.html', {
        'form': JobCreateForm(data=request.POST),
        'employee': employee,
        'active_section': active_section
    })


def favorite_jobs(request):
    fav_jobs = FavoriteJob.objects.filter(applicant__user_id=request.user.id).all()
    job_ids = [app.job_id for app in fav_jobs]

    all_jobs = Job.objects.filter(id__in=job_ids)

    context = {'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries': City.objects.all().order_by('name'),
               'jobs': [add_days_left(job) for job in all_jobs],
               'active_section': get_active_section(request),
               'fav_jobs': [job.job.id for job in fav_jobs],
               }
    return render(request, 'job/favorite_jobs.html', context)


def applied_jobs(request):
    applications = Application.objects.filter(applicant__user_id=request.user.id).all()
    job_ids = [app.job_id for app in applications]

    all_jobs = Job.objects.filter(id__in=job_ids)

    context = {'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries': City.objects.all().order_by('name'),
               'jobs': [add_days_left(job) for job in all_jobs],
               'active_section': get_active_section(request)
               }
    return render(request, 'job/applied_jobs.html', context)



def get_active_section(request):
    active_section = None
    if request.path.startswith('/jobs/'):
        active_section = 'jobs'
    elif request.path.startswith('/companies/'):
        active_section = 'companies'

    return active_section

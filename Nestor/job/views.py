from django.shortcuts import render, get_object_or_404, redirect
from job.forms.job_form import JobCreateForm
from job.models import Job
from django.utils import timezone
from common.models import JobCategory, City
from company.models import Company, Employee


def add_days_left(job):
    days_left = job.application_due_date - timezone.now().date()
    job.days_left = str(days_left).split()[0]
    return job

def index(request):
    active_section = get_active_section(request)
    all_jobs = Job.objects.all().order_by('name')
    jobs_with_days_left = [add_days_left(job) for job in all_jobs]

    context = {'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries': City.objects.all().order_by('name'),
               'jobs': jobs_with_days_left,
               'active_section': active_section
               }
    return render(request, 'job/index.html', context)

def get_job_by_id(request, id):
    active_section = get_active_section(request)
    return render(request, 'job/job_page.html', {
        'job': get_object_or_404(Job, pk=id),
        'active_section': active_section
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

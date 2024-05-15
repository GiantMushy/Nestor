from django.shortcuts import render, get_object_or_404, redirect
from job.forms.job_form import JobCreateForm
from applicant.models import Applicant
from job.models import Job, Application, FavoriteJob, hasEducation, hasExperience, hasReferences, hasSkills
from django.utils import timezone
from common.models import JobCategory, City
from company.models import Company, Employee
from applicant.models import Education, CVEducation, CVExperience
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


def add_days_left(job):
    days_left = job.application_due_date - timezone.now().date()
    job.days_left = str(days_left).split()[0]
    return job


def index(request):
    all_jobs = Job.objects.all().order_by('name')
    fav_jobs = FavoriteJob.objects.filter(user_id=request.user.id).all()
    employee = Employee.objects.filter(user=request.user.id).first()

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

    jobs = [add_days_left(job) for job in all_jobs]
    filtered_jobs = [job for job in jobs if int(job.days_left) > 0]

    context = {'jobs': filtered_jobs,
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
               'employee': employee
               }

    return render(request, 'job/index.html', context)


def get_application_status(application):
    if application.job.application_due_date < timezone.now().date():
        if not application.job.is_available:
            application.status = 'Finished'
        else:
            application.status = 'In review'
    else:
        application.status = 'In progress'


def get_job_by_id(request, id):
    fav_jobs = FavoriteJob.objects.filter(user_id=request.user.id).all()
    application = Application.objects.filter(applicant__user_id=request.user.id, job_id=id).first()
    if application:
        get_application_status(application)

    return render(request, 'job/job_page.html', {
        'job': get_object_or_404(Job, pk=id),
        'fav_jobs': [job.job.id for job in fav_jobs],
        'application': application,
        'active_section': get_active_section(request)
    })



@login_required(redirect_field_name="/login")
@permission_required('job.add_job', raise_exception=True)
def create_job(request):
    employee = Employee.objects.filter(user=request.user).first()
    active_section = get_active_section(request)
    if request.method == 'POST':
        form = JobCreateForm(data=request.POST, initial= {'company': employee.company})
        if form.is_valid():
            job = form.save(commit=False)
            job.company = employee.company
            job.save()
            return redirect('job_index')
    else:
        form = JobCreateForm()
    return render(request, 'job/create_job.html', {
        'form': JobCreateForm(data=request.POST),
        'employee': employee,
        'active_section': active_section
    })

#TODO: 

@login_required(redirect_field_name="/login")
def favorite_jobs(request):
    fav_jobs = FavoriteJob.objects.filter(user_id=request.user.id).all()
    job_ids = [app.job_id for app in fav_jobs]
    all_jobs = Job.objects.filter(id__in=job_ids)

    context = {'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries': City.objects.all().order_by('name'),
               'jobs': [add_days_left(job) for job in all_jobs],
               'active_section': get_active_section(request),
               'fav_jobs': [job.job.id for job in fav_jobs]}

    return render(request, 'job/favorite_jobs.html', context)

# TODO: 

@login_required(redirect_field_name="/login")
def applied_jobs(request):
    applications = Application.objects.filter(applicant__user_id=request.user.id, is_submitted=True).all()

    for application in applications:
        get_application_status(application)

    context = {'companies': Company.objects.all().order_by('name'),
               'categories': JobCategory.objects.all().order_by('name'),
               'countries': City.objects.all().order_by('name'),
               'applications': applications,
               'active_section': get_active_section(request)}

    return render(request, 'job/applied_jobs.html', context)

# TODO: 

@login_required(redirect_field_name="/login")
def favorite_job(request):
    # To get the job that was selected in the url before and the applicant
    job_id = request.POST.get('job_id')

    fav_jobs = FavoriteJob.objects.filter(user_id=request.user.id).all()
    fav_job = fav_jobs.filter(job__id=job_id).all()
    job = get_object_or_404(Job, id=job_id)
    # applicant = get_object_or_404(Applicant, user_id=request.user.id)

    if not fav_job:
        new_favorite = FavoriteJob(user=request.user, job=job)
        new_favorite.save()
    else:
        fav_job.delete()

    return redirect(f'/jobs/{job_id}')

# TODO: 

@login_required(redirect_field_name="/login")
@permission_required('job.view_job', raise_exception=True)
def your_job_offers(request):
    employee = get_object_or_404(Employee, user=request.user)
    company_id = employee.company.id
    company_jobs = Job.objects.filter(company_id=company_id)
    get_total_applicants(company_jobs)

    context = {'jobs': [add_days_left(job) for job in company_jobs],
               'active_section': get_active_section(request),
               'employee': employee}

    return render(request, 'job/your_job_offers.html', context)

# TODO: 
@login_required(redirect_field_name="/login")
@permission_required('job.view_job', raise_exception=True)
def get_applications_by_job_id(request, id):
    employee = get_object_or_404(Employee, user=request.user)
    job = get_object_or_404(Job, pk=id)
    applications = Application.objects.filter(job_id=id).all()
    job.num_of_applicants = len(applications)

    for application in applications:
        education = hasEducation.objects.filter(application=application.id)
        experience = hasExperience.objects.filter(application=application.id)
        skills = hasSkills.objects.filter(application=application.id)
        references = hasReferences.objects.filter(application=application.id)
        if education.exists():
            for ed in education:
                application.education = ed.education

        if experience.exists():
            for ex in experience:
                application.experience = ex.experience

    return render(request, 'job/applications_page.html', {
        'job': job,
        'applications':applications,
        'active_section': get_active_section(request),
        'employee': employee
    })

# TODO: 
@permission_required('job.view_job', raise_exception=True)
def review_application(request, jid, aid):
    
    application = Application.objects.get(id=aid)

    education = hasEducation.objects.filter(application=application.id)
    experience = hasExperience.objects.filter(application=application.id)
    skills = hasSkills.objects.filter(application=application.id)
    references = hasReferences.objects.filter(application=application.id)
    if education.exists():
        application.education = []
        for ed in education:
            application.education.append(ed.education)

    if experience.exists():
        application.experience = []
        for ex in experience:
            application.experience.append(ex.experience)

    if skills.exists():
        application.skills = []
        for skill in skills:
            application.skills.append(skill.skill)
    
    if references.exists():
        application.references = []
        for ref in references:
            application.references.append(ref.reference)

    return render(request, 'job/review_application.html', {
        'job': Job.objects.get(id=jid),
        'application': application,
        'active_section': get_active_section(request)
    })



def get_active_section(request):
    active_section = None
    if request.path.startswith('/jobs/'):
        active_section = 'jobs'
    elif request.path.startswith('/companies/'):
        active_section = 'companies'

    return active_section


def get_total_applicants(company_jobs):
    for job in company_jobs:
        total_applicants = Application.objects.filter(job_id=job.id).count()
        job.total_applicants = total_applicants

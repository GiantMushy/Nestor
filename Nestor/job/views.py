from django.shortcuts import render, get_object_or_404
from job.forms.job_form import JobCreateForm
from job.models import Job


# Create your views here.

jobs = [
    { 'title': 'Software Engineer', 'company': 'Marel', 'percentage': '100', 'days': '12'},
    { 'title': 'Bank Engineer', 'company': 'Arion', 'percentage': '90', 'days': '123'},
    { 'title': 'Cunt Engineer', 'company': 'Islandsbanki', 'percentage': '25', 'days': '1'}
]


def index(request):
    return render(request, 'job/index.html', context={'jobs': jobs})


def get_job_by_id(request, id):
    return render(request, 'job/job_page.html', {
        'job': get_object_or_404(Job, pk=id)
    })


def create_job(request):
    if request.method == 'POST':
        print(1)
    else:
        form = JobCreateForm()
    return render(request, 'job/create_job.html', {
        'form': form
    })
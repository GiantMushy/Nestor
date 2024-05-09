from django.shortcuts import render, get_object_or_404, redirect
from job.forms.job_form import JobCreateForm
from job.models import Job


def index(request):
    context = {'jobs': Job.objects.all().order_by('name')}
    return render(request, 'job/index.html', context)


def get_job_by_id(request, id):
    return render(request, 'job/job_page.html', {
        'job': get_object_or_404(Job, pk=id)
    })


def create_job(request):
    if request.method == 'POST':
        form = JobCreateForm(data=request.POST)
        if form.is_valid():
            job = form.save()
            return redirect('job_index')
    else:
        form = JobCreateForm()
    return render(request, 'job/create_job.html', {
        'form': form
    })

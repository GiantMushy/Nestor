from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from applicant.models import Applicant, CVEducation, CVExperience, CVReferences
from applicant.forms.applicant_form import ApplicantForm
from common.models import ZipCode


def applicant(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ApplicantForm(instance=applicant, data=request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.user = request.user
            applicant.save()
            return redirect('applicant')
    experience = CVExperience.objects.filter(applicant=applicant).all()
    education = CVEducation.objects.filter(applicant=applicant).all()
    references = CVReferences.objects.filter(applicant=applicant).all()
    return render(request, 'applicant/applicant.html', {
        'form': ApplicantForm(instance=applicant),
        'applicant': applicant,
        'zip_options': ZipCode.objects.all(),
        'experiences': experience,
        'educations': education,
        'references': references
    })


def index(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    return render(request,'applicant/index.html', {'applicant': applicant})
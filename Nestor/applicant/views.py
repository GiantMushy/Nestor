from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from applicant.models import Applicant, CVEducation, CVExperience, CVReferences
from applicant.forms.applicant_form import *
from common.models import ZipCode


def applicant(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    experiences = CVExperience.objects.filter(applicant=applicant).all()
    educations = CVEducation.objects.filter(applicant=applicant).all()
    references = CVReferences.objects.filter(applicant=applicant).all()

    if request.method == 'POST':
        applicant_form = ApplicantForm(instance=applicant, data=request.POST)
        validity = True

        if applicant_form.is_valid():
            applicant = applicant_form.save(commit=False)
            applicant.user = request.user
        else:
            validity = False

        for experience in experiences:
            experience_form = ExperienceForm(instance=experience, data=request.POST)
            if experience_form.is_valid():
                experience = experience_form.save(commit=False)
                experience.user = request.user
            else:
                validity = False

        for education in educations:
            education_form = EducationForm(instance=education, data=request.POST)
            if education_form.is_valid():
                education = education_form.save(commit=False)
                education.user = request.user
            else:
                validity = False

        for reference in references:
            reference_form = ReferenceForm(instance=reference, data=request.POST)
            if reference_form.is_valid():
                reference = reference_form.save(commit=False)
                reference.user = request.user
            else:
                validity = False

        if validity:
            applicant.save()
            for experience in experiences:
                experience.save()
            for education in educations:
                education.save()
            for reference in references:
                reference.save()
            return redirect('applicant')

        experience_forms = {}
        for experience in experiences:
            experience_forms[experience]: ExperienceForm(instance=experience)
        education_forms = {}
        for education in educations:
            education_forms[education]: EducationForm(instance=education)
        reference_forms = {}
        for reference in references:
            reference_forms[reference]: ReferenceForm(instance=reference)

        context = {
            'applicant_form': ApplicantForm(instance=applicant),
            'experience_forms': experience_forms,
            'education_forms': education_forms,
            'reference_forms': reference_forms,
            'applicant': applicant,
            'zip_options': ZipCode.objects.all(),
            'experiences': experiences,
            'educations': educations,
            'references': references
        }

    return render(request, 'applicant/applicant.html', context)


def index(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    return render(request,'applicant/index.html', {'applicant': applicant})

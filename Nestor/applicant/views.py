from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from applicant.models import Applicant, CVEducation, CVExperience, CVReferences
from applicant.forms.applicant_form import *
from common.models import ZipCode


def applicant(request):
    print("Hello what")
    applicant = Applicant.objects.filter(user=request.user).first()
    experiences = CVExperience.objects.filter(applicant=applicant).all()
    educations = CVEducation.objects.filter(applicant=applicant).all()
    references = CVReferences.objects.filter(applicant=applicant).all()


    if request.method == 'POST':
        print(request)
        applicant_form = ApplicantForm(instance=applicant, data=request.POST)
        validity = True

        if applicant_form.is_valid():
            applicant = applicant_form.save(commit=False)
            applicant.user = request.user
            applicant.save()
            print("Contact Info Validity Confirmed")
        else:
            validity = False

#        for experience in experiences:
#            experience_form = ExperienceForm(instance=experience, data=request.POST)
#            if experience_form.is_valid():
#                experience = experience_form.save(commit=False)
#                experience.user = request.user
#                experience.save()
#                print("Experience Validity Confirmed")
#            else:
#                print("Experience Validity Failed")
#                validity = False

#        for education in educations:
#            education_form = EducationForm(instance=education, data=request.POST)
#            if education_form.is_valid():
#                print("Education Validity Confirmed")
#                education = education_form.save(commit=False)
#                education.user = request.user
#            else:
#                validity = False

        for reference in references:
            reference_form = ReferenceForm(instance=reference, data=request.POST)
            print(reference_form)
            print(reference)
            if reference_form.is_valid():
                print("Reference Validity Confirmed")
                reference = reference_form.save(commit=False)
                reference.user = request.user
            else:
                print("Reference Validity Failed")
                validity = False

        if validity:
            print("Validity Confirmed")
#            for experience in experiences:
#                experience.save()
#            for education in educations:
#                education.save()
#            for reference in references:
#                reference.save()
            return redirect('applicant')
        else:
            print("Validity Failed")
            return redirect('applicant')

    context = {
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
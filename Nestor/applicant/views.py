from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from applicant.models import *
from applicant.forms.applicant_form import *
from common.models import ZipCode


def applicant(request):
    print("Hello what")
    applicant = Applicant.objects.filter(user=request.user).first()
    experiences = CVExperience.objects.filter(applicant=applicant).all()
    educations = CVEducation.objects.filter(applicant=applicant).all()
    references = CVReferences.objects.filter(applicant=applicant).all()

    if request.method == 'POST':
        print("request:")
        print(request)
        print("request.POST:")
        print(request.POST)
        validity = True

        if "zipcode" in request.POST:  #Applicant
            applicant_form = ApplicantForm(instance=applicant, data=request.POST)
            if applicant_form.is_valid():
                applicant = applicant_form.save(commit=False)
                applicant.user = request.user
                applicant.save()
                print("Contact Info Validity Confirmed")
            else:
                validity = False

        if "workplace_name" in request.POST and "start_date" in request.POST:  #Experience
            experience_form = ExperienceForm(data=request.POST)
            print(experience_form.errors)
            if experience_form.is_valid():
                print("Experience Validity SUCCESS")
                experience = experience_form.save(commit=False)
                applicant = Applicant.objects.filter(user=request.user).first()
                experience.save()
                cvexp = CVExperience(applicant=applicant, experience=experience)
                cvexp.save()

            else:
                print("Experience Validity Failed: ")
                print(experience_form.errors)
                validity = False

        if "school_name" in request.POST:  #Education
            education_form = EducationForm(data=request.POST)
            print(education_form.errors)
            if education_form.is_valid():
                print("Education Validity SUCCESS")
                education = education_form.save(commit=False)
                applicant = Applicant.objects.filter(user=request.user).first()
                education.save()
                cvedu = CVEducation(applicant=applicant, education=education)
                cvedu.save()

            else:
                print("Education Validity Failed: ")
                print(education_form.errors)
                validity = False

        if "is_contactable" in request.POST:  #References
            reference_form = ReferenceForm(data=request.POST)
            print(reference_form.errors)
            if reference_form.is_valid():
                print("Reference Validity SUCCESS")
                reference = reference_form.save(commit=False)
                applicant = Applicant.objects.filter(user=request.user).first()
                reference.save()
                cvref = CVReferences(applicant=applicant, reference=reference)
                cvref.save()

            else:
                print("Reference Validity Failed: ")
                print(reference_form.errors)
                validity = False

        if validity:
            print("Validity Confirmed")
            return redirect('applicant')
        else:
            print("Validity Failed")
            return redirect('applicant')

    context = {
        'applicant': applicant,
        'zip_options': ZipCode.objects.all(),
        'education_levels': EducationLevel.objects.all(),
        'experiences': experiences,
        'educations': educations,
        'references': references
    }
    return render(request, 'applicant/applicant.html', context)


def index(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    return render(request, 'applicant/index.html', {'applicant': applicant})

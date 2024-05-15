from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from applicant.models import *
from applicant.forms.applicant_form import *
from common.models import ZipCode, Skills, SkillGenre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from job.models import Job, Application, hasSkills, hasEducation, hasExperience, hasReferences


################################  CONTACT INFORMATION #####################################
def contact_info(request):
    print("Hello Contact Info")
    applicant = Applicant.objects.filter(user=request.user).first()


    applicant_form = ApplicantForm(instance=applicant, data=request.POST)
    if applicant_form.is_valid():
        applicant = applicant_form.save(commit=False)
        applicant.user = request.user

        applicant.save()
        print("PATCH Contact Info Validity SUCCESS")
        return redirect('applicant')
    else:
        print("PATCH Contact Info Validity Failed")
        return redirect('applicant')


################################  EXPERIENCES #####################################
def experience_add(request):
    print("Adding Experience")
    applicant = Applicant.objects.filter(user=request.user).first()

    experience_form = ExperienceForm(data=request.POST)
    if experience_form.is_valid():
        print("POST Experience Validity SUCCESS")
        experience = experience_form.save(commit=False)
        applicant = Applicant.objects.filter(user=request.user).first()
        experience.save()
        cvexp = CVExperience(applicant=applicant, experience=experience)
        cvexp.save()
        return redirect('applicant')
    else:
        print("POST Experience Validity Failed: ")
        return redirect('applicant')


def experience_edit(request):
    print("Editing Experience")
    applicant = Applicant.objects.filter(user=request.user).first()
    experience_id = request.POST.get('experience_id')
    experience = get_object_or_404(Experience, id=experience_id)
    experience_form = ExperienceForm(data=request.POST, instance=experience)

    if experience_form.is_valid():
        print("POST Experience Validity SUCCESS")
        experience_form.save()
        return redirect('applicant')
    else:
        print("POST Experience Validity Failed")
        return redirect('applicant')


def experience_del(request):
    return redirect('applicant')


################################  EDUCATIONS #####################################
def education_add(request):
    print("Adding Education")
    applicant = Applicant.objects.filter(user=request.user).first()

    education_form = EducationForm(data=request.POST)
    if education_form.is_valid():
        print("POST Education Validity SUCCESS")
        education = education_form.save(commit=False)
        applicant = Applicant.objects.filter(user=request.user).first()
        education.save()
        cvedu = CVEducation(applicant=applicant, education=education)
        cvedu.save()
        return redirect('applicant')
    else:
        print("POST Education Validity Failed: ")
        return redirect('applicant')


def education_edit(request):
    print("Editing Education")
    applicant = Applicant.objects.filter(user=request.user).first()
    education_id = request.POST.get('education_id')
    education = get_object_or_404(Education, id=education_id)
    education_form = EducationForm(data=request.POST, instance=education)

    if education_form.is_valid():
        print("POST Education Validity SUCCESS")
        education_form.save()
        return redirect('applicant')
    else:
        print("POST Education Validity Failed")
        return redirect('applicant')


def education_del(request):
    return redirect('applicant')


################################  REFERENCES #####################################
def reference_add(request):
    print("Adding Reference")
    applicant = Applicant.objects.filter(user=request.user).first()

    reference_form = ReferenceForm(data=request.POST)
    if reference_form.is_valid():
        print("POST Reference Validity SUCCESS")
        reference = reference_form.save(commit=False)
        applicant = Applicant.objects.filter(user=request.user).first()
        reference.save()
        cvref = CVReferences(applicant=applicant, reference=reference)
        cvref.save()
        return redirect('applicant')
    else:
        print("POST Reference Validity Failed: ")
        return redirect('applicant')


def reference_edit(request):
    print("Editing Reference")
    applicant = Applicant.objects.filter(user=request.user).first()
    reference_id = request.POST.get('reference_id')
    reference = get_object_or_404(References, id=reference_id)
    reference_form = ReferenceForm(data=request.POST, instance=reference)

    if reference_form.is_valid():
        print("POST Reference Validity SUCCESS")
        reference_form.save()
        return redirect('applicant')
    else:
        print("POST Reference Validity Failed")
        return redirect('applicant')


def reference_del(request):
    return redirect('applicant')


################################  SKILLS  #####################################
def add_skill(request): #adds a skill
    applicant = Applicant.objects.filter(user=request.user).first()
    app_skills = CVSkills.objects.filter(applicant=applicant).all()
    token, data = request.POST.items()
    genre, skill = data
    print(app_skills)
    validity = True
    for app_skill in app_skills:
        if skill in app_skill.skill.name:
            validity = False
    if validity:
        skill_object = Skills.objects.filter(name=skill).first()
        cvskill = CVSkills(applicant=applicant, skill=skill_object)
        cvskill.save()
        print("Skill Added SUCCESS")
    else:
        print("Skill already in Applicant")

    return redirect('applicant')


def remove_skill(request): #removes a skill
    return redirect('applicant')


################################  OTHER  #####################################
@login_required(redirect_field_name="/login")
def applicant(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    experiences = CVExperience.objects.filter(applicant=applicant).all()
    educations = CVEducation.objects.filter(applicant=applicant).all()
    references = CVReferences.objects.filter(applicant=applicant).all()
    app_skills = CVSkills.objects.filter(applicant=applicant).all()
    genres = SkillGenre.objects.all()
    skills = Skills.objects.all()

    all_skills = {}
    applicant_skills = {}
    for genre in genres:
        all_skills[genre] = []
        applicant_skills[genre] = []
    for skill in skills:
        all_skills[skill.genre].append(skill)
    for skill in app_skills:
        applicant_skills[skill.skill.genre].append(skill.skill)
   

    context = {
        'applicant': applicant,
        'zip_options': ZipCode.objects.all(),
        'education_levels': EducationLevel.objects.all(),
        'experiences': experiences,
        'educations': educations,
        'references': references,
        'applicant_skills': applicant_skills,
        'all_skills': all_skills
    }
    return render(request, 'applicant/applicant.html', context)


@login_required(redirect_field_name="/login")
def index(request):
    applicant = Applicant.objects.filter(user=request.user).first()
    return render(request, 'applicant/index.html', {'applicant': applicant})


def apply_init(request, id):
    print("Displaying Application Data")
    applicant = Applicant.objects.filter(user=request.user).first()
    job = get_object_or_404(Job, pk=id)

    application = Application.objects.filter(job=job, applicant=applicant)
    if not application.exists():
        application = Application(applicant=applicant, job=job)
        application.save()
        profile_experiences = CVExperience.objects.filter(applicant=applicant).all()
        profile_educations = CVEducation.objects.filter(applicant=applicant).all()
        profile_references = CVReferences.objects.filter(applicant=applicant).all()
        profile_app_skills = CVSkills.objects.filter(applicant=applicant).all()

        for experience in profile_experiences:
            exp = hasExperience(application=application, experience=experience.experience)
            exp.save()
        for education in profile_educations:
            edu = hasEducation(application=application, education=education.education)
            edu.save()
        for reference in profile_references:
            ref = hasReferences(application=application, reference=reference.reference)
            ref.save()
        for skill in profile_app_skills:
            skl = hasSkills(application=application, skill=skill.skill)
            skl.save()
        print("New Application Created Successfully and Data Transferred")
    else:
        application = application.first()
        print("Application Already Exists")

    experiences = hasExperience.objects.filter(application=application).all()
    educations = hasEducation.objects.filter(application=application).all()
    references = hasReferences.objects.filter(application=application).all()
    app_skills = hasSkills.objects.filter(application=application).all()

    genres = SkillGenre.objects.all()
    skills = Skills.objects.all()
    all_skills = {}
    applicant_skills = {}
    for genre in genres:
        all_skills[genre] = []
        applicant_skills[genre] = []
    for skill in skills:
        all_skills[skill.genre].append(skill)
    for skill in app_skills:
        applicant_skills[skill.skill.genre].append(skill.skill)

    context = {
        'job': job,
        'applicant': applicant,
        'zip_options': ZipCode.objects.all(),
        'education_levels': EducationLevel.objects.all(),
        'experiences': experiences,
        'educations': educations,
        'references': references,
        'applicant_skills': applicant_skills,
        'all_skills': all_skills
    }
    return render(request, 'applicant/application/__init__.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from applicant.models import *
from applicant.forms.applicant_form import *
from common.models import ZipCode, Skills, SkillGenre, City, Country
from django.contrib.auth.decorators import login_required
from job.models import Job, Application, hasSkills, hasEducation, hasExperience, hasReferences
from company.models import Employee


################################  CONTACT INFORMATION #####################################
def contact_info(request):
    '''Validates and updates applicant contact_info requests
    Redirects to profile'''
    applicant = Applicant.objects.filter(user=request.user).first()

    applicant_form = ApplicantForm(instance=applicant, data=request.POST)
    if applicant_form.is_valid():
        applicant = applicant_form.save(commit=False)
        applicant.user = request.user

        applicant.save()
        return redirect('applicant')
    else:
        return redirect('applicant')


def application_contact_info(request, id):
    '''Validates and updates applicant contact_info requests from the application page
    Redirects back to application page instead of profile'''
    applicant = Applicant.objects.filter(user=request.user).first()

    applicant_form = ApplicantForm(instance=applicant, data=request.POST)
    if applicant_form.is_valid():
        applicant = applicant_form.save(commit=False)
        applicant.user = request.user

        applicant.save()
        return redirect('/applicants/application/' + str(id) + '/cover-letter')
    else:
        return redirect('/applicants/application/' + str(id) + '/cover-letter')


################################  EXPERIENCES #####################################
def experience_add(request):
    '''Validates and adds an experience instance for the applicants profile
    Redirects to profile'''
    applicant = Applicant.objects.filter(user=request.user).first()

    experience_form = ExperienceForm(data=request.POST)
    if experience_form.is_valid():
        experience = experience_form.save(commit=False)
        applicant = Applicant.objects.filter(user=request.user).first()
        experience.save()
        cvexp = CVExperience(applicant=applicant, experience=experience)
        cvexp.save()
        return redirect('applicant')
    else:
        return redirect('applicant')


def experience_edit(request):
    '''Validates and updates an experience instance for the applicants profile
    Redirects to profile'''
    applicant = Applicant.objects.filter(user=request.user).first()
    experience_id = request.POST.get('experience_id')
    experience = get_object_or_404(Experience, id=experience_id)
    experience_form = ExperienceForm(data=request.POST, instance=experience)

    if experience_form.is_valid():
        experience_form.save()
        return redirect('applicant')
    else:
        return redirect('applicant')


def remove_experience(request):
    '''Removes an experience instance from the applicants profile
    Redirects to profile'''
    experience_id = request.POST.get('experience_id')
    exp = get_object_or_404(Experience, id=experience_id)
    exp.delete()
    return redirect('applicant')


################################  EDUCATIONS #####################################
def education_add(request):
    '''adds an instance of education in the users profile'''
    applicant = Applicant.objects.filter(user=request.user).first()

    education_form = EducationForm(data=request.POST)
    if education_form.is_valid():
        education = education_form.save(commit=False)
        applicant = Applicant.objects.filter(user=request.user).first()
        education.save()
        cvedu = CVEducation(applicant=applicant, education=education)
        cvedu.save()
        return redirect('applicant')
    else:
        return redirect('applicant')


def education_edit(request):
    '''edits an instance of education in the users profile'''
    applicant = Applicant.objects.filter(user=request.user).first()
    education_id = request.POST.get('education_id')
    education = get_object_or_404(Education, id=education_id)
    education_form = EducationForm(data=request.POST, instance=education)

    if education_form.is_valid():
        education_form.save()
        return redirect('applicant')
    else:
        return redirect('applicant')


def remove_education(request):
    '''Removes an education instance from the applicants profile
    Redirects to profile'''
    education_id = request.POST.get('education_id')
    edu = get_object_or_404(Education, id=education_id)
    edu.delete()
    return redirect('applicant')


################################  REFERENCES #####################################
def reference_add(request):
    '''adds an instance of reference to the users profile'''
    applicant = Applicant.objects.filter(user=request.user).first()

    reference_form = ReferenceForm(data=request.POST)
    if reference_form.is_valid():
        reference = reference_form.save(commit=False)
        applicant = Applicant.objects.filter(user=request.user).first()
        reference.save()
        cvref = CVReferences(applicant=applicant, reference=reference)
        cvref.save()
        return redirect('applicant')
    else:
        return redirect('applicant')


def reference_edit(request):
    '''updates a reference data'''
    applicant = Applicant.objects.filter(user=request.user).first()
    reference_id = request.POST.get('reference_id')
    reference = get_object_or_404(References, id=reference_id)
    reference_form = ReferenceForm(data=request.POST, instance=reference)

    if reference_form.is_valid():
        reference_form.save()
        return redirect('applicant')
    else:
        return redirect('applicant')


def remove_reference(request):
    '''Removes a reference instance from the applicants profile
    Redirects to profile'''
    reference_id = request.POST.get('reference_id')
    ref = get_object_or_404(References, id=reference_id)
    ref.delete()
    return redirect('applicant')


################################  SKILLS  #####################################
def add_skill(request):
    '''adds a skill to the users profile
    does not add it if it is already in the user data'''
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
    return redirect('applicant')


def remove_skill(request):
    '''Removes an experience instance from the applicants profile
    Redirects to profile'''
    applicant = Applicant.objects.filter(user=request.user).first()
    skill_name = request.POST.get('skill_name')
    skill = get_object_or_404(Skills, name=skill_name)
    cvskill = CVSkills.objects.filter(skill=skill, applicant=applicant).first()
    cvskill.delete()
    return redirect('applicant')


################################  OTHER  #####################################
@login_required(redirect_field_name="/login")
def applicant(request):
    '''Displays all data for an applicants Profile
    note: hasThing -> application specific Thing ..... CVThing -> Profile specific Thing'''
    applicant = Applicant.objects.filter(user=request.user).first()
    is_employee = Employee.objects.filter(user=request.user).exists()
    experiences = CVExperience.objects.filter(applicant=applicant).all()
    educations = CVEducation.objects.filter(applicant=applicant).all()
    references = CVReferences.objects.filter(applicant=applicant).all()
    app_skills = CVSkills.objects.filter(applicant=applicant).all()
    genres = SkillGenre.objects.all()
    skills = Skills.objects.all()
   
    


    if not applicant:
        applicant = {
            "full_name": request.user.get_full_name(),
            "email": request.user.email
        }

    all_skills = {}
    applicant_skills = {}
    for genre in genres:
        all_skills[genre] = []
        applicant_skills[genre] = []
    for skill in skills:
        all_skills[skill.genre].append(skill)
    for skill in app_skills:
        applicant_skills[skill.skill.genre].append(skill.skill)
    for ed in educations:
        ed.education.start_date = ed.education.start_date.strftime("%Y-%m-%d")
        ed.education.end_date = ed.education.end_date.strftime("%Y-%m-%d")
    for exp in experiences:
        exp.experience.start_date = exp.experience.start_date.strftime("%Y-%m-%d")
        exp.experience.end_date = exp.experience.end_date.strftime("%Y-%m-%d")

    context = {
        'applicant': applicant,
        'zip_options': ZipCode.objects.all(),
        'education_levels': EducationLevel.objects.all(),
        'experiences': experiences,
        'educations': educations,
        'references': references,
        'applicant_skills': applicant_skills,
        'all_skills': all_skills,
        'countries': Country.objects.all(),
        'cities': City.objects.all(),
        'is_employee': is_employee
    }
    return render(request, 'applicant/applicant.html', context)


@login_required(redirect_field_name="/login")
def index(request):
    '''index for certain applicant'''
    applicant = Applicant.objects.filter(user=request.user).first()
    return render(request, 'applicant/index.html', {'applicant': applicant})


@login_required(redirect_field_name="/login")
def apply_init(request, id, page):
    '''Displays all application data
    if application does not already exist, then it copies all
    data from the users profile to the application
    redirects to the application page'''
    applicant = Applicant.objects.filter(user=request.user).first()
    job = get_object_or_404(Job, pk=id)

    application = Application.objects.filter(job=job, applicant=applicant)
    if not application.exists():
        #Copy over all details from users profile to the application
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
            education.education.start_date = education.education.start_date.strftime("%Y-%m-%d")
            education.education.end_date = education.education.end_date.strftime("%Y-%m-%d")
            edu = hasEducation(application=application, education=education.education)
            edu.save()
        for reference in profile_references:
            ref = hasReferences(application=application, reference=reference.reference)
            ref.save()
        for skill in profile_app_skills:
            skl = hasSkills(application=application, skill=skill.skill)
            skl.save()
    else:
        application = application.first()

    #Getting application-specific user details (hasThing -> application)/(CVThing -> Profile)
    experiences = hasExperience.objects.filter(application=application).all()
    educations = hasEducation.objects.filter(application=application).all()
    references = hasReferences.objects.filter(application=application).all()
    app_skills = hasSkills.objects.filter(application=application).all()

    #Getting Skill information and formatting it correctly for the context-obj
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

    for education in educations:
        education.education.start_date = education.education.start_date.strftime("%Y-%m-%d")
        education.education.end_date = education.education.end_date.strftime("%Y-%m-%d")
    for experience in experiences:
        experience.experience.start_date = experience.experience.start_date.strftime("%Y-%m-%d")
        experience.experience.end_date = experience.experience.end_date.strftime("%Y-%m-%d")
    context = {
        'job': job,
        'applicant': applicant,
        'zip_options': ZipCode.objects.all(),
        'education_levels': EducationLevel.objects.all(),
        'experiences': experiences,
        'educations': educations,
        'references': references,
        'applicant_skills': applicant_skills,
        'all_skills': all_skills,
        'application': application,
        'page': str(page),
        'countries': Country.objects.all(),
    }
    return render(request, 'applicant/application/__init__.html', context)


def application_experience_edit(request, id):
    '''edits an instance of experience in an application'''
    applicant = Applicant.objects.filter(user=request.user).first()
    experience_id = request.POST.get('experience_id')
    experience = get_object_or_404(Experience, id=experience_id)
    experience_form = ExperienceForm(data=request.POST, instance=experience)

    if experience_form.is_valid():
        experience_form.save()
        return redirect('/applicants/application/' + str(id) + '/experience')
    else:
        return redirect('/applicants/application/' + str(id) + '/experience')


def application_remove_experience(request, id):
    '''removes an instance of experience from an application
    does not remove it from the users profile'''
    job = get_object_or_404(Job, pk=id)
    applicant = Applicant.objects.filter(user=request.user).first()
    application = Application.objects.filter(job=job, applicant=applicant).first()
    experience_id = request.POST.get('experience_id')
    experience = get_object_or_404(Experience, id=experience_id)
    exp = hasExperience.objects.filter(experience=experience, application=application).first()
    exp.delete()
    return redirect('/applicants/application/' + str(id) + '/experience')


def application_education_edit(request, id):
    '''edits an instance of education in an application'''
    applicant = Applicant.objects.filter(user=request.user).first()
    education_id = request.POST.get('education_id')
    education = get_object_or_404(Education, id=education_id)
    education_form = EducationForm(data=request.POST, instance=education)

    if education_form.is_valid():
        education_form.save()
        return redirect('/applicants/application/' + str(id) + '/education')
    else:
        return redirect('/applicants/application/' + str(id) + '/education')


def application_remove_education(request, id):
    '''removes an education from an application
    does not remove it from the profile'''
    job = get_object_or_404(Job, pk=id)
    applicant = Applicant.objects.filter(user=request.user).first()
    application = Application.objects.filter(job=job, applicant=applicant).first()
    education_id = request.POST.get('education_id')
    education = get_object_or_404(Education, id=education_id)
    edu = hasEducation.objects.filter(education=education, application=application).first()
    edu.delete()
    return redirect('/applicants/application/' + str(id) + '/education')


def application_reference_edit(request, id):
    '''edits a reference in the application'''
    applicant = Applicant.objects.filter(user=request.user).first()
    reference_id = request.POST.get('reference_id')
    reference = get_object_or_404(References, id=reference_id)
    reference_form = ReferenceForm(data=request.POST, instance=reference)

    if reference_form.is_valid():
        reference_form.save()
        return redirect('/applicants/application/' + str(id) + '/reference')
    else:
        return redirect('/applicants/application/' + str(id) + '/reference')


def application_remove_reference(request, id):
    '''removes a reference from an application
    does not remove it from the users profile'''
    job = get_object_or_404(Job, pk=id)
    applicant = Applicant.objects.filter(user=request.user).first()
    application = Application.objects.filter(job=job, applicant=applicant).first()
    reference_id = request.POST.get('reference_id')
    reference = get_object_or_404(References, id=reference_id)
    ref = hasReferences.objects.filter(reference=reference, application=application).first()
    ref.delete()
    return redirect('/applicants/application/' + str(id) + '/reference')


def application_experience_add(request, id):
    '''adds an instance of experience to an application
    does not add it to the users profile'''
    applicant = Applicant.objects.filter(user=request.user).first()
    job = get_object_or_404(Job, pk=id)
    application = Application.objects.filter(job=job, applicant=applicant).first()

    experience_form = ExperienceForm(data=request.POST)

    if experience_form.is_valid():
        experience = experience_form.save(commit=False)
        experience.save()
        exp = hasExperience(application=application, experience=experience)
        exp.save()
        return redirect('/applicants/application/' + str(id) + '/experience')
    else:
        return redirect('/applicants/application/' + str(id) + '/experience')


def application_education_add(request, id):
    '''adds an instance of education to the application
    does not add it to the users profile'''
    applicant = Applicant.objects.filter(user=request.user).first()
    job = get_object_or_404(Job, pk=id)
    application = Application.objects.filter(job=job, applicant=applicant).first()

    education_form = EducationForm(data=request.POST)
    if education_form.is_valid():
        education = education_form.save(commit=False)
        education.save()
        edu = hasEducation(application=application, education=education)
        edu.save()
        return redirect('/applicants/application/' + str(id) + '/education')
    else:
        return redirect('/applicants/application/' + str(id) + '/education')


def application_reference_add(request, id):
    '''adds a reference to the application
    does not add it to the users profile'''
    applicant = Applicant.objects.filter(user=request.user).first()
    job = get_object_or_404(Job, pk=id)
    application = Application.objects.filter(job=job, applicant=applicant).first()

    reference_form = ReferenceForm(data=request.POST)
    if reference_form.is_valid():
        reference = reference_form.save(commit=False)
        reference.save()
        ref = hasReferences(application=application, reference=reference)
        ref.save()
        return redirect('/applicants/application/' + str(id) + '/reference')
    else:
        return redirect('/applicants/application/' + str(id) + '/reference')


def application_add_skill(request, id):
    '''adds a skll to an application
    does not add it to the users profile'''
    applicant = Applicant.objects.filter(user=request.user).first()
    app_skills = CVSkills.objects.filter(applicant=applicant).all()
    job = get_object_or_404(Job, pk=id)
    application = Application.objects.filter(job=job, applicant=applicant).first()
    token, data = request.POST.items()
    genre, skill = data
    validity = True
    for app_skill in app_skills:
        if skill in app_skill.skill.name:
            validity = False
    if validity:
        skill_object = Skills.objects.filter(name=skill).first()
        hasskill = hasSkills(application=application, skill=skill_object)
        hasskill.save()
    return redirect('/applicants/application/' + str(id) + '/skill')


def application_remove_skill(request, id):
    '''removes a skill from an application
    does not remove it from the applicants profle'''
    job = get_object_or_404(Job, pk=id)
    applicant = Applicant.objects.filter(user=request.user).first()
    application = Application.objects.filter(job=job, applicant=applicant).first()
    skill_name = request.POST.get('skill_name')
    skill = get_object_or_404(Skills, name=skill_name)
    hasskill = hasSkills.objects.filter(skill=skill, application=application).first()
    hasskill.delete()
    return redirect('/applicants/application/' + str(id) + '/skill')


def application_cover_letter(request, id):
    '''updates/saves the cover letter of an application
    rediriects to the application's page'''
    job = get_object_or_404(Job, pk=id)
    applicant = Applicant.objects.filter(user=request.user).first()
    application = Application.objects.filter(job=job, applicant=applicant).first()
    covlet = request.POST['cover-letter']

    application.cover_letter = covlet
    print(application.cover_letter)
    application.save()
    return redirect('/applicants/application/' + str(id) + '/cover-letter')


def final_apply(request, id):
    '''makes an application un-accessible for the user
        accessible for the company
        and redirects the user to the success_message page'''
    application = get_object_or_404(Application, pk=id)
    application.is_submitted = True
    application.save()
    context = {
        'job_name': application.job.name,
        'company_name': application.job.company
    }
    return render(request, 'applicant/application/success_message.html', context)

from django.db import models
from django.contrib.auth.models import User
from common.models import Skills, ZipCode


class Applicant(models.Model):
    '''Class conatining all data for all users'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=70)
    profile_image = models.CharField(max_length=9999)
    email = models.EmailField()
    phone = models.CharField(max_length=7)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=120)
    bio = models.CharField(max_length=400, null=True)

    def __str__(self):
        return str(self.user.get_full_name())


class CVSkills(models.Model):
    '''Class that connects a user's profile to a specific Skill in our
    skill list'''
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.applicant) + ": " + str(self.skill.name) 
    

class Experience(models.Model):
    '''Class that contains all data for an input instance of "Experience"'''
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)

    def __str__(self):
        return str(self.workplace_name) + " - " + str(self.role) + " - " + str(self.start_date)


class CVExperience(models.Model):
    '''Class that connects a specific Experience to a specific applicant'''
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.applicant.full_name) + " - " + str(self.experience.workplace_name)


class EducationLevel(models.Model):
    '''CLass that contains a list of all education levels'''
    level = models.CharField(max_length=255)

    def __str__(self):
        return self.level


class Education(models.Model):
    '''Class that contains all data for an input instance of "Education"'''
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)

    def __str__(self):
        return str(self.school_name) + " " + str(self.degree) + " " + str(self.level) + " " + str(self.start_date)


class CVEducation(models.Model):
    '''Class that connects a specific instance of Education to a specific applicant'''
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.applicant.full_name) + ' - ' + str(self.education.degree) + ' - ' + str(self.education.level)

class References(models.Model):
    '''Class that contains all data for an input instance of "Reference"'''
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    is_contactable = models.BooleanField()

    def __str__(self):
        return str(self.name) + " " + str(self.role)


class CVReferences(models.Model):
    '''Class that coonnects a specific reference to a specific applicant'''
    reference = models.ForeignKey(References, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.applicant.full_name) + ' - ' + str(self.reference.name)

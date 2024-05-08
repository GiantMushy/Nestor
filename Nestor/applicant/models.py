from django.db import models
from user.models import Profile 
from common.models import Skills


class Applicant(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bio = models.CharField(max_length=400, null=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user.user.username)


class CVSkills(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.applicant.user.user.username) + ": " + str(self.skill.name) 
    

class Experience(models.Model):
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)

    def __str__(self):
        return str(self.workplace_name) + " " + str(self.role) + " " + str(self.start_date)


class CVExperience(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)


class EducationLevel(models.Model):
    level = models.CharField(max_length=255)

    def __str__(self):
        return self.level


class Education(models.Model):
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)

    def __str__(self):
        return str(self.school_name) + " " + str(self.degree) + " " + str(self.level) + " " + str(self.start_date)


class CVEducation(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)


class References(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    is_contactable = models.BooleanField()

    def __str__(self):
        return str(self.name) + " " + str(self.role)


class CVReferences(models.Model):
    reference = models.ForeignKey(References, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

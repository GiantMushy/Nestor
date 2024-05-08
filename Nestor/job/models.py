from django.db import models
from company.models import Company
from common.models import ZipCode, Skills
from applicant.models import Applicant, Experience, Education, References


class JobType(models.Model):  #summer/internship/part-time/fulltime
    type = models.CharField(max_length=100)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_image = models.CharField(max_length=9999)
    name = models.CharField(max_length=255)
    address = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000)
    date_of_offering = models.DateField()
    application_due_date = models.DateField()
    starting_date = models.DateField()
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    percentage = models.IntegerField()
    num_of_applicants = 0
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name) + ", " + self.company.name


class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


class hasSkills(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)


class hasExperience(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)


class hasEducation(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)


class hasReferences(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    reference = models.ForeignKey(References, on_delete=models.CASCADE)

from django.db import models
from company.models import Company
from common.models import ZipCode, Skills, JobCategory
from applicant.models import Applicant, Experience, Education, References
from django.utils import timezone
from django.contrib.auth.models import User


class JobType(models.Model):  #summer/internship/part-time/fulltime
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    job_category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    job_image = models.CharField(max_length=9999, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    date_of_offering = models.DateField(default=timezone.now)
    application_due_date = models.DateField()
    starting_date = models.DateField()
    num_of_applicants = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name) + ", " + self.company.name


class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    cover_letter = models.TextField(max_length=1000, blank=True, null=True)
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.applicant.full_name) + ' - ' + str(self.job.name)


class FavoriteJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.get_full_name()) + ' - ' + str(self.job.name)


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

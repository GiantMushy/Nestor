from django.db import models
from company.models import Company
from common.models import ZipCode

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
    type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    percentage = models.IntegerField()
    num_of_applicants = models.IntegerField(null=True)
    is_available = models.BooleanField()

    def __str__(self):
        return str(self.name) + ", " + self.company.name



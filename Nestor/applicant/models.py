from django.db import models
from user.models import User
from common.models import Skills


class Experience(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)

    
    def __str__(self):
        return self.workplace_name

class EducationLevel(models.Model):
    level = models.CharField(max_length=255)

    def __str__(self):
        return self.level


class Education(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)

    def __str__(self):
        return self.school_name

class References(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    is_contactable = models.BooleanField()

    def __str__(self):
        return self.name

from django.db import models
from user.models import User
from common.models import Skills


class Experience(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)


class EducationLevel(models.Model):
    level = models.CharField(max_length=255)


class Education(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True, null=True)


class References(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    workplace_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    is_contactable = models.BooleanField()



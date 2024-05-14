from django.db import models
from django.contrib.auth.models import User
from common.models import ZipCode


class Company(models.Model):
    name = models.CharField(max_length=100)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    description = models.TextField(max_length=1000)
    link = models.URLField(max_length=1000)
    logo = models.CharField(max_length=9999)
    cover_image = models.CharField(max_length=9999, null=True, blank=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.get_full_name()) + ", " + str(self.company.name)

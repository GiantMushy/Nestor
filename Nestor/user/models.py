from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class ZipCode(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zip = models.CharField(max_length=20)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    email = models.EmailField()
    SSN = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=7)
    description = models.CharField(max_length=9999)
    is_company = models.BooleanField()
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)



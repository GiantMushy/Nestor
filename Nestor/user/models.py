from django.db import models
from django.contrib.auth.models import User
from common.models import ZipCode
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    email = models.EmailField()
    SSN = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=7)
    description = models.CharField(max_length=9999)
    is_company = models.BooleanField()
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)



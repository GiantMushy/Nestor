from django.db import models
from django.contrib.auth.models import User
from common.models import ZipCode
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    email = models.EmailField()
    phone = models.CharField(max_length=7)
    zipcode = models.ForeignKey(ZipCode, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=120)
    
    def __str__(self):
        return str(self.user)

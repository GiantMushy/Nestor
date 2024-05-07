from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=7)
    description = models.CharField(max_length=9999)
    is_company = models.BooleanField()
    




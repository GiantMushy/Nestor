from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    SSN = models.IntegerField(max_length=10)
    link = models.URLField(max_length=1000)

    def __str__(self):
        return self.name

class CompanyImage(models.Model):
    image = models.CharField(max_length=9999)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


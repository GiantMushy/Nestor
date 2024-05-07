from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class ZipCode(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zip = models.CharField(max_length=20)


class Skills(models.Model):
    genre = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

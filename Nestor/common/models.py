from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class ZipCode(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return str(self.city) + " " + str(self.zip)


class SkillGenre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Skills(models.Model):
    genre = models.ForeignKey(SkillGenre, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class JobCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

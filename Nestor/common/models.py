from django.db import models


class Country(models.Model):
    '''List of Countries'''
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    '''List of Cities with reference to their respective Countries'''
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class ZipCode(models.Model):
    '''List of ZipCodes with reference to their respective Cities'''
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return str(self.city) + " " + str(self.zip)


class SkillGenre(models.Model):
    '''List of all Skill Genres
    genres: Programming Languages, Languages, Outdoor Activites, Sports, Liscenses, Hobbies'''
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Skills(models.Model):
    '''List of all Skills with reference to their respective Genre
    i.e. name: Python -> genre: Programming Language'''
    genre = models.ForeignKey(SkillGenre, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class JobCategory(models.Model):
    '''List of all Job Categories'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

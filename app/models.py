from django.db import models

# Create your models here.
class userData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    nationality = models.CharField(max_length=100, default='Bangladeshi')

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    def __str__(self):
        return self.country_name

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    section = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    roll = models.IntegerField()
    country = models.ForeignKey(Country, default=True, on_delete=models.CASCADE)
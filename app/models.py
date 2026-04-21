from django.db import models

# Create your models here.
class userData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    nationality = models.CharField(max_length=100, default='Bangladeshi')

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    section = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    roll = models.IntegerField()
from django.db import models
from django_fields import DefaultStaticImageField

# Create your models here.



class user(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    family_type = models.CharField(max_length=10)
    login = models.CharField(max_length=100)
    ml_model = models.CharField(max_length=100)



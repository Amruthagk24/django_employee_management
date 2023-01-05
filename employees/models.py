from django.db import models
from django import forms

class loginmodel(models.Model):
    # default = ''
    uname = models.CharField(max_length=100)

    password = models.CharField(max_length=15)
    type=models.CharField(max_length=20)


    class Meta:
        db_table = "login"

class employemodel(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    gen22 = models.CharField(max_length=100)
    class Meta:
        db_table = "emp"


class charity(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        db_table="ee"

# Create your models here.

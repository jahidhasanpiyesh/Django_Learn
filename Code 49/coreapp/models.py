from django.db import models

# Create your models here.
class User(models.Model):
    studentname=models.CharField(max_length=70)
    techername=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=70)
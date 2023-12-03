from django.db import models

# Create your models here.

class Enroll(models.Model):
    stid = models.IntegerField()
    name = models.CharField(max_length=70)
    department = models.CharField(max_length=20)
    address = models.TextField(max_length=70)
    email_address = models.EmailField(max_length=40)
    phone_number = models.TextField(max_length=19)
    
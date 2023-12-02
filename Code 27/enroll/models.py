from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=25)
    stuemail = models.EmailField(max_length=18)
    stupass = models.CharField(max_length=26)
    comments = models.TextField(max_length=40, default="not available")
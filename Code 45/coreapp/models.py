from django.db import models

# Create your models here.

class User(models.Model):
    # Use to blank = True --- then error massage not show this fileds ----
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
from django.db import models

# Create your models here.
# create and show data for admin panal 
class Student(models.Model):
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=60)
    
    # Show spacific data name show 
    def __str__(self):
        return self.stuname
    
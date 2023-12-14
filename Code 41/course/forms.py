from django import forms
from django.core import validators
class RegisterFrom(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(validators=[validators.MaxLengthValidator(15)])
    
    
"""
Please learn this note ----
 
--- import validators
--- name or email filed use to validators=[validators.MaxLengthValidator(any requirments text)]
"""
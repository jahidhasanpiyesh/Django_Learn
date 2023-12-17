from django import forms
from django.core import validators

def Custom_validate_name (value):
    if value[0] !=  'M':
        raise forms.ValidationError("Please Start to First Char M")

def Custom_validate_email(value1):
    if value1 != '@':
        raise forms.ValidationError("Please use to @ .com")

class RegisterFrom(forms.Form):     
    name = forms.CharField(validators=[Custom_validate_name])
    email = forms.EmailField(validators=[Custom_validate_email])
    
    
"""
Please learn this note ----
 
--- import validators
--- use to conditions 
"""
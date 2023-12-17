from django import forms
from django.core import validators

def Custom_valid_name(value):
    if value != "@":
        raise forms.ValidationError("Please Enter @gmail.com")

class StudentForms(forms.Form):
    name = forms.CharField(min_length=6, max_length=25,error_messages={"required":"Please Enter Your Valid Name"})
    email = forms.EmailField(min_length=7, max_length=45,error_messages={"required":"Please Enter Your Valid Email"},required=[Custom_valid_name])
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label="Password(again)" ,widget=forms.PasswordInput)
    
    def clean(self):
        clean_data=super().clean()
        vname = self.cleaned_data["password"]
        vname1 = self.cleaned_data["rpassword"]
        if vname != vname1:
            raise forms.ValidationError("Password Not Matched")
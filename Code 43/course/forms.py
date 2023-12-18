from django import forms


class StudentForms(forms.Form):
    name = forms.CharField(min_length=6, max_length=25,error_messages={"required":"Please Enter Your Valid Name"})
    email = forms.EmailField(min_length=7, max_length=45,error_messages={"required":"Please Enter Your Valid Email"})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={"required":"Please Enter Strong Password"})
   
    
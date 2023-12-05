from django import forms

class StudentRegister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
  
from django import forms

class Studentforms(forms.Form):
    name = forms.CharField(min_length=6, max_length=20)
    email = forms.EmailField(min_length=6, max_length=40)
    password = forms.CharField(min_length=6, max_length=20)
from django import forms

class StudentForms(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    
    # undascor not show this output just first latter capital trying to code -
    first_name = forms.CharField()
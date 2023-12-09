from django import forms

class StudentRegister(forms.Form):
    # use to initial value and help text show this forms.html file
    name = forms.CharField()
    email = forms.EmailField()
    
    # create new input box 
    mobile = forms.IntegerField()
    
    # Hiden Fields ------
    key = forms.CharField(widget=forms.HiddenInput())
  
  
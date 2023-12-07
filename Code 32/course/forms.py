from django import forms

class StudentRegister(forms.Form):
    # use to initial value and help text show this forms.html file
    name = forms.CharField(initial="My name is Jahid",help_text="please dont try this topics")
    email = forms.EmailField()
  
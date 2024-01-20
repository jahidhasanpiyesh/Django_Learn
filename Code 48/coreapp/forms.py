from django import forms
from .models import User
class UserForms(forms.ModelForm):
    class Meta:
        model=User
        # # First way All fields show
        # fields = ('__all__')
        
        # # Second way All fields show and fixig way use 
        # fields = ('name','email','password')
        
        # # Thard way fixing fields not show 
        # # exclude = ('name',)
        exclude = ['name']
        
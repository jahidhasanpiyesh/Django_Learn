from django.contrib.auth.forms import User 
from django import forms
# input django creating forms -- try to update 
from django.contrib.auth.forms import UserCreationForm

class Sigh_Up_forms(UserCreationForm):
    
    # lables tag name change --
    password1 = forms.CharField(label='Confirm Password (agin)',widget=forms.PasswordInput)
    class Meta:
        model = User
        
        # show any fields Just flow this code 
        fields=['username','first_name','last_name','email']
        # lables tag change try
        labels = {'email':"Email"}

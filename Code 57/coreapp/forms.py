from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class UserChange(UserChangeForm):
    password = None
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email','last_login','date_joined']
        

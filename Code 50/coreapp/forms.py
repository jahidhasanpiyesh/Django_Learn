from django import forms
from .models import User
class studentforms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['studentname','email','password']
        
# Inherit studentforms class ---- or Meta inherit   
class techerforms(studentforms):
    class Meta(studentforms.Meta):
       fields = ['techername','email','password']
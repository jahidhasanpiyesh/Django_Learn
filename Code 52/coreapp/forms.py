from django import forms
from .models import User
class StudentForms(forms.ModelForm):
    class Meta:
        model = User
        fields=('__all__')
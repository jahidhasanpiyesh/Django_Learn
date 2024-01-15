from django import forms
from . models import User
class RegisterForms(forms.ModelForm):
    class Meta:
        model=User
        # fields ----Use to [] or ()----
        # Serial wyas filed name set any requirments --
        fields=('name','email','password')
        labels={'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
        error_messages={
            'name':{'required' : 'Must Be Enter Your Valid Name'}
            }
        widgets={
            
            # password hiden dont show type password 
           'password':forms.PasswordInput,
           
           # class set -----
           'name':forms.TextInput(attrs={'class':'Muclass','placeholder':'Please Enter Your Name'}),
           'email':forms.TextInput(attrs={'placeholder':'Please Enter Your Email'}),
           'password':forms.TextInput(attrs={'placeholder':'Please Enter Your Password'})
           }
        
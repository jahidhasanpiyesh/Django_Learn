from django import forms

class FormRegister(forms.Form):
   
    name = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        clean_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        
        # error massage step to step ! first error fix and solve then second error !
        if len(valname) < 4 :
            raise forms.ValidationError('Please Try to 4 char up letter')
        
        if len(valemail) < 10 :
            raise forms.ValidationError("Please Try to Email 10 letter up") 
from django import forms

class StudentRegister(forms.Form):
    # widget use to spacial way data input --- not try esy data input filed !
    # name = forms.CharField(widget=forms.PasswordInput())

    # # use to widget = Textarea 
    # name = forms.CharField(widget=forms.Textarea)
    
    # # use to widget = ChackboxInput()
    # name = forms.CharField(widget=forms.CheckboxInput())
    
    # # use to widget = FileInput()
    # name = forms.CharField(widget=forms.FileInput())
    
    # use to attrs={"class":"Someone","id":"unicid"}---id == not a chaptal letter just small letter !
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"Someone","id":"unicid"}))
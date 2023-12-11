from django import forms

class FormRegister(forms.Form):
    # using to ---  empty_value="any data"  and more then 
    # strip=True/False    True= Space not use to output  -------False = Space use to output-     
    name = forms.CharField(min_length=5, max_length=10 ,strip=True,
                           error_messages={'required':"Please Enter Your Name"}, label_suffix= " ")
    submit = forms.BooleanField(label='Chack Mark', error_messages={'required':"Please Chack Mark On"},
                                label_suffix=" ")
    price = forms.DecimalField( min_value=5, max_digits=10, decimal_places=1)
    rate = forms.IntegerField(min_value=5, max_value=10)
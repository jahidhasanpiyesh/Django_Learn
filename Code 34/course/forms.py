from django import forms

class StudentRegister(forms.Form):
    # use to initial value and help text show this forms.html file
    
    # First Way use to this code ---------
    # Use to label_suffix = " any spacial icon and space "
    # Use to initial = Value and any text type 
    # Use to required = True / False 
    # Use to disabled = True  and Text Filed not rename 
    # initial value parformenc is Low
    name = forms.CharField(label="Your Name", label_suffix=" ", initial="Please Your Name Enter", 
                           required=False, disabled=True, help_text=" lemit 70 Char ")
    
    # Second Way use to this code --------
    # your_Name = forms.CharField()  # But just first char big and all char small text
    
  
  
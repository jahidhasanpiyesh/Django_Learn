from django.shortcuts import render
from .forms import Studentforms
from .models import User
# Create your views here.
def student(request):
    
    if request.method == 'POST':
        print('Use to POST Method')
        s = Studentforms(request.POST)
        if s.is_valid():
            nm = s.cleaned_data['name']
            em = s.cleaned_data['email']
            pas = s.cleaned_data['password']
            
            Save_data = User(name=nm, email=em, password=pas)
            Save_data.save()
    else:
        print("Use To Get Mehtod")   
    S = Studentforms()
    return render(request,'coreapp/index.html',{'form':S})
from django.shortcuts import render
from .models import User
from .forms import StudentForms
# Create your views here.

def Student(request):
    if request.method == 'POST':
        print("Use to POST Method")
        S = StudentForms(request.POST)
        if S.is_valid():
            nm=S.cleaned_data['name']
            em=S.cleaned_data['email']
            pas=S.cleaned_data['password']
            save_data=User(name=nm,email=em,password=pas)
            save_data.save()
            
    else:
        print("Use to Get Method")
        S = StudentForms()
    return render(request,'coreapp/index.html',{'form':S})
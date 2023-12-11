from django.shortcuts import render
from . forms import FormRegister
from django.http import HttpResponseRedirect
# Create your views here.

# spacific function run spacific url 
def massage(request):
    return render(request,'courseApp/success.html')

def course(request):
    if request.method == "POST":
        f = FormRegister(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            password = f.cleaned_data['password']
            
            print("Name:", name)
            print("Email:", email)
            print("Password:", password)
            
            # use to HttpResponseRedirect spacific link create this site run 
            return HttpResponseRedirect('/reg/success/')
            # return render(request,'courseApp/success.html', {'nm': name})
        
    else:
        f = FormRegister()
        print("use to get method")
    return render(request,'courseApp/home.html', {'form': f})
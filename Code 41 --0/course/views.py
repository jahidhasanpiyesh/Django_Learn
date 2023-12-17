from django.shortcuts import render
from .forms import RegisterFrom
# Create your views here.

def course(request):
    
    if request.method == 'POST':
        print("using to POST method")
        reg = RegisterFrom(request.POST)
        if reg.is_valid():
            print("Name:",reg.cleaned_data["name"])
            print("Email:",reg.cleaned_data["email"])
    
    else:
        print("using to GET method")
        reg = RegisterFrom()
    return render(request,'course/home.html',{'from': reg})
from django.shortcuts import render
from. forms import StudentRegister
# Create your views here.
def courseApp(request):
    if request.method == "POST":
        f = StudentRegister(request.POST)
        if f.is_valid():
            print(" it is valid ")
            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            password = f.cleaned_data['password']
            print("Name:", name)
            print("Email:", email)
            print("Password:", password)
    
    else:
        f = StudentRegister()
        print("using to get method")   
    return render(request, 'courseApp/home.html', {"form": f})
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


# Singup Base Functions --------
def Sign_up(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your Form is Submit Successfully !!')
            fm.save()
        fm = UserForm()        
    else:
        fm = UserForm()
    return render(request, 'coreapp/signup.html', {'from':fm})


# Login Base Functions ------
def log_in(request):
    
    # 
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Your Account Login Successfully !!')
                    return HttpResponseRedirect('/profile/')
            fm = AuthenticationForm()   
        else:
            fm = AuthenticationForm()  
        return render(request, 'coreapp/login.html', {'from':fm})
    else:
        return HttpResponseRedirect('/profile/')
    
    
# Logout Base Functions -----
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Profile Base Functions -----
def profile(request):
    if request.user.is_authenticated:
        return render(request,'coreapp/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
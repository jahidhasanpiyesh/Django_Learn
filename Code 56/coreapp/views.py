from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.


# Singup Base Functions --------
def Sign_up(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():  # chack valid data 
            messages.success(request, 'Your Form is Submit Successfully !!')
            fm.save()       
    else:
        fm = UserForm()
    return render(request, 'coreapp/signup.html', {'from':fm})


# Login Base Functions ------
def log_in(request):
    
    # please chack user data is_authenticated 
    if not request.user.is_authenticated:
        if request.method == 'POST':   # use to Post method 
            # import AuthenticationForm()  in ---from django.contrib.auth.forms
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():    # chack valid data
                # and call cleaned_data 
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                     # import login() in ---from django.contrib.auth
                    login(request,user)
                    # built message funciton just user -- 
                    messages.success(request, 'Your Account Login Successfully !!')
                    # import HttpResponseRedirect()
                    return HttpResponseRedirect('/profile/')   
        else:
            fm = AuthenticationForm()  
        return render(request, 'coreapp/login.html', {'from':fm})
    else:
        return HttpResponseRedirect('/profile/')
    
    
# Logout Base Functions -----
def log_out(request):
    # import logout() in ---from django.contrib.auth
    logout(request)
    return HttpResponseRedirect('/login/')


# Profile Base Functions -----
def profile(request):
    # Please Call is_authenticated Functions 
    if request.user.is_authenticated:
        return render(request,'coreapp/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

# Change Password Without old password just call setpasswordform()--functions with pass same code --
# Change Password With old password Functions Base------
def changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # please import --PasswordChangeForm() in --from django.contrib.auth.forms
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                
                # session maintain i mean its call then run and solve this 
                # submit change pass and show profile page  
                update_session_auth_hash(request,fm.user)
                messages.success(request, 'Your Password Change Successfully !!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'coreapp/changepass.html',{'form':fm})
    
    else:
        return HttpResponseRedirect('/login/')
    

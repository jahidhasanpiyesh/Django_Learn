from django.shortcuts import render
from django.contrib import messages
# import to forms class 
from .forms import Sigh_Up_forms
# Create your views here.
def home(request):
    if request.method == 'POST':
        F = Sigh_Up_forms(request.POST)
        if F.is_valid():
            F.save()
            messages.success(request,'Your Forms Submit Successfully !')
    else:
        F = Sigh_Up_forms()
    return render(request, 'home.html',{'form':F})
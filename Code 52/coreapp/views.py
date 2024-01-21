from django.shortcuts import render
from .forms import StudentForms
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        S = StudentForms(request.POST)
        if S.is_valid():
            S.save()
            messages.info(request,'message in info')
            messages.success(request,'message in success')
            messages.error(request,'message in error')
            messages.warning(request,'message in warning')
    else:
        S = StudentForms()
    return render(request,'index.html',{'form':S})
from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'corinfo/base.html')

def home(request):
    return render(request,'corinfo/home.html')

def about(request):
    return render(request,'corinfo/about.html')
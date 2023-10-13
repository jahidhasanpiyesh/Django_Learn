from django.shortcuts import render


# Create your views here.

def home(request):
    info = {'nm': 'Django is amazing'}
    return render(request , 'HTML/index.html' , info)

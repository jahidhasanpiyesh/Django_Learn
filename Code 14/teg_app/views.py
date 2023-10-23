from django.shortcuts import render

# Create your views here.

def index(request):
    # function true run code and output show function false then not output show this code 
    return render(request,"HTML/index.html",{'name':True,'roll':472826})  
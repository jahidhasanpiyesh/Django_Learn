from django.shortcuts import render
from .forms import UserForms
# Create your views here.
def index(request):
    f = UserForms()  
    return render(request,'index.html',{'form':f})
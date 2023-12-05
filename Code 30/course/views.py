from django.shortcuts import render
from .forms import StudentRegister
# Create your views here.
def forms(request):
    ff = StudentRegister()
    return render(request,"course/forms.html",{"st": ff})
from django.shortcuts import render
from .forms import StudentRegister
# Create your views here.
def forms(request):
    # initial value parformenc is high
    ff = StudentRegister()
    return render(request,"course/forms.html",{"st": ff})
from django.shortcuts import render
from . forms import FormRegister
from django.http import HttpResponseRedirect
# Create your views here.
def course(request):
    if request.method == "POST":
        f = FormRegister(request.POST)
        if f.is_valid():
            print("Name :",f.cleaned_data['name'])
            print("Chack Mark :",f.cleaned_data['submit'])
            print("Price",f.cleaned_data['price'])
            print("Rate",f.cleaned_data['rate'])
    else:
        f = FormRegister()
    return render(request,'courseApp/home.html', {'form': f})
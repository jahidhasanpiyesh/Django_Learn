from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        h = UserCreationForm(request.POST)
        if h.is_valid():
            h.save()
    else:
        h = UserCreationForm()
    return render(request,'index.html',{'form':h})
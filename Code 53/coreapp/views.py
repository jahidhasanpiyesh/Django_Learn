from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        F = UserCreationForm(request.POST)
        if F.is_valid():
            F.save()
    else:
        F = UserCreationForm()
    return render(request, 'home.html',{'form':F})
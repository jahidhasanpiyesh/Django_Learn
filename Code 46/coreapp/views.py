from django.shortcuts import render
from .forms import RegisterForms
# Create your views here.
def Register(request):
    if request.method == 'POST':
        S = RegisterForms(request.POST)
        if S.is_valid():
            nm = S.cleaned_data['name']
            em = S.cleaned_data['email']
            pw = S.cleaned_data['password']
            print(nm)
            print(em)
            print(pw)
    else:
        print('Use to Get Method')
        S=RegisterForms()
    return render(request,'index.html',{'from':S})
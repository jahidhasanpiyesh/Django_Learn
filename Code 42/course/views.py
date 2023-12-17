from django.shortcuts import render
from .forms import StudentForms
# Create your views here.
def Student(request):
    if request.method == 'POST':
        print("Use to  POST Method")
        S = StudentForms(request.POST)
        if S.is_valid():
            print("Name:",S.cleaned_data['name'])
            print("Email:",S.cleaned_data['email'])
            print("Password:",S.cleaned_data['password'])
            print("RePassword:",S.cleaned_data['rpassword'])
    else:
        print('Use to GET Method')
        S = StudentForms()
    return render(request,'course/home.html',{'from': S})
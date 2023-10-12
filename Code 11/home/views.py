from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'Md Jahid Hasan'
    department = 'CSE'
    roll = 472826
    data = {'nm':name, 'dep':department, 'rol':roll}
    return render(request,'HTML/index.html', data)
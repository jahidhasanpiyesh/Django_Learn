from django.shortcuts import render
from .forms import studentforms,techerforms

# Create your views here.
def student(request):
    if request.method == 'POST':
        s = studentforms(request.POST)
        if s.is_valid():
            s.save()
    else:
        s = studentforms()        
    return render(request,'student.html',{'st':s})

def techer(request):
    if request.method == 'POST':
        t = techerforms(request.POST)
        if t.is_valid():
            t.save()
    else:
        t = techerforms()
    
    return render(request,'techer.html',{'te':t})

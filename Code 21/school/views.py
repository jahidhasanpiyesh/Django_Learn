from django.shortcuts import render

# Create your views here.
def school(request):
    return render(request,'school/index.html',{'school':'I am index'})
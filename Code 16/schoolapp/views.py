from django.shortcuts import render

# Create your views here.
def school(request):
    return render(request,'index.html',{'nm':'phulpur_high','sit':77})
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request,id,chack):
    print(chack)
    if id == 1:
        s= 'rohan'
    if id == 2:
        s= 'rahol'
    if id == 3:
        s= 'roshid'
    return render(request,'home.html',{'name':s})
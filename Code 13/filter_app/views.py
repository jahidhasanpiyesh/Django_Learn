from django.shortcuts import render
# Create your views here.

def filter_pro(request):
    
    return render(request,"HTML/index.html",{'p1':72.3256, 'p2':88.32569, 'p3':99.365, 'p4':55.00000})
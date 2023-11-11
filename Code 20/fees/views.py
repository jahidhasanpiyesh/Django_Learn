from django.shortcuts import render

# Create your views here.

def feesone(request):
    return render(request,'fees/feesone.html',{'num':'Fees one Python With Django'})

def feestwo(request):
    return render(request,'fees/feestwo.html',{'data':'Fees two Python With Django'})
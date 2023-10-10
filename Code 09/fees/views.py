from django.shortcuts import render

# Create your views here.
def feesfirst(request):
    return render(request, 'fees/feesone.html')

def feessecond(request):
    return render(request, 'fees/feestwo.html')
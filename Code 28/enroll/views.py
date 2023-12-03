from django.shortcuts import render
from.models import Enroll
# Create your views here.
def enroll(request):
    # all data show to try this code and comment one code 
    # move to enroll.html file 
    # en = Enroll.objects.all()
    
    # Spacific one data show just comment one this code and 
    # move to enroll.html file 
    en = Enroll.objects.get(pk=3)
    
    return render(request,"enroll/enroll.html", {"enr": en})
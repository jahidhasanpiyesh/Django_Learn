from django.shortcuts import render
from datetime import datetime
# Create your views here.
def calander(request):
    date = datetime.now()
    return render (request,'index.html',{'dt':date})
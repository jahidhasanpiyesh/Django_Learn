from django.shortcuts import render

# Create your views here.
def coursefirst(request):
    return render(request,'course/courseone.html')

def coursesecond(request):
    return render(request,'course/coursetwo.html')
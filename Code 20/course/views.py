from django.shortcuts import render

# Create your views here.
def courseone(request):
    return render(request,'course/courseone.html',{'nm':'Course one Django With Python'})

def coursetwo(request):
    return render(request,'course/coursetwo.html',{'dt':'Course two Django with Python'})
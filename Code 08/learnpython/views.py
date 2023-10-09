from django.shortcuts import render

# Create your views here.
def learnpy(requenst):
    return render(requenst , 'home.html')
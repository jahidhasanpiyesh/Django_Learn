from django.shortcuts import render

# Create your views here.
def learndj(requenst):
    return render(requenst , 'index.html')
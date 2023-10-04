from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def firstapp(request):
    return HttpResponse("Hello first app")


def firstapps(request):
    return HttpResponse("Hello first apps")

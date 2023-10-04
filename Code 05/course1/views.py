from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def cour1(request):
    return HttpResponse("Hello this my first app")


def cour11(request):
    return HttpResponse("Hi Their")

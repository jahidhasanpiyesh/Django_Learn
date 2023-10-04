from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def cour2(request):
    return HttpResponse("Hello this my second app")


def cour22(request):
    return HttpResponse("Hi Their all")
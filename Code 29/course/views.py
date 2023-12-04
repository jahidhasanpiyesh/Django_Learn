from django.shortcuts import render
from .models import Student
# Create your views here.
def student(request):
    info = Student.objects.all()
    return render(request,"course/home.html",{"stu":info})
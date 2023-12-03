from django.shortcuts import render
from .models import Student
# Create your views here.
def student(request):
    stud = Student.objects.all()
    return render(request,"resource/home.html",{"stu": stud})
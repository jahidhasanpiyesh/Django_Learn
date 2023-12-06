from django.shortcuts import render
from .models import Student
from .forms import StudentForms
# Create your views here.
def student(request):
    stu = Student.objects.all()
    return render(request,"course/course.html",{"s":stu})

def studentforms(request):
    # use to ------True/False/String any_%3 etc
    # new use to label_suffix=' any spaciel icon and word etc'
    # new use to initial = { : }  all name field data show and inital value show --
    sf = StudentForms(auto_id=True,label_suffix=' ',initial={"name":"Md Jahid Hasan"})
    return render(request,"course/course.html",{"SF":sf})
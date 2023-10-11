from django.shortcuts import render

# Create your views here.
def coursefirst(request):
    advance = {'name':'in python'}
    return render(request,'course/courseone.html', advance) 

def coursesecond(request):
    name = "MD Jahid Hasan"
    roll = 472826
    cgpa = 3.98
    all_info = {'nm':name, 'rol':roll, 'gpa':cgpa}
    return render(request,'course/coursetwo.html',all_info)
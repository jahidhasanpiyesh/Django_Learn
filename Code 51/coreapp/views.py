from django.shortcuts import render
from .forms import studentforms,techerforms

# please import messages 
from django.contrib import messages

# Create your views here.
def student(request):
    if request.method == 'POST':
        s = studentforms(request.POST)
        if s.is_valid():
            s.save()
            
            # # first Way use to messages 
            # messages.add_message(request,messages.SUCCESS,'New Student Informetions Add Successfull !')
           
            # set message level name and show message or DEBUG SIMPLE 
            messages.set_level(request,messages.DEBUG)
            # message not show but why ?
            messages.debug(request, "New Student Informetions Add Successfull !")
            # Print out this level number 
            print(messages.get_level(request))
            
    else:
        s = studentforms()        
    return render(request,'student.html',{'st':s})

def techer(request):
    if request.method == 'POST':
        t = techerforms(request.POST)
        if t.is_valid():
            t.save()
            
            # Second Way use to messages 
            messages.info(request, "New Techer Informetions Add Successfully")
    else:
        t = techerforms()
    
    return render(request,'techer.html',{'te':t})
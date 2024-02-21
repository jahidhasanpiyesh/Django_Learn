from django.shortcuts import render

# Create your views here.
def homesessaion(request):
    return render(request, 'coreapp/sessaion.html')

def setsessaion(request):
    # Create a Session Data 
    request.session['name']= 'jahid'
    return render(request, 'coreapp/setsessaion.html')

def getsessaion(request):
    # # Simple way get Session data 
    # name = request.session['name']
    
    # Default Session Guast Data Set 
    name = request.session.get('name', default='Guast')
    return render(request, 'coreapp/getsessaion.html',{'name':name})

def delsessaion(request):
    # if name = Session hoi  then remove this name data
    if 'name' in request.session :
        del request.session['name']
    return render(request, 'coreapp/delsessaion.html')
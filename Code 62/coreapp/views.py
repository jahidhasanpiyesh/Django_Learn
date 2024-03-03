from django.shortcuts import render

# Create your views here.
def homesessaion(request):
    return render(request, 'coreapp/sessaion.html')

def setsessaion(request):
    # Create a Session Data 
    request.session['name']= 'jahid'
    return render(request, 'coreapp/setsessaion.html')

def getsessaion(request):
    name = request.session.get('name')
    # key show this template just call keys()
    keys =request.session.keys()
    # value Show this template just call items()
    items = request.session.items()
     
    # # set a default value this templates show value and key just call setdefault()
    # defult = request.session.setdefault('age','20')
    
    return render(request, 'coreapp/getsessaion.html',{'name':name, 'keys': keys, 'items':items})

def delsessaion(request):
    # # This code run just comment defult code line number 20 and remove value pass key
    # request.session.flush()
    
    if 'name' in request.session :
        del request.session['name']
    return render(request, 'coreapp/delsessaion.html')
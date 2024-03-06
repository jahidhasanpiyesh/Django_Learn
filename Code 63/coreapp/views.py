from django.shortcuts import render

# Create your views here.
def homesessaion(request):
    return render(request, 'coreapp/sessaion.html')

def setsessaion(request):
    # Create a Session Data 
    request.session['name']= 'jahid'
    
    # session set any seconds time just try this code 
    # set_expiry(0) = True & set_expiry(600) = False
    request.session.set_expiry(0)
    return render(request, 'coreapp/setsessaion.html')

def getsessaion(request):
    name = request.session.get('name')
    
    # Session age show my output and print my terminal 
    print(request.session.get_session_cookie_age())
    
    # Session expiry date show 
    print(request.session.get_expiry_date())
    
    # age show
    print(request.session.get_expiry_age())
    
    # session data not none == false and none hoi then true 
    print(request.session.get_expire_at_browser_close())
    print(request.session.clear_expired())
    return render(request, 'coreapp/getsessaion.html',{'name':name})

def delsessaion(request):
    # # This code run just comment defult code line number 20 and remove value pass key
    # request.session.flush()
    
    if 'name' in request.session :
        del request.session['name']
    return render(request, 'coreapp/delsessaion.html')
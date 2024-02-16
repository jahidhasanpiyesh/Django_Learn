from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def homecookie(request):
    return render(request, 'coreapp/cookie.html')

def setcookie(request):
    reponse = render(request,'coreapp/setcookie.html')
    # # To set cookies in the browser, please Use set_cookie()
    # reponse.set_cookie('name','jahid') 
    
    # # Cookies will be automatically removed after 60 seconds just call  max_age=60/ any number but number of second.
    # reponse.set_cookie('name','jahid', max_age=60)
    
    # Cookies will be automatically removed after date or time fixed.
    # Cookies append just flow code and change "name/any text","jahid/any text"
    reponse.set_cookie('name','jahid', expires=datetime.utcnow() + timedelta(days=2))
    return reponse

def getcookie(request):
    # Browser cookies not set then face big errors . default Value not none set.
    # name = request.COOKIES['name']
    
    # Browser cookies not set then face not errors. default = none value set.
    # name = request.COOKIES.get('name')
    
    # default value set 'Guest'
    name = request.COOKIES.get('name','Guest')
    return render(request,'coreapp/getcookie.html',{'name':name})

def delcookie(request):
    reponse = render(request,'coreapp/delcookie.html')
    # If you want to Delete the cookies, just call delete_cookie()
    reponse.delete_cookie('name')
    return reponse
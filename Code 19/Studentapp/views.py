from django.shortcuts import render

# Create your views here.
def student(request):
    
    # # Multiple data use to dict and stor this {st} variable .
    st = {
        'st1':{'name':'Jahid','roll':472826},
        'st2':{'name':'saddam','roll':472772},
        'st3':{'name':'naeem','roll':472792},
        'st4':{'name':'mamun','roll':472795}
    } 
    
    # singla data using and try this problem fixing  
    # st = {'name':'jahid','roll':472826}
    
    return render(request, 'index.html',{'total':st}) 
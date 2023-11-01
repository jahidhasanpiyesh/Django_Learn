from django.shortcuts import render

# Create your views here.
def student(request):
    data = {'Name':['Jahid','Hasan','Piyesh','Rana']}
    return render(request, 'index.html', data)
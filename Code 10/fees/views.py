from django.shortcuts import render

# Create your views here.
def feesfirst(request):
    phone_number = 1710756233
    work = 'web Developer'
    location = 'Dhaka'
    salary = 15000
    total_info = {'ph':phone_number, 'wo':work,'lo':location,'sa':salary,}
    return render(request, 'fees/feesone.html', total_info)

def feessecond(request):
    name = 'Md Jahid Hasan'
    year = '19 year 2 mounth'
    address = 'Phulpur'
    salary = 30000
    student = True
    info = {"nm":name, "y":year, "a":address, "s":salary, "s":student}
    
    return render(request, 'fees/feestwo.html', info)
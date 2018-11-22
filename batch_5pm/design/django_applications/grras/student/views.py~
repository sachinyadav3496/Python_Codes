from django.shortcuts import render
from .models import Student,Address,Faculty,Course
from django.http import HttpResponse
def index(request):
    return render(request,'student/index.html')

def data(request,name=None):
    if name : 
        try : 
            student = Student.objects.get(name=name)
            data = { 'name':student.name,
                     'roll_no': student.roll_no,
                     'dob' : student.dob,
                     'ph_no' : student.ph_no,
                     'address' : student.address,
                     'email' : student.email,
                                                 }
            return render(request,'student/data.html',{'data':data })
        except Exception as e : 
            error = f"Error : {e} "
            return HttpResponse(error)
     
from django.shortcuts import render
from .models import Student,Address,Faculty,Course
from django.http import HttpResponse
from .forms import Login_Form

def index(request):
    form = Login_Form()
    return render(request,'student/index.html',{'form':form,})

def make_Login(request,method=['POST','GET']):
    return HttpResponse("You are at login page.")


















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






def contact(request):
    return render(request,'student/contact.html')

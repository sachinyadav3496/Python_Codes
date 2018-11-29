from django.shortcuts import render
from .models import Student,Address,Faculty,Course
from django.http import HttpResponse
from .forms import Login_Form,Signup_Form

def index(request):
    form = Login_Form()
    return render(request,'student/index.html',{'form':form,})

def make_Login(request):
    form = Login_Form(request.POST)
    if form.is_valid() :
        roll_no = form.cleaned_data['roll_no']
        password = form.cleaned_data['password']
        try :
            student = Student.objects.get(roll_no=roll_no,password=password)
            data = { 'NAME':student.name,
                          'PASSWORD': student.password,
                           'PHONE NUMBER' : student.ph_no,
                            'DATE OF BIRTH':student.dob,
                         }
            return render(request,'student/data.html',{'data':data})

        except Exception as error:
            form = Login_Form
            error = "Either Username or Password Invalid"
            return render(request,'student/index.html',{'form':form,'error':error})
    else :
        return HttpResponse("!!Error!!Form data is Incorrect")


def Signup(request):
    form = Signup_Form()
    return render(request,'student/signup.html',{'form':form})

def make_Signup(request):
    form = Signup_Form(request.POST)
    if form.is_valid():
        data = {
        'roll_no' : form.cleaned_data['roll_no'],
        'name' : form.cleaned_data['name'],
        'password' : form.cleaned_data['password'],
        'ph_no'  : form.cleaned_data['ph_no'],
        'dob' : form.cleaned_data['dob'],
         }
        user = Student(**data)
        user.save()
        form = Login_Form()
        return  render(request,'student/index.html',{'form':form,'error':'User Successfully Created Please Login'})

    else :
        form = Signup_Form()
        error = "Invalid Form Format"
        return render(request,'student/signup.html',{'form':form,'error':error})














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

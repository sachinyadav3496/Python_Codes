from django.shortcuts import render
from django.http import HttpResponse
from .forms import signup as sign
from .forms import login as logged
# Create your views here.

def home(request) :

    return render(request,'bank/home.html')

def signup(request):

    myform = sign()
    return render(request,'bank/signup.html',{'form':myform})

def mysignup(request):

    if request.method == 'POST' :

        myform = sign(request.POST)
        if myform.is_valid() :

            name = myform.cleaned_data['UName']
            fname = myform.cleaned_data['FName']
            lname = myform.cleaned_data['LName']
            password = myform.cleaned_data['Password']
            email = myform.cleaned_data['Email']
            dob = myform.cleaned_data['DOB']

            mydict = { 'Name':name,"First Name":fname,"Last Name":lname,\
                      "Password":password,"Email":email,"Date of Birth":dob }

            return render(request,'bank/signup1.html',{'data':mydict})

        else :
            myform = sign()
            err = "Error:Invalid Form Data or Fields"
            return render(request,'bank/signup.html',{'error':err,'form':myform})

    else :
        myform = sign()
        err = "Error:We only Deal with Post Methods"
        return render(request,'bank/signup.html',{'error':err,'form':myform})

def login(request):

    myform = logged()


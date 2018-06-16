__author__ = 'sachin yadav'

from django.http import HttpResponse
from django.shortcuts import render
from .forms import myData

def home(request):
    form = myData()
    return render(request,'index.html',{'form':form})

def myform(request):

    if request.method == 'POST' :

        form = myData(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            first_name = form.cleaned_data['FName']
            last_name = form.cleaned_data['LName']
            bal = form.cleaned_data['bal']
            id  = form.cleaned_data['id']
            email = form.cleaned_data['Email']
            dob = form.cleaned_data['DOB']
            data = {'Name':name,'Account Number':id,'First Name':first_name,'Last Name':last_name,\
                    'Balance':bal,'Email':email,'DOB':dob,}
            return render(request,'sucess.html',{'data':data})

        else :

            return HttpResponse("You are at myform view with Error")
    else :
        form = myData()
        return render(request,'index.html',{'form':form})

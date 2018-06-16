from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import login
from .models import mydata
# Create your views here.
def home(request):
    form = login()
    return render(request,'myapp1/home.html',{ 'form':form})

def mklogin(request):
    if request.method == 'POST' :
        form = login(request.POST)

        if form.is_valid() :
            n = form.cleaned_data['name']
            p = form.cleaned_data['password']
            e = form.cleaned_data['email']
            obj = mydata(name=n,password=p,email=e)
            obj.save()
            return render(request,'myapp1/sucess.html',{'name':n,'password':p,'email':e})

        else :
            form = login()
            error = "Error!!your form is not valid"
            return render(request,'myapp1/home.html',{'form':form,'error':error})
    else :
        form = login()
        error = "Error!!Not a Valid Form you should user Post method"
        return redirect('http://localhost',{'error':error,'form':form})
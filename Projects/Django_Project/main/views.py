
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import signup_form
from django.contrib.auth.models import User

def main(request):

    return render(request,'main/main.html')

def login(request):
    myerror = None
    context = {'error':myerror}
    return render(request,'main/login.html',context)

def signup(request):

    if request.method == 'POST':

        form = signup_form(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            name=str(name).strip()
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            try:
                user = User.objects.get(username=name)
                myerror = "User already Exist Please Login"
                context = { 'error':myerror}
                return render(request,'main/login.html',context )
            except:
                return render(request,'main/profile.html')


            #return HttpResponse("Name = %s<br />Email = %s<br />password = %s<br />"%(name,email,password))
        else:
            error = "Form data is invalid  Please try again "
            return render(request,'main/login.html',{error})

    else :
        return HttpResponse('bye')



def profile(request):

        return render(request,'main/profile.html')

def adduser(request):

    pass

__author__ = 'sachin yadav'

from django import forms

class login(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput())

class signup(forms.Form) :

    FName = forms.CharField(max_length=50)
    LName = forms.CharField(max_length=50)
    UName = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50,widget=forms.PasswordInput())
    DOB = forms.DateTimeField()
    Email = forms.EmailField()
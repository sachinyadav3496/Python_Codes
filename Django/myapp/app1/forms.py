__author__ = 'sachin yadav'

from django import forms

class login(forms.Form):

    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

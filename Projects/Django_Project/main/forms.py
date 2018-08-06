__author__ = 'sachin yadav'
from django import forms

class signup_form(forms.Form):

    name = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

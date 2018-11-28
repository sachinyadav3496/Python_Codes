from django import forms

class Login_Form(forms.Form) :
    roll_no = forms.IntegerField(label='Roll Number',label_suffix=' : ',required=True,\
        error_messages={'REQUIRED':"Please Enter Valid Roll Number"})
    password = forms.CharField(label='Password ',label_suffix=' : ',\
       widget=forms.PasswordInput(),required=True,\
       error_messages={"REQUIRED":"Please Enter Password"})


class Signup_Form(forms.Form) :
    roll_no = forms.IntegerField(label='Roll Number',label_suffix=' :',required=True)
    name = forms.CharField(max_length=50,required=True,label_suffix=' :',label='NAME')
    dob = forms.DateField(widget=forms.DateInput,required=True,label_suffix=' : ',\
                          label='DOB ')
    ph_no = forms.CharField(max_length=15,required=True,label_suffix=' : ',label='PH NO')
    email = forms.EmailField(widget=forms.EmailInput,label='Email',label_suffix=':')
    password = forms.CharField(widget=forms.PasswordInput(),label='Password',label_suffix=' : ',required=True)

from django import forms

class Login_Form(forms.Form) :
    roll_no = forms.IntegerField(label='Roll Number',label_suffix=' : ',required=True,\
        error_messages={'REQUIRED':"Please Enter Valid Roll Number"})
    password = forms.CharField(label='Password ',label_suffix=' : ',\
       widget=forms.PasswordInput,required=True,\
       error_messages={"REQUIRED":"Please Enter Password"})


class signup(forms.Form) :
    pass

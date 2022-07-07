from django.db import models
from django import forms
from user.models import Register
from user.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','last_login']

        widgets = {
            'username': forms.TextInput(attrs={"placeholder":"Enter Username"}),
            'first_name':forms.TextInput(attrs={"placeholder":"Enter Your First Name"}),
            'last_name':forms.TextInput(attrs={"placeholder":"Enter Your Last Name"}),
            'email':forms.EmailInput(attrs={"placeholder":"Enter Your Email address"}),
            'password':forms.PasswordInput(attrs={"placeholder":"Enter Password"}),
            
            }


class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={"placeholder":"Enter Your Username"}),
            'password':forms.PasswordInput(attrs={"placeholder":"Enter Your Password"})
        }
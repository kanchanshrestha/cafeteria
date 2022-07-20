from django.db import models
from django import forms
from cafecustomer.models import Customer
from cafecustomer.models import Login
from user.models import User
GENDER=[
    ('M','Male'),
    ('F','Female'),
    ('O','others'),
]



class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['username','name','profile_picture','mobile_number','email','city','country','dob','gender','occupation']
    
        widgets = {
            'name':forms.TextInput(attrs={"placeholder":"Enter Your Full Name"}),
            'mobile_number':forms.TextInput(attrs={"placeholder":"Enter Your Mobile Number"}),
            'email':forms.EmailInput(attrs={"placeholder":"Enter Your Email address"}),
            'city':forms.TextInput(attrs={"placeholder":"Enter your City"}),
            'country':forms.TextInput(attrs={"placeholder":"Enter Your Country"}),
            'dob':forms.DateInput(attrs={"type":"date"}),
            'gender':forms.RadioSelect(choices=GENDER),
            'occupation':forms.TextInput(attrs={"placeholder":"Enter Your Occupation"}),
            }
        


class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={"placeholder":"Enter Your Username"}),
            'password':forms.PasswordInput(attrs={"placeholder":"Enter Your Password"})
        }

class AddBalance(forms.ModelForm):
	class Meta:
		model = User
		fields = ['balance']

class UpdateRegister(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','profile_picture','mobile_number','email','city','country','dob','gender','occupation']

        widgets = {
            'name':forms.TextInput(attrs={"placeholder":"Enter Your Full Name"}),
            'mobile_number':forms.TextInput(attrs={"placeholder":"Enter Your Mobile Number"}),
            'email':forms.EmailInput(attrs={"placeholder":"Enter Your Email address"}),
            'city':forms.TextInput(attrs={"placeholder":"Enter your City"}),
            'country':forms.TextInput(attrs={"placeholder":"Enter Your Country"}),
            'dob':forms.DateInput(attrs={"type":"date"}),
            'gender':forms.RadioSelect(choices=GENDER),
            'occupation':forms.TextInput(attrs={"placeholder":"Enter Your Occupation"}),
            }
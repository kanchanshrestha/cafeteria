from django.db import models
from django import forms
from cafecustomer.models import Customer
from cafecustomer.models import Login
from user.models import User
from django.forms import ValidationError
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
            "password":forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
            # 'password':forms.PasswordInput(attrs={"placeholder":"Enter Your Password"})
        }

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if not username:
    #             raise forms.ValidationError('This Field is Required')
    #     user=User.objects.filter(username=username).exists()
    #     if not user:
    #         raise ValidationError('\n Couldnot find Your Account')
    #     return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('This Field is Required')
        user=User.objects.filter(password=password).exists()
        if not user:
            raise ValidationError('\n Invalid credentials ')
        return password
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
from django.db import models
from django import forms
from user.models import User
from user.models import Transaction

GENDER=[
    ('M','Male'),
    ('F','Female'),
    ('O','others'),
]

TYPE=[
    ('expense','Expense'),
    ('income','Income'),
    

]
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','name', 'profile_picture','password' ,'mobile_number','email','city','country','dob','gender','occupation']
    
        widgets = {
            'username':forms.TextInput(attrs={"placeholder":"Enter a Username"}),
            'name':forms.TextInput(attrs={"placeholder":"Enter Your Full Name"}),
            'password':forms.PasswordInput(attrs={"placeholder":"Enter Password"}),
            'mobile_number':forms.TextInput(attrs={"placeholder":"Enter Your Mobile Number"}),
            'email':forms.EmailInput(attrs={"placeholder":"Enter Your Email address"}),
            'city':forms.TextInput(attrs={"placeholder":"Enter your City"}),
            'country':forms.TextInput(attrs={"placeholder":"Enter Your Country"}),
            'dob':forms.DateInput(attrs={"type":"date"}),
            'gender':forms.RadioSelect(choices=GENDER),
            'occupation':forms.TextInput(attrs={"placeholder":"Enter Your Occupation"}),
            }

class UpdateForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['name', 'mobile_number','email','city','country','dob','gender','occupation']
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
class TransactionForm(forms.ModelForm):
    user=forms.CharField(required=False,empty_value=None)
    class Meta:
        model=Transaction
        fields=['user','description','date','time','amount','transaction_type']

        widgets = {
            'date':forms.DateInput(attrs={"type":"date"}),
            'time':forms.TimeInput(attrs={"type":"time"}),
            'transaction_type':forms.Select(choices=TYPE)
         }




         
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if not username:
    #         raise forms.ValidationError('This Field is Required')
    #     for instance in Customer.objects.all():
    #         if instance.username==username:
    #             raise forms.ValidateError(username +'is already created')
    #         return username


    

	    # if not category:
		# raise forms.ValidationError('This field is required')
		    

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=Login
#         fields='__all__'
#         widgets={
#             'username':forms.TextInput(attrs={"placeholder":"Enter Your Username"}),
#             'password':forms.PasswordInput(attrs={"placeholder":"Enter Your Password"})
#         }

    
    # password = forms.CharField(widget = forms.PasswordInput, validators = [check_size, ])
    # password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
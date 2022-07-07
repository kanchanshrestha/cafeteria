from django.shortcuts import redirect, render
from django. http import HttpRequest, HttpResponse,HttpResponseRedirect
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import logout

def registerform(request):
    forms=RegisterForm()
    if request.method=='POST':
        forms=RegisterForm(request.POST)

        if forms.is_valid():
            user=forms.save(commit=False)
            user.set_password(forms.cleaned_data['password'])
            user.is_customer=1
            user.save()
            return redirect('/admin/')
            
        else:
            return HttpResponse(forms.errors)

    context={
        "forms":forms
    }
  
    return render (request,'userregister/userregister.html',context)


def loginform(request):
    forms=LoginForm()
    if request.method=='POST':
        forms=LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return render (request,'userlogin/userlogout.html')            
        else:
            return HttpResponse("Invalid Credentials")
            
    context={
        "forms":forms
    }
  
    return render (request,'userlogin/userlogin.html',context)

def logoutuser(request):
        logout(request)
        return redirect('/user/login/')





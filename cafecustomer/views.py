from django.shortcuts import render,redirect
from cafecustomer.models import Customer
from user.models import Transaction
from user.models import User
from user.forms import UserForm
from .forms import UpdateRegister
from .forms import LoginForm
from django. http import HttpResponse
from django.contrib.auth import  authenticate , login,logout
from .forms import AddBalance 
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required

@transaction.atomic
def registration(request):
    forms=UserForm()
    if request.method=='POST':
        forms=UserForm(request.POST)
        if forms.is_valid():       
            user=forms.save(commit=False)
            user.set_password(forms.cleaned_data['password'])
            user.is_customer=1
            user.balance=0
            user.save()
            Customer.objects.create(username=user, name=request.POST["name"] ,mobile_number=request.POST["mobile_number"])
            messages.success(request,'Registration Sucessful now Login')
            # Customer.objects.create(username=request.POST["username"], name=request.POST["name"] , mobile_number=request.POST["mobile_number"])
            return redirect('/customer/login')
            
        else:
            return HttpResponse(forms.errors)
    context={
        "forms":forms
    }
  
    return render (request,'customerlogin/customerregister.html',context)
# Create your views here.

@login_required(login_url='/customer/login')
def updateregisterform(request,id):
    customer=User.objects.get(id=id)
    forms=UpdateRegister(instance=customer)
    if request.method=='POST':
        forms=UpdateRegister(request.POST , request.FILES,instance=customer)
        if forms.is_valid():            
            forms.save()
            messages.success(request,'Registration Sucessful')
            return redirect('/customer/dashboard/')
            
        else:
            return HttpResponse(forms.errors)
     
    context={
        "forms":forms
    }
  
    return render (request,'customerlogin/updateregister.html',context)


# def loginform(request):
#     forms=LoginForm()
#     if request.method=='POST':
#         forms=LoginForm(request.POST)
#         username=request.POST['username']
#         password=request.POST['password']
#         user = authenticate(username=username, password=password)
#         login(request,user)
#         if user is not None:
#             messages.success(request,"Login Sucessful") 
#             return redirect('/customer/dashboard')
#             # return render(request,'dashboard/dashboard.html', {"user":user})            
#         else:
#             return render(request, 'customerlogin/customerlogin.html')
            
            
#     context={
#         "forms":forms
#     }
  
#     return render (request,'customerlogin/customerlogin.html',context)
def loginform(request):
    forms=LoginForm()
    if request.method=='POST':
        forms=LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        login(request,user)
        if request.user.is_superuser==1:
            return redirect('/user/admindashboard') 
        if user is not None:
            messages.success(request,"Login Sucessful") 
            return redirect('/customer/dashboard')
            # return render(request,'dashboard/dashboard.html', {"user":user})            
        else:
            return render(request, 'customerlogin/customerlogin.html')
            
            
    context={
        "forms":forms
    }
  
    return render (request,'customerlogin/customerlogin.html',context)



@login_required(login_url='/customer/login')
def dashboard(request):
        transactions=Transaction.objects.filter(user_id=request.user.id)
        user=User.objects.get(id=request.user.id)
        context={
            "user":user,
            'transaction':transactions
        }
        # logout(request) no logout 
        return render(request,'dashboard/dashboard.html',context)
       


def viewtransactionlist(request):
    transactions=Transaction.objects.all
    # totalnumber=transactions.count()
    # print("total",totalnumber)
    transactionlist={
        'list':transactions
        
    }
    return render(request,'customerlogin/transaction_list.html',transactionlist)
# 

# @login_required(login_url='/customer/login')
# def viewtransactionlist(request):
#     transactions=Transaction.objects.filter(user_id=request.user.id)
#     transactionlist={
#         'list':transactions,
#     }
#     return render(request,'customerlogin/transaction_list.html',transactionlist)


@login_required(login_url='/customer/login')
def addbalance(request, id):
    print(request)
    forms = AddBalance(request.POST)
    if request.method=="POST":
        user=User.objects.get(id=id)
        user=User.objects.filter(id=id).update(balance= user.balance + int(request.POST['balance']))
        messages.success(request,"Balance Added Sucessfully To Your Account") 
        return redirect('/customer/dashboard/')

    else:
        forms=AddBalance()
    add={
         "forms":forms
    }
    return render(request,'customerlogin/add_balance.html',add)

def user_logout(request):
    logout(request)
    messages.success(request,'Logout Sucessful')
    return redirect('/customer/login')




















	
	
	

	

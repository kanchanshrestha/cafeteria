from urllib import request
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
from .decorators import customer_only
from .decorators import admin_only
from datetime import date,datetime

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
            

    context={
        "forms":forms
    }
  
    return render (request,'customerlogin/customerregister.html',context)
# Create your views here.

# username = self.cleaned_data.get('username')
#   
        # 
#       try: 
        #   for instance in Customer.objects.all():
        #     if instance.username==username:
        #         raise forms.ValidateError(username +'is already created')
#  except:  
 #         return Exception(username +'is already created') 



@login_required(login_url='/customer/login')
# @customer_only
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
#             if user.is_superuser==1:
#                 messages.success(request,"Login Sucessful") 
#                 return redirect('/user/admindashboard')
#             # return render(request,'dashboard/dashboard.html', {"user":user})            
#             elif user.is_customer==1:
#                 messages.success(request,"Login Sucessful") 
#                 return redirect('/customer/dashboard')
#         else:
#             messages.error(request,'username or password not correct')
#             return redirect('login')
            
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
        if user is not None:
            login(request,user)
            if user.is_superuser==1:
                messages.success(request,"Login Sucessful") 
                return redirect('/user/admindashboard')
            # return render(request,'dashboard/dashboard.html', {"user":user})            
            elif user.is_customer==1:
                messages.success(request,"Login Sucessful") 
                return redirect('/customer/dashboard')
   
            
    context={
        "forms":forms
    }
  
    return render (request,'customerlogin/customerlogin.html',context)


#   elif:
#   if username is None:
#       return HttpResponse("Couldn't find your Account")
#   else:
#       return HttpResponse("Invalid Password")


@login_required(login_url='/customer/login')
# @customer_only
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

@transaction.atomic
@login_required(login_url='/customer/login')
# @customer_only
def addbalance(request, id):
    print(request)
    forms = AddBalance(request.POST)
    if request.method=="POST":
        user=User.objects.get(id=id)
        today=datetime.now()
        user=User.objects.filter(id=id).update(balance= user.balance + int(request.POST['balance']))
        Transaction.objects.create(user_id=request.user.id,description="Top Up",date=today,time=today,amount=request.POST["balance"],transaction_type="Top Up")
        messages.success(request,"Balance Added Sucessfully To Your Account") 
        return redirect('/customer/dashboard/')

    else:
        forms=AddBalance()
    add={
         "forms":forms
    }
    return render(request,'customerlogin/add_balance.html',add)

# from datetime import date,datetime

# today = datetime.now()
# print("Today's date:", today)
# print(today.strftime("%Y:%m:%D")
# print(today.strftime("%H:%M:%S")
# )
# @customer_only
def user_logout(request):
    messages.success(request,'Logout Sucessful')
    logout(request)
    
    return redirect('/customer/login')


def edit_picture(request):
    pass




















	
	
	

	

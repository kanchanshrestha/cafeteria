from django.shortcuts import render,redirect
from cafecustomer.models import Customer
from user.models import User
from .forms import UpdateForm
from user.models import Transaction
from .forms import TransactionForm
from django. http import HttpResponse
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/customer/login')
def admin(request):
    user=User.objects.all().exclude(is_superuser=1)
    totalnumber=user.count()
    print("total",totalnumber)
    
    customerlist={
        'list':user,
        "total":totalnumber
    }
    return render(request,'admindash/admindashboard.html',customerlist)


@login_required(login_url='/customer/login')
def updatecustomer(request,id): 
    customer=User.objects.get(id=id)
    forms=UpdateForm(instance=customer)
    if request.method=='POST':
        forms=UpdateForm(request.POST,instance=customer)
        if forms.is_valid():
            forms.save()
            messages.success(request,'Updated Sucessfully')
            return redirect ("/user/admindashboard/")
        else:
            return HttpResponse(forms.errors)
    cupdate={
         "forms":forms
    }
    return render(request,'userregister/userregister.html',cupdate)

@login_required(login_url='/customer/login')
def deletecustomer(request,id):
    user=User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request,'Deleted Sucessfully')
        return redirect('/user/admindashboard/')
        
    return render(request, 'admindash/delete_customer.html')





    # User.objects.get(id=id)
    # return redirect("/user/admindashboard/")

# @transaction.atomic
# def addtransaction(request,id):
#     user=User.objects.get(id=id)
#     forms=TransactionForm()
#     if request.method=="POST":
#         forms=TransactionForm(request.POST)
#         if forms.is_valid():
#             transacation=forms.save(commit=False)
#             transacation.user=user
#             forms.save()
#             messages.success(request,'Transaction Added Sucessfully')
#             return redirect('/user/admindashboard') 
#         else:
#             messages.error(request,forms.errors)
#             print(forms.errors)
        
#     context={
#         "forms":forms
#     }
  
#     return render(request,'transaction/add_txn.html',context)


@login_required(login_url='/customer/login')
def addtransaction(request,id):
    user=User.objects.get(id=id)
    Transaction.objects.get(id=id)
    forms=TransactionForm()
    if request.method=="POST":
        forms=TransactionForm(request.POST)
        if forms.is_valid():
            print(request)
            transacation=forms.save(commit=False)
            transacation.user=user
            if request.POST['transaction_type']=="income":
                user=User.objects.filter(id=id).update(balance= user.balance+ int(request.POST['amount']))
                pass

            else:
                user=User.objects.filter(id=id).update(balance= user.balance - int(request.POST['amount'])) 
            forms.save()
            messages.success(request,'Transaction Added Sucessfully')
            return redirect('/user/admindashboard') 
        else:
            messages.error(request,forms.errors)
            print(forms.errors)
        
    context={
        "forms":forms
    }
  
    return render(request,'transaction/add_txn.html',context)

# if user.transaction_type=='income':
#                 user=User.objects.filter(id=id).update(balance= user.balance + int(request.POST['balance']))

#             else:
#                 user=User.objects.filter(id=id).update(balance= user.balance - int(request.POST['balance'])) 

def customer_transactionlist(request):
    transactions=Transaction.objects.all()
    totalnumber=transactions.count()
    print("total",totalnumber)
    transactionlist={
        'list':transactions,
         "total":totalnumber
    }

    return render(request,'transaction/transaction.html',transactionlist)



def customerlist(request):
   customers=Customer.objects.all()
   customerlist={
        'list':customers,
    
    }
   return render(request,'customerlist/customer_list.html',customerlist)


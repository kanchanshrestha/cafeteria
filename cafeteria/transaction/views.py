from django.shortcuts import render
from transaction.models import Transaction
# Create your views here.
def transactionlist(request):
   transactions=Transaction.objects.all()
   return render(request,'transactiontemp/transaction_list.html')
from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
     path('admindashboard/',views.admin,name="admindashboard"),
     path('updatecustomer/<int:id>',views.updatecustomer,name="update"),
     path('deletecustomer/<int:id>',views.deletecustomer,name="delete"),
     path('addtransaction/<int:id>',views.addtransaction,name="addtransaction"),
     path('customer_transactions/',views.customer_transactionlist,name="customer_txn_list"),
     # path('transaction/<int:id>',views.transaction,name="transaction"),
    
]

         
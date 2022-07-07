from django.contrib import admin
from django.urls import path
from transaction import views
urlpatterns = [
     path('transactiondetails/',views.transactionlist,name="transaction"),
]
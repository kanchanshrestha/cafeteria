from django.contrib import admin
from django.urls import path
from customer import views
urlpatterns = [
     path('customerdetails/',views.customerlist,name="customerdetails"),
]

    
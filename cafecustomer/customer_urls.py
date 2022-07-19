from django.contrib import admin
from django.urls import path
from cafecustomer import views
urlpatterns = [
     path('login/', views.loginform,name="login"),
     path('completeregister/<int:id>',views.updateregisterform,name="register"),
     path('dashboard/',views.dashboard,name="dashboard"),
     path('registration/',views.registration,name="registration"),
     path('viewtransactions/',views.viewtransactionlist,name="viewtransactions"),
     path('addbalance/<int:id>',views.addbalance,name="addbalance"),
     path('logout/',views.user_logout,name="logout"),


]

         

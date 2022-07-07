from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('login/', views.loginform,name="login"),
     path('register/',views.registerform,name="register"),
     path('logout/',views.logoutuser,name="logout")
     
]
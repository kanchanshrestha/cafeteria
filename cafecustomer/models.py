from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from datetime import datetime, date
from user.models import User
# Create your models here.

class Customer(models.Model):
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=120,null=False,blank=False)
    password=models.CharField(max_length=25,null=False,blank=False)
    profile_picture=models.ImageField(null=True,blank=True)
    mobile_number=models.CharField(max_length=12,null=False,blank=False)
    email=models.EmailField(null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=40,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    occupation=models.CharField(max_length=30,null=True,blank=True)
    

    class Meta:
        db_table="Customer"

class Login(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=25)



from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_customer=models.BooleanField(default=False)
    name=models.CharField(max_length=120,null=True,blank=True)
    profile_picture=models.ImageField(null=True,blank=True)
    mobile_number=models.CharField(max_length=12,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=40,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    occupation=models.CharField(max_length=30,null=True,blank=True)
    balance=models.IntegerField(null=True,blank=True)
    # add_balance=models.IntegerField(null=True,blank=True)
    class Meta:
        db_table="User"


class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True, blank=True)
    time=models.TimeField(null=True, blank=True)
    amount=models.IntegerField(null=False,blank=False)
    status=models.CharField(max_length=20,null=True,blank=True)
    transaction_type=models.CharField(max_length=20,null=True,blank=True)
    
    class Meta:
        db_table="Transaction"
    













 # password=models.CharField(max_length=25,null=False,blank=False)
    # profile_picture=models.ImageField(upload_to = "\images",null=True,blank=True)
    # # country_code=models.IntegerField(null=True,blank=True)
        # email=models.EmailField(null=True,blank=True)
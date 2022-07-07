from django.db import models
from user.models import User
# Create your models here.

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to = "\images",null=True,blank=True)
    name=models.CharField(max_length=120,null=True,blank=True)
    mobile_number=models.CharField(max_length=12,null=True,blank=True)
    email=models.EmailField(unique=True,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    # is_active=models.ForeignKey(User,on_delete=models.CASCADE)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    occupation=models.CharField(max_length=30)
    balance=models.IntegerField(null=True,blank=True)

    class Meta:
        db_table="Customer"
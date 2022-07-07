from django.db import models
from user.models import User
# Create your models here.
class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(auto_now_add=True, blank=True)
    time=models.TimeField(auto_now_add=True, blank=True)
    amount=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=20,null=True,blank=True)
    
    class Meta:
        db_table="Transaction"
    
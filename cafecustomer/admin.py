from django.contrib import admin

# Register your models here.
from cafecustomer.models import Customer

@admin.register(Customer)
class Customer(admin.ModelAdmin):
    pass
    list_display = ("username","name","password","profile_picture","mobile_number","email","occupation")
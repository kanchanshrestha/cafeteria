from django.contrib import admin
from customer.models import Customer

@admin.register(Customer)
class Customer(admin.ModelAdmin):
    pass
    list_display = ("user", "profile_picture", "name","mobile_number","email","occupation","balance")


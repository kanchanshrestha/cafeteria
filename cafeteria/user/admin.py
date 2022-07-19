from django.contrib import admin
from user.models import User
from user.models import Transaction
# Register your models here.
admin.site.register(User)
@admin.register(Transaction)
class Customer(admin.ModelAdmin):
    list_display = ("user_id","description","date","time","amount","transaction_type")
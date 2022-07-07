from django.contrib import admin
from transaction.models import Transaction

@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    pass
    list_display =("user", "description", "date", "time", "amount", "status")
from django.db import models
from django import forms
from transaction.models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=['__all__']

    
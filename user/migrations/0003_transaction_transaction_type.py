# Generated by Django 4.0.6 on 2022-07-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_transaction_date_alter_transaction_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

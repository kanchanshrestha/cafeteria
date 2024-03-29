# Generated by Django 4.0.6 on 2022-07-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]

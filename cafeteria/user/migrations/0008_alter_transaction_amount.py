# Generated by Django 4.0.6 on 2022-07-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_transaction_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
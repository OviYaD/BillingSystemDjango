# Generated by Django 4.0.4 on 2022-06-01 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0005_bill_cartproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='bid',
            new_name='id',
        ),
    ]

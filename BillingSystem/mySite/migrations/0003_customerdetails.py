# Generated by Django 4.0.4 on 2022-06-01 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerDetails',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]

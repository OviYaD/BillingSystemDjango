# Generated by Django 4.0.4 on 2022-05-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]

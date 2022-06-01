from django.db import models

# Create your models here.
class signin(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

def __unicode__(self):
    return self.name

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __unicode__(self):
        return self.name
class customerDetail(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Bill(models.Model):
    id=models.AutoField(primary_key=True)
    total=models.FloatField()
    customer=models.ForeignKey(customerDetail,on_delete=models.CASCADE)

class CartItem(models.Model):
    bill=models.ForeignKey(Bill,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()


from django.contrib import admin

# Register your models here.
from mySite.models import signin, Product,customerDetail,Bill,CartItem

admin.site.register(signin)
admin.site.register(Product)
admin.site.register(customerDetail)
admin.site.register(Bill)
admin.site.register(CartItem)

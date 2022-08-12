from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']
# admin.site.register(Customer,CustomerModelAdmin)
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','quantity','order_date','status']



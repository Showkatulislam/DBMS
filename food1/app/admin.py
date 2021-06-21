from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced
# Register your models here.
@admin.register(Customer)
class CutomerModeladmin(admin.ModelAdmin):
    list_display=['user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModeladmin(admin.ModelAdmin):
    list_display=['title','selling_price','discounted_price',
    'description','category','product_image']

@admin.register(Cart)
class CartModeladmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModeladmin(admin.ModelAdmin):
    list_display=['user','customer','prodect','quantity','ordered_date','status']

from django.contrib import admin
from .models import Product, Cart

# Register your models here.

#admin.site.register(Product)
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title', 'discounted_price', 'category', 'image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user', 'product' , 'quantity'] 
from django.contrib import admin

# Register your models here.
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display=['id','category','name','desc','price','image','trending','offer']

admin.site.register(Products, ProductsAdmin)

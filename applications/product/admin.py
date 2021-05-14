from django.contrib import admin
from applications.product.models import Product, Category

admin.site.register(Category)
admin.site.register(Product)

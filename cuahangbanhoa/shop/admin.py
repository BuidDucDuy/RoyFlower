from django.contrib import admin
from .models import Product , Cart , Cart_item
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart_item)
admin.site.register(Cart)


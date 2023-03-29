from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product),
admin.site.register(Product_images),
admin.site.register(Products_size),
admin.site.register(Cart),
admin.site.register(Customer),
admin.site.register(Wishlist),
admin.site.register(Address),
admin.site.register(Checkout)




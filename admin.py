from django.contrib import admin
from .models import Product, CartItem
 
admin.site.register(Product)
admin.site.register(CartItem)

#Now, Go to the http://127.0.0.1:8000/admin/ and add the Images, name and its description.
#First we need to figure out how to log into the admin login prompt
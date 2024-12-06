from django.contrib import admin
from .models import Product, ContactMessage, Cart, CartItem, SignInLog
# Register your models here.
admin.site.register(Product)
admin.site.register(ContactMessage)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(SignInLog)
from django.contrib import admin
from instadash.models import User, Cart, OrderHistory, Business, Item, ItemCart

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(OrderHistory)
admin.site.register(Business)
admin.site.register(Item)
admin.site.register(ItemCart)

from django.contrib import admin
from .models import Customer, Product, Order, Tag
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_created')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date_created')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'date_created')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)

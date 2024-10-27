from django.contrib import admin
from .models import Order, Menu


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = [
        'user',
        'menu',
        'breakfast',
        'lunch',
        'dinner',
        'dessert',
        'persons',
        'datestart',
    ]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('foodtype',)
    list_display = ('foodtype', 'price')

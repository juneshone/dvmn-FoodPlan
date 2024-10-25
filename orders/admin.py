from django.contrib import admin
from .models import Order, Menu



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'persons',
        'breakfast',
        'lunch',
        'dinner',
        'dessert',
        'price',
        'datestart',
        'dateend'
    ]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)

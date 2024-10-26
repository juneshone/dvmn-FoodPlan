from django.contrib import admin
from .models import Order, Menu



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'menu',
    ]




@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('foodtype',)
    list_display = ('foodtype',)





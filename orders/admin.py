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
        'payment_status',
        'get_allergies'
    ]
    readonly_fields = ['allergy']
    def get_allergies(self, obj):
        all_allergies = [
            'Рыба и морепродукты',
            'Мясо',
            'Зерновые',
            'Продукты пчеловодства',
            'Орехи и бобовые',
            'Молочные продукты',
        ]
        allergies = ''
        for allergy in all_allergies:
            if allergy in obj.allergy:
                allergies = allergies + allergy + ' '
        return allergies



@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('foodtype',)
    list_display = ('foodtype', 'price')

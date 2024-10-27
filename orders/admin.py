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
        'get_allergy'
    ]

    def get_allergy(self, obj):
        all_allergy_list = [
            'Рыба и морепродукты',
            'Мясо',
            'Зерновые',
            'Продукты пчеловодства',
            'Орехи и бобовые',
            'Молочные продукты',
        ]

        all_allergy = obj.allergy
        allergies = ''
        for allergy in all_allergy_list:
            if allergy in all_allergy:
                allergies = allergies + allergy + ' '

        return  allergies



@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('foodtype',)
    list_display = ('foodtype', 'price')

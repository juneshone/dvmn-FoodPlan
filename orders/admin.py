from django.contrib import admin
from django.utils.html import format_html

from .models import Order, Menu

MAX_IMAGE_WIDTH = 300
MAX_IMAGE_HEIGHT = 200


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
        'get_allergy',
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

        return allergies


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('foodtype',)
    list_display = ('foodtype', 'price')
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: {}px; max-height={}px" />',
                obj.image.url,
                MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT
            )

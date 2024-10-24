from django.contrib import admin
from .models import Order, Allergy


class AllergyInline(admin.TabularInline):
    model = Allergy
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields =[
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

    inlines = [
        AllergyInline
    ]
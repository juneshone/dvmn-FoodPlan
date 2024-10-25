from django.contrib import admin
from .models import Order


# class OrderAllergyInline(admin.TabularInline):
#     model = OrderAllergy
#     extra = 0

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
        'period',
        'allergy1',
        'allergy2',
        'allergy3',
        'allergy4',
        'allergy5',
        'allergy6'
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
        'period',
        'allergy1',
        'allergy2',
        'allergy3',
        'allergy4',
        'allergy5',
        'allergy6'
    ]

    # inlines = [
    #     OrderAllergyInline
    # ]
from django import forms
from .models import Order, Menu


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['datestart']
        fields = ['id', 'menu', 'datestart', 'period', 'user', 'persons', 'breakfast',
                  'lunch', 'dinner', 'dessert', 'promocode', 'allergy1', 'allergy1', 'allergy2',
                  'allergy3', 'allergy4', 'allergy5', 'allergy6']

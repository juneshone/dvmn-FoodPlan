from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    foodtype = forms.DecimalField(
        required=True,
        decimal_places=0,
    )
    allergy1 = forms.CharField(
        required=False,
        max_length=50,
    )
    allergy2 = forms.CharField(
        required=False,
        max_length=50,
    )
    allergy3 = forms.CharField(
        required=False,
        max_length=50,
    )

    class Meta:
        model = Order
        fields = (
            'breakfast',
            'lunch',
            'dinner',
            'dessert',
            'persons',
            'subscription_period',
        )


class PaymentForm(forms.Form):
    card_number = forms.CharField(
        required=True,
        max_length=19,
    )
    validity_period = forms.CharField(
        required=True,
        max_length=7,
    )
    card_code = forms.CharField(
        required=True,
        max_length=3,
    )

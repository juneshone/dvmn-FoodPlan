from django import forms


class OrderCreateForm(forms.Form):
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
    breakfast = forms.CharField(
        required=False,
        max_length=50,
    )
    lunch = forms.CharField(
        required=False,
        max_length=50,
    )
    dinner = forms.CharField(
        required=False,
        max_length=50,
    )
    dessert = forms.CharField(
        required=False,
        max_length=50,
    )
    persons = forms.CharField(
        required=False,
        max_length=50,
    )
    subscription_period = forms.CharField(
        required=False,
        max_length=50,
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


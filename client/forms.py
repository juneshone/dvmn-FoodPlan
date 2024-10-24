from django import forms

from .models import User


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        max_length=25,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    last_name = forms.CharField(
        required=True,
        max_length=25,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    username = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password',)


from django import forms

from .models import User


class SignUpForm(forms.Form):
    """ Форма регистрации пользователя """

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
    password_confirmation = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )


class LoginForm(forms.Form):
    """ Форма аутентификации пользователя """

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
    """ Форма обновления данных пользователя """

    password = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)


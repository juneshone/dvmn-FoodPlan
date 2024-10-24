from django import forms

from .models import User


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        label='Имя',
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    last_name = forms.CharField(
        max_length=50,
        label='Фамилия',
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    username = forms.CharField(
        max_length=50,
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    password = forms.CharField(
        max_length=50,
        label='Пароль',
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )
    password = forms.CharField(
        max_length=50,
        label='Пароль',
        widget=forms.TextInput(
            attrs={'class': 'custom-input'}
        )
    )


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password',)


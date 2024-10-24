from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import *


def signup(request):
    """ Регистрация пользователя """

    print(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(
                username=username,
                password=password,
                last_name=last_name,
                first_name=first_name
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/client/account/')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    """ Аутентификация пользователя по существующему паролю """

    print(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user is None:
                raise 'Аутентификация пользователя не удалась'
            return redirect('/client/account/')
    else:
        form = LoginForm()
    return render(request, 'auth.html', {'form': form})


class AccountView(LoginRequiredMixin, TemplateView):
    """ Представление личного кабинета пользователя """

    template_name = 'lk.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = get_object_or_404(User, username=user.username)
        return context

from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import *


class SignUp(TemplateView):
    """ Регистрация пользователя """

    def get(self, request):
        return render(request, 'registration.html', {})

    def post(self, request):
        # TODO: обработать ошибку уникального пользователя и символы /&?
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
            print(form.errors)
        content = {'form': form}
        return render(request, 'registration.html', content)


class UserLogin(TemplateView):
    """ Аутентификация пользователя по существующему паролю """

    def get(self, request):
        return render(request, 'auth.html', {})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            user = authenticate(username=username, password=password)
            # TODO: написать условие для подтверждения пароля
            if user is None:
                # TODO: вывести пользователю информацию об ошибке ввода идентификационных данных
                # 'Аутентификация пользователя не удалась'
                # 'Пожалуйста, введите корректные логин и пароля. Оба поля могут быть чувствительны к регистру.'
                # 'Если у вас еще нет акккаунта, то зарегистрируйтесь'
                return redirect('/client/auth/')
            login(request, user)
            return redirect('/client/account/')
        else:
            print(form.errors)
        content = {'form': form}
        return render(request, 'auth.html', content)


class AccountView(LoginRequiredMixin, TemplateView):
    """ Представление личного кабинета пользователя """

    template_name = 'lk.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = get_object_or_404(User, username=user.username)
        return context

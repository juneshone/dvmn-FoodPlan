from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe

from .forms import *


class SignUp(TemplateView):
    """ Регистрация пользователя """

    def get(self, request):
        return render(request, 'registration.html', {})

    def post(self, request):
        # TODO: установить ограничение на ввод символов /& и тп.?
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_confirmation = form.cleaned_data.get('password_confirmation')
            if password != password_confirmation:
                message_text = 'Подтверждение пароля не совпадает с самим паролем'
                messages.success(request, message_text)
                return redirect('/client/registration/')
            try:
                User.objects.get(username=username)
                message_text = 'Пользователь с таким email уже существует'
                messages.success(request, message_text)
                return redirect('/client/registration/')
            except User.DoesNotExist:
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
            if user is None:
                message_text = (f'''
                    Пожалуйста, введите корректные логин и пароль.</br>
                    Оба поля могут быть чувствительны к регистру.</br>
                    Если у вас еще нет акккаунта, то зарегистрируйтесь.</br>
                    ''')
                messages.success(request, mark_safe(message_text))
                return redirect('/client/auth/')
            login(request, user)
            return redirect('/client/account/')
        else:
            print(form.errors)
        content = {'form': form}
        return render(request, 'auth.html', content)


class AccountView(LoginRequiredMixin, TemplateView):
    """ Представление и редактирование данных личного кабинета пользователя """

    model = User
    form_class = UserEditForm
    template_name = 'lk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = get_object_or_404(User, username=user.username)
        return context

    def post(self, request):
        try:
            user_account = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            return redirect('/client/account/')
        form = UserEditForm(request.POST, instance=user_account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return redirect('/client/account/')
        else:
            messages.success(request, 'Заполните все поля для изменения данных')
            return redirect('/client/account/')
        content = {'form': form}
        return render(request, 'lk.html', content)

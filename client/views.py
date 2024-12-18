import random

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from .forms import *
from orders.models import Order
from recipe.models import Recipe, RecipeIngredient

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
        order = Order.objects.filter(user=user, payment_status='PAID').last()

        if not order:
            context['order'] = ''
            return context

        all_allergies = [
            'Рыба и морепродукты',
            'Мясо',
            'Зерновые',
            'Продукты пчеловодства',
            'Орехи и бобовые',
            'Молочные продукты',
        ]
        allergies = ''
        for allergy in all_allergies:
            if allergy in order.allergy:
                allergies = allergies + allergy + '\n'
        context['allergies'] = allergies

        if 'Рыба и морепродукты' in order.allergy:
            allergy_fish = True
        else:
            allergy_fish = False
        if 'Мясо' in order.allergy:
            allergy_meat = True
        else:
            allergy_meat = False
        if 'Зерновые' in order.allergy:
            allergy_cereal = True
        else:
            allergy_cereal = False
        if 'Продукты пчеловодства' in order.allergy:
            allergy_bee = True
        else:
            allergy_bee = False
        if 'Орехи и бобовые' in order.allergy:
            allergy_nuts = True
        else:
            allergy_nuts = False
        if 'Молочные продукты' in order.allergy:
            allergy_milk = True
        else:
            allergy_milk = False

        menu = order.menu.foodtype

        recipes = Recipe.objects.filter(
            foodtype=menu, recommend=True).filter(
            Q(breakfast=order.breakfast) & Q(breakfast=True) |
            Q(lunch=order.lunch) & Q(lunch=True) |
            Q(dinner=order.dinner) & Q(dinner=True) |
            Q(dessert=order.dessert) & Q(dessert=True)).filter(
            ~(Q(allergy_fish=allergy_fish) & Q(allergy_fish=True)) &
            ~(Q(allergy_meat=allergy_meat) & Q(allergy_meat=True)) &
            ~(Q(allergy_cereal=allergy_cereal) & Q(allergy_cereal=True)) &
            ~(Q(allergy_bee=allergy_bee) & Q(allergy_bee=True)) &
            ~(Q(allergy_nuts=allergy_nuts) & Q(allergy_nuts=True)) &
            ~(Q(allergy_milk=allergy_milk) & Q(allergy_milk=True)))

        if recipes.exists():
            recipe = random.choice(recipes)
            calories = sum([recipe_ingredient.calorie for recipe_ingredient in recipe.ingredients.all()])
            recipe.calories = calories
            context['recipe'] = recipe
            context['recipe_ingredients'] = RecipeIngredient.objects.filter(recipe=recipe).select_related('ingredient')
        else:
            context['no_dish'] = 'Не найдено подходящего блюда'

        if order.menu.foodtype == 'keto':
            order.name = 'Кето'
        if order.menu.foodtype == 'veg':
            order.name = 'Вегетарианское'
        if order.menu.foodtype == 'low':
            order.name = 'Низкокалорийное'
        if order.menu.foodtype == 'classic':
            order.name = 'Классическое'

        context['order'] = order

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

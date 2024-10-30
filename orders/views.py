from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView

from .forms import *
from .models import *


def order_create(request):
    # TODO: создать ограничение на выбор только 3х аллергий
    menu = Menu.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            foodtype_price = form.cleaned_data.get('foodtype')
            allergy1 = form.cleaned_data.get('allergy1')
            allergy2 = form.cleaned_data.get('allergy2')
            allergy3 = form.cleaned_data.get('allergy3')
            breakfast = form.cleaned_data.get('breakfast')
            lunch = form.cleaned_data.get('lunch')
            dinner = form.cleaned_data.get('dinner')
            dessert = form.cleaned_data.get('dessert')
            persons = form.cleaned_data.get('persons')
            subscription_period = form.cleaned_data.get('subscription_period')
            allergy = allergy1, allergy2, allergy3
            menu = get_object_or_404(Menu, price=foodtype_price)

            if request.user.is_authenticated:
                order = Order.objects.create(
                    menu=menu,
                    user=get_object_or_404(User, id=request.user.id),
                    allergy=allergy,
                    breakfast=breakfast,
                    lunch=lunch,
                    dinner=dinner,
                    dessert=dessert,
                    persons=persons,
                    subscription_period=subscription_period,
                    cost=foodtype_price
                )
            else:
                messages.success(request, 'Для оформления подписки необходимо войти в свой профиль')
                return redirect('/menu/order/')
            if order:
                return redirect('/menu/pay/')
        else:
           messages.success(request, 'Для оформления подписки необходимо выбрать меню')
    return render(request, 'order.html', {'menu': menu})


class PaymentView(LoginRequiredMixin, TemplateView):
    """ Представление и оплата заказа пользователя """

    model = Order
    template_name = 'payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = get_object_or_404(User, username=user.username)
        order = Order.objects.filter(user=user.id).last()

        if order.menu.foodtype == 'keto':
            order.name = 'Кето'
        if order.menu.foodtype == 'veg':
            order.name = 'Вегетарианское'
        if order.menu.foodtype == 'low':
            order.name = 'Низкокалорийное'
        if order.menu.foodtype == 'classic':
            order.name = 'Классическое'

        if order.breakfast == True:
            order.breakfast = 'да'
        else:
            order.breakfast = 'нет'
        if order.lunch == True:
            order.lunch = 'да'
        else:
            order.lunch = 'нет'
        if order.dinner == True:
            order.dinner = 'да'
        else:
            order.dinner = 'нет'
        if order.dessert == True:
            order.dessert = 'да'
        else:
            order.dessert = 'нет'

        context['order'] = order

        return context

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User, id=request.user.id)
            order = Order.objects.filter(user=user, payment_status='NOT_PAID').last()
            order.payment_status = 'PAID'
            order.save()
            return redirect('/recipe/card/')
        else:
            messages.success(request, 'Введите карту')
            return redirect('/menu/order/')
        content = {'form': form}
        return render(request, 'lk.html', content)
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *


def order_create(request):
    # TODO: создать ограничение на выбор только 3х аллергий
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
                    subscription_period=subscription_period
                )
            else:
                messages.success(request, 'Для оформления подписки необходимо войти в свой профиль')
                return redirect('/menu/order/')
            if order:
                return redirect('/client/account/')
        else:
           messages.success(request, 'Для оформления подписки необходимо выбрать меню')
    return render(request, 'order.html')

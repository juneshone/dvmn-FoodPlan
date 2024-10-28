import random

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from recipe.models import Recipe, RecipeIngredient
from orders.models import Order


def card(request):
    user = request.user
    if user.id:
            order = Order.objects.filter(user=user.id, payment_status='PAID').last()
            if order:
                menu = order.menu.foodtype
                recipe = random.choice(Recipe.objects.filter(foodtype=menu).prefetch_related('ingredients'))
            else:
                messages.success(request, 'Для просмотра всех рецептов необходимо оформить подписку')
                recipe = get_object_or_404(Recipe, id=1)
    else:
        messages.success(request, 'Для просмотра всех рецептов необходимо авторизоваться и оформить подписку')
        recipe = get_object_or_404(Recipe, id=1)

    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe).select_related('ingredient')
    recipe_context = {
        'dish': recipe.dish,
        'image': recipe.image,
        'price': recipe.price,
        'instruction': recipe.instruction,
        'ingredients': recipe_ingredients,
        'calories': sum([recipe_ingredient.ingredient.calorie for recipe_ingredient in recipe_ingredients])
    }
    return render(request, 'card.html', context={'recipe': recipe_context})
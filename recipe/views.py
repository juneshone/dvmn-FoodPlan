import random

from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe, RecipeIngredient


def card(request):
    # recipes = Recipe.objects.all().values_list('id', flat=True)
    # recipe_id = random.choice(recipes)
    # recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe = random.choice(Recipe.objects.all())
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

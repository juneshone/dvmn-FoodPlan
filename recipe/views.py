from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe, RecipeIngredient


def card(request, recipe_num):
    # TODO: привязать рецепты к меню
    try:
        recipe = get_object_or_404(Recipe, id=recipe_num)
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe).select_related('ingredient')
        recipe_context = {
            'dish': recipe.dish,
            'image': recipe.image,
            'price': recipe.price,
            'instruction': recipe.instruction,
            'ingredients': recipe_ingredients,
            'calories': sum([i.ingredient.calorie for i in recipe_ingredients])
        }
        return render(request, 'card.html', context={'recipe': recipe_context})
    except:
        return render(request, 'card.html', context={
                'not_recipe': f'Рецепта с id={recipe_num} не найдено'
            }
        )

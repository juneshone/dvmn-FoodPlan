from django.contrib import admin

from recipe.models import Ingredient, Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 5


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('dish',)
    list_display = ('dish', 'price',)
    raw_id_fields = ('ingredients',)
    inlines = (RecipeIngredientInline,)

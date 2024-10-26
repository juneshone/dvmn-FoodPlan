from django.contrib import admin
from django.utils.html import format_html

from recipe.models import Ingredient, Recipe, RecipeIngredient

MAX_IMAGE_WIDTH = 300
MAX_IMAGE_HEIGHT = 200


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 5


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ('dish', 'get_preview')
    list_display = ('dish', 'price',)
    raw_id_fields = ('ingredients',)
    inlines = (RecipeIngredientInline,)
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: {}px; max-height={}px" />', obj.image.url, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT)
        return 'картинка блюда'
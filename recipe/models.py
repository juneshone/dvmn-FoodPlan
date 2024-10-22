from django.db import models


class Ingredient(models.Model):
    title = models.CharField(
        'Название ингредиента',
        max_length=200
    )
    calorie = models.IntegerField(
        'Калорийность ингредиента'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['title']


class Recipe(models.Model):
    dish = models.CharField(
        'Название блюда', max_length=100
    )
    image = models.ImageField(
        'Изображение',
        upload_to='image',
        blank=True
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        related_name="recipes",
        verbose_name='Ингредиенты'
    )
    price = models.DecimalField(
        'Стоимость блюда',
        max_digits=10,
        decimal_places=2,
    )
    instruction = models.TextField(
        'Инструкция приготовления'
    )

    def __str__(self):
        return self.dish

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['dish']


class RecipeIngredient(models.Model):
    quantity = models.IntegerField(
        'Количество ингредиента в рецепте'
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=20,
        default='грамм'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент рецепта'
    )

    class Meta:
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецепта'

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
    FOODTYPE_CHOICES = (
        ('classic', 'Классическое'),
        ('low', 'Низкоуглеводное'),
        ('veg', 'Вегетарианское'),
        ('keto', 'Кето'),
    )
    foodtype = models.CharField(
        verbose_name= 'меню',
        choices=FOODTYPE_CHOICES,
        max_length=50
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
    breakfast = models.BooleanField(
        verbose_name='Завтрак',
        default=True
    )
    lunch = models.BooleanField(
        verbose_name='Обед',
        default=True
    )
    dinner = models.BooleanField(
        verbose_name='Ужин',
        default=True
    )
    dessert = models.BooleanField(
        verbose_name='Десерт',
        default=True
    )

    recommend = models.BooleanField(
        verbose_name='Рекомендовать пользователям',
        default=True
    )

    allergy_fish = models.BooleanField(
        verbose_name='Аллергия на рыбу и морепродукты',
        default=False
    )
    allergy_meat = models.BooleanField(
        verbose_name='Аллергия на мясо',
        default=False
    )
    allergy_cereal = models.BooleanField(
        verbose_name='Аллергия на зерновые',
        default=False
    )
    allergy_bee = models.BooleanField(
        verbose_name='Аллергия на продукты пчеловодства',
        default=False
    )
    allergy_nuts = models.BooleanField(
        verbose_name='Аллергия на орехи и бобовые',
        default=False
    )
    allergy_milk = models.BooleanField(
        verbose_name='Аллергия на молочные продукты',
        default=False
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

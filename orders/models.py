from django.core.validators import MinValueValidator
from django.db import models

from client.models import User
from recipe.models import Recipe


# class Menu(models.Model):
#     title = models.CharField(max_length=50)
#     recipes = models.ForeignKey(
#         Recipe,
#         verbose_name='рецепты',
#         related_name='recipes',
#         on_delete=models.CASCADE
#     )
#

class Subscription(models.Model):
    MENU_CHOICES = (
        ('classic', 'Классическое'),
        ('low', 'Низкоуглеводное'),
        ('veg', 'Вегетарианское'),
        ('keto', 'Кето'),
    )
    PERIOD_CHOICES = (
        (1, '1 мес'),
        (3, '3 мес'),
        (6, '6 мес'),
        (12, '12 мес')
    )
    PERSONS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )
    menu = models.CharField(
        verbose_name='меню',
        max_length=10,
        choices=MENU_CHOICES,
        blank=True,
    )
    datestart = models.DateTimeField(
        verbose_name='дата начала',
        auto_now_add=True
    )
    period = models.PositiveIntegerField(
        choices=PERIOD_CHOICES,
        verbose_name='период',
        default=1,
    )
    breakfast = models.BooleanField(
        verbose_name='завтрак',
        blank=True
    )
    lunch = models.BooleanField(
        verbose_name='обед',
        blank=True
    )
    dinner = models.BooleanField(
        verbose_name='ужин',
        blank=True
    )
    dessert = models.BooleanField(
        verbose_name='десерт',
        blank=True
    )
    persons = models.PositiveIntegerField(
        verbose_name='кол-во персон',
        choices=PERSONS_CHOICES,
        default=1,
        db_index=True
    )
    allergy1 = models.BooleanField(
        verbose_name='Рыба и морепродукты',
        blank=True
    )
    allergy2 = models.BooleanField(
        verbose_name='Мясо',
        blank=True
    )
    allergy3 = models.BooleanField(
        verbose_name='Зерновые',
        blank=True
    )
    allergy4 = models.BooleanField(
        verbose_name='Продукты пчеловодства',
        blank=True
    )
    allergy5 = models.BooleanField(
        verbose_name='Орехи и бобовые',
        blank=True
    )
    allergy6 = models.BooleanField(
        verbose_name='Молочные продукты',
        blank=True
    )
    promocode = models.CharField(
        verbose_name='промокод',
        max_length=50,
        blank=True
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True
    )
    active = models.BooleanField(
        verbose_name='статус подписки',
        default=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        related_name='users',
        on_delete=models.CASCADE
    )

    class Meta():
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f'{self.id} {self.user.username}'


# class Allergy(models.Model):
#     title = models.CharField(
#         verbose_name='аллергия',
#         max_length=50,
#     )
#
#
# class OrderAllergy(models.Model):
#     allergy = models.ForeignKey(
#         Allergy,
#         verbose_name='аллергии',
#         related_name='allergies',
#         on_delete=models.CASCADE,
#     )
#     order = models.ForeignKey(
#         Order,
#         verbose_name='подписки',
#         related_name='orders',
#         on_delete=models.CASCADE,
#     )

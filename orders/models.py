from django.core.validators import MinValueValidator
from django.db import models

from client.models import User
from recipe.models import Recipe


class Menu(models.Model):
    title = models.CharField(max_length=50)
    recipes = models.ForeignKey(
        Recipe,
        verbose_name='рецепты',
        related_name='recipes',
        on_delete=models.CASCADE
    )




class Order(models.Model):
    PERSONS_CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
    ]
    menu = models.ForeignKey(
        Menu,
        verbose_name='меню',
        related_name='menu',
        on_delete=models.CASCADE
    )
    datestart = models.DateTimeField(
        verbose_name='дата начала'
    )
    dateend = models.DateTimeField(
        verbose_name='дата конца'
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        related_name='users',
        on_delete=models.CASCADE
    )
    persons = models.PositiveIntegerField(
        choices=PERSONS_CHOICES,
        default='UNPROCESSED',
        db_index=True
    )
    breakfast = models.BooleanField(
        verbose_name='завтрак',
        null=False,
        blank=True
    )
    lunch = models.BooleanField(
        verbose_name='обед',
        null=False,
        blank=True
    )
    dinner = models.BooleanField(
        verbose_name='ужин',
        null=False,
        blank=True
    )
    dessert = models.BooleanField(
        verbose_name='десерт',
        null=False,
        blank=True
    )
    promocode = models.CharField(
        verbose_name='промокод',
        max_length=50,
        null=False,
        blank=True
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=False,
        blank=True
    )
    active = models.BooleanField(
        verbose_name='статус подписки',
        default=False
    )

    class Meta():
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f'{self.id} {self.user.name}'


class Allergy(models.Model):
    title = models.CharField(
        verbose_name='аллергия',
        max_length=50,
        null=True,
        blank=True
    )
    order = models.ForeignKey(
        Order,
        verbose_name='аллергии',
        related_name='allergies',
        on_delete=models.CASCADE
    )
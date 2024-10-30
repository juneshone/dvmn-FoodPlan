from django.core.validators import MinValueValidator
from django.db import models
from client.models import User



class Menu(models.Model):
    FOODTYPE_CHOICES = (
        ('classic', 'Классическое'),
        ('low', 'Низкоуглеводное'),
        ('veg', 'Вегетарианское'),
        ('keto', 'Кето'),
    )
    foodtype = models.CharField(
        verbose_name='Тип меню',
        choices=FOODTYPE_CHOICES,
        max_length=50
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='image'
    )
    price = models.DecimalField(
        verbose_name='Стоимость',
        max_digits=10,
        decimal_places=0
    )

    def __str__(self):
        return self.foodtype

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Order(models.Model):
    STATUS_CHOICES = [
        ('PAID', 'Оплаченный'),
        ('NOT_PAID', 'Не оплаченный'),
    ]
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='user',
        on_delete=models.CASCADE
    )
    subscription_period = models.PositiveIntegerField(
        verbose_name='Срок подписки',
        default=1
    )

    datestart = models.DateTimeField(
        verbose_name='Дата начала подписки',
        auto_now_add=True
    )
    persons = models.PositiveIntegerField(
        verbose_name='Количество персон',
        default=1
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
    allergy = models.CharField(
        verbose_name='Аллергия',
        max_length=50,
        default=None,
        blank=True,
        null=True
    )
    cost = models.DecimalField(
        verbose_name='Стоимость',
        max_digits=10,
        decimal_places=0
    )
    payment_status = models.CharField(
        verbose_name='Статус',
        max_length=50,
        choices=STATUS_CHOICES,
        default='NOT_PAID'
    )

    def __str__(self):
        return f'{self.menu} {self.user}'

    class Meta:
        verbose_name = 'Подписка на меню'
        verbose_name_plural = 'Подписки на меню'


# class Payment(models.Model):
#     amount = models.DecimalField(verbose_name='Сумма', max_digits=10, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Платеж'
#         verbose_name_plural = 'Платежи'
#
#     def __str__(self):
#         return f'Платеж {self.amount}'
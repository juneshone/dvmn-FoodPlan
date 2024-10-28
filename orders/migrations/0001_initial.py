# Generated by Django 4.2 on 2024-10-28 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodtype', models.CharField(choices=[('classic', 'Классическое'), ('low', 'Низкоуглеводное'), ('veg', 'Вегетарианское'), ('keto', 'Кето')], max_length=50, verbose_name='Тип меню')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_period', models.PositiveIntegerField(default=1, verbose_name='Срок подписки')),
                ('datestart', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала подписки')),
                ('persons', models.PositiveIntegerField(default=1, verbose_name='Количество персон')),
                ('breakfast', models.BooleanField(default=True, verbose_name='Завтрак')),
                ('lunch', models.BooleanField(default=True, verbose_name='Обед')),
                ('dinner', models.BooleanField(default=True, verbose_name='Ужин')),
                ('dessert', models.BooleanField(default=True, verbose_name='Десерт')),
                ('allergy', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Аллергия')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('payment_status', models.CharField(choices=[('PAID', 'Оплаченный'), ('NOT_PAID', 'Не оплаченный')], default='NOT_PAID', max_length=50, verbose_name='Статус')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.menu', verbose_name='Меню')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Подписка на меню',
                'verbose_name_plural': 'Подписки на меню',
            },
        ),
    ]

import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """ Менеджер авторизации для пользователя """

    @classmethod
    def normalize_username(cls, username):
        """ Нижний регистр логина"""
        return username.lower()

    def _create_user(self, username, last_name, first_name, password=None, **extra_fields):
        """
        Создает и возвращает пользователя с заданными именем, фамилией, и паролем (защищенный метод)
        """
        if not username:
            raise ValueError('Не указан адрес электронной почты')
        if not last_name:
            raise ValueError('Не указана фамилия')
        if not first_name:
            raise ValueError('Не указано имя')
        username = self.normalize_username(username)
        user = self.model(username=username, last_name=last_name, first_name=first_name, **extra_fields)
        user.set_password(password)
        # user.secure_code = password
        user.save(using=self._db)
        return user

    def create_user(self, username, last_name, first_name, password=None, **extra_fields):
        """
        Создает и возвращает пользователя с заданными именем, фамилией, и паролем (публичный метод)
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, last_name, first_name, password, **extra_fields)

    def create_superuser(self, username, last_name, first_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('У суперпользователя должно быть значение is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('У суперпользователя должно быть значение is_superuser=True.')

        return self._create_user(username, last_name, first_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Пользователь системы """

    id = models.AutoField('Идентификатор', primary_key=True)
    is_staff = models.BooleanField('Признак отношения к персоналу', default=False)
    username = models.CharField('Имя пользователя(логин email)', max_length=50, unique=True)
    last_name = models.CharField('Фамилия', max_length=25)
    first_name = models.CharField('Имя', max_length=25)
    password = models.CharField('Пароль', max_length=100)

    objects = UserManager()

    REQUIRED_FIELDS = ['last_name', 'first_name', 'password']
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользовватели'

    @property
    def token(self):
        """ Токен пользователя """

        return self._generate_jwt_token()

    def __str__(self):
        """ Возвращает строковое представление пользователя """

        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def get_short_name(self):
        """ Возвращает фамилию и инициалы """

        return f'{self.last_name} {self.first_name[0]}'

    def _generate_jwt_token(self):
        """
        Создает веб-токен JSON, в котором хранится
        идентификатор этого пользователя и срок его действия составляет 30 дней
        """

        dt = datetime.now() + timedelta(days=30) # время жизни токена
        token = jwt.encode({
            'user_id': self.id,
            'exp': int(dt.strftime('%S'))
        }, settings.DJANGO_SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'token',)

    def create(self, validated_data):
        return User.object.create_user(**validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        super.update(instance, validated_data)
        return instance


class LoginSerializer(serializers.Serializer):
    """ Аутентификация пользователя по существующему паролю (возвращает токен) """

    username = serializers.CharField(max_length=50, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('Не указан логин')
        if password is None:
            raise serializers.ValidationError('Не указан пароль')
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed('Аутентификация пользователя не удалась')
        user_data = UserSerializer(user)
        return user_data.data


class SignUpSerializer(serializers.Serializer):
    """ Регистрация пользователя (возвращает информацию о пользователе) """

    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    password_confirmation = serializers.CharField(max_length=128, write_only=True, required=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)

    def validate(self, data):
        users_count = User.objects.filter(username=data['username']).count()
        errors = []
        if users_count > 0:
            errors.append(
                {'username': 'Пользователь уже существует'}
            )
        if data['password'] != data['password_confirmation']:
            errors.append(
                {'password_confirmation': 'Подтверждение пароля не совпадает с самим паролем'}
            )
        if len(errors) > 0:
            raise serializers.ValidationError({'errors': errors})
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            last_name=data['last_name'],
            first_name=data['first_name']
        )
        user_data = UserSerializer(user)
        return user_data.data

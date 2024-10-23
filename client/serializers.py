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



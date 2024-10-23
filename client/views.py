from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import *

class LoginAPIView(APIView):
    """ Аутентификация существующего пользователя """
    serializer_class = LoginSerializer
    def post(self, request):
        """ Проверяет существует ли пользователь и возвращает токен в случае аутентификации """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)


def account(request):
    return render(request, 'lk.html')


def registration(request):
    return render(request, 'registration.html')

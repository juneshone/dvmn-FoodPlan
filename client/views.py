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


class SighUpAPIView(APIView):
    """ Регистрация пользователя """
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.validated_data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                'status': False,
                'detail': serializer.errors
            })


def account(request):
    return render(request, 'lk.html')

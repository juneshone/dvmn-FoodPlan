from django.urls import path, re_path

from .views import *
from . import views


urlpatterns = [
    re_path(r'^auth/?$', LoginAPIView.as_view(), name='auth'),
    re_path(r'^registration/?$', SighUpAPIView.as_view(), name='registration'),
    path('account/', views.account, name='account'),
]

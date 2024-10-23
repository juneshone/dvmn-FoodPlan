from django.urls import path, re_path

from .views import *
from . import views


urlpatterns = [
    re_path(r'^auth/?$', LoginAPIView.as_view(), name='auth'),
    path('account/', views.account, name='account'),
    path('registration/', views.registration, name='registration'),
]

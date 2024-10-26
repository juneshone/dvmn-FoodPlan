from django.urls import path, re_path

from .api_views import *
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    re_path(r'^api-auth/?$', LoginAPIView.as_view()),
    re_path(r'^api-registration/?$', SighUpAPIView.as_view()),
    path('account/', views.AccountView.as_view(), name='account'),
    path('registration/', views.SignUp.as_view(), name='registration'),
    path('auth/', views.UserLogin.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

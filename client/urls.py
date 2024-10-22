from django.urls import path

from . import views


urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('account/', views.account, name='account'),
    path('registration/', views.registration, name='registration'),
]

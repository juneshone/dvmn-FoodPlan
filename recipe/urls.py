from django.urls import path

from . import views


urlpatterns = [
    path(f'card<int:recipe_num>/', views.card, name='card'),
]

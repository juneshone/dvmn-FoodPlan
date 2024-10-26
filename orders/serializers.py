from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Subscription


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['id', 'menu', 'datestart', 'period', 'persons', 'breakfast',
                  'lunch', 'dinner', 'dessert', 'promocode', 'allergy1', 'allergy1', 'allergy2',
                  'allergy3', 'allergy4', 'allergy5', 'allergy6']



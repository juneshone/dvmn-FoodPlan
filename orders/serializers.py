from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Order


# class OrderAllergySerializer(ModelSerializer):
#
#     class Meta:
#         model = OrderAllergy
#         fields = ['allergy_title']

class OrderSerializer(ModelSerializer):
    # allergies = OrderAllergySerializer(many=True, allow_empty=False, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'menu_title', 'datestart', 'period', 'user', 'persons', 'breakfast',
                  'lunch', 'dinner', 'dessert', 'promocode', 'allergy1', 'allergy1', 'allergy2',
                  'allergy3', 'allergy4', 'allergy5', 'allergy6']


    def create(self, validated_data):
        print(validated_data)
        # allergies = validated_data.pop('allergies')
        #
        # order = Order.objects.create(**validated_data)
        #
        # for allergy in allergies:
        #     try:
        #         allergy = Allergy.objects.get(title=allergy['title'])
        #     except Allergy.DoesNotExist:
        #         raise ValidationError(f"Аллергия с названием {allergy['title']} не найдена.")
        #
        #     OrderAllergy.objects.create(order=order, allergy=allergy)
        #
        order = Order.objects.create(**validated_data)
        return order
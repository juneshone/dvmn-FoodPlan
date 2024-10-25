from django.shortcuts import render
from rest_framework.decorators import api_view
from pprint import pprint


from orders.serializers import OrderSerializer


@api_view(['POST'])
def order(request):
    ord = {"period": 0, "menu": "classic", "breakfast": 1, "lunch": 0, "dinner": 1, "dessert": 0, "persons": 2, "allergy2": 1}
    # serializer = OrderSerializer(data=request.data)
    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    data = request.data
    pprint(data)
    return render(request, 'order.html')

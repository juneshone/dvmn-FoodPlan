import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from pprint import pprint


# from orders.serializers import OrderSerializer
#
#
# @api_view(['POST'])
# def order(request):
#     ord = {"period": 0, "menu": "classic", "breakfast": 1, "lunch": 0, "dinner": 1, "dessert": 0, "persons": 2, "allergy2": 1}
#     # serializer = OrderSerializer(data=request.data)
#     # serializer.is_valid(raise_exception=True)
#     # serializer.save()
#     data = request.data
#     pprint(data)
#     return render(request, 'order.html')

#
# from django.shortcuts import render, redirect
# from .forms import OrderForm
#
#
# def order(request):
#     print(request.method)
#     if request.method == 'GET':
#         form = OrderForm(request.GET)
#         print(form)
#         if form.is_valid():
#             form.save()
#
#             # return redirect('success_url')  # Переход на страницу успеха после успешной отправки формы
#     else:
#         form = OrderForm()
#     return render(request, 'order.html', {'form': form})


def order(request):
    print(request.method)
    data = request.GET
    pprint(data)

    return render(request, 'order.html')
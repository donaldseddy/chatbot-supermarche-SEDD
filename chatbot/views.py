from django.shortcuts import render
from django.http import JsonResponse
from chatbot.services.product_service import get_all_products

def product_list_view(request):
    data = get_all_products()
    return JsonResponse(data, safe=False)


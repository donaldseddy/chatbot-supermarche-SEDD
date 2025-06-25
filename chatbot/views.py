from django.shortcuts import render
from django.http import JsonResponse
from chatbot.services.product_service import *

def product_list_view(request):
    data = get_all_products()
    return JsonResponse(data, safe=False)

def product_detail_view(request, product_id):
    product = get_product_by_id(product_id)
    if product:
        return JsonResponse(product, safe=False)
    else:
        return JsonResponse({"error": "Product not found"}, status=404)
    

def product_category_view(request, category):
    products = get_products_by_category(category)
    if products:
        return JsonResponse(products, safe=False)
    else:
        return JsonResponse({"error": "No products found in this category"}, status=404)
    
def product_pagination_view(request, nb_page=1, limit=25):
    products = get_products_by_pagination(page=nb_page, limit=limit)
    if products:
        return JsonResponse(products, safe=False)
    else:
        return JsonResponse({"error": "No products found"}, status=404)
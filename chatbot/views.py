from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatbot.services.product_service import *
import json

@csrf_exempt
def product_list_view(request):
    if request.method == 'GET':
        products = get_all_products()
        if products:
            return JsonResponse(products, safe=False)
        return JsonResponse({"error": "No products found"}, status=404)


@csrf_exempt
def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = get_product_by_id(product_id)
        if product:
            return JsonResponse(product, safe=False)
        return JsonResponse({"error": "Product not found"}, status=404)


@csrf_exempt
def product_category_view(request, category):
    if request.method == 'GET':
        products = get_products_by_category(category)
        if products:
            return JsonResponse(products, safe=False)
        return JsonResponse({"error": "No products found in this category"}, status=404)

@csrf_exempt
def product_pagination_view(request, page=1, limit=25):
    if request.method == 'GET':
        products = get_products_by_pagination(page, limit)
        if products:
            return JsonResponse(products, safe=False)
        return JsonResponse({"error": "No products found"}, status=404)
    

@csrf_exempt
def product_search_view(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if not query:
            return JsonResponse({"error": "Query parameter is required"}, status=400)
        
        products = search_products(query)
        if products:
            return JsonResponse(products, safe=False)
        return JsonResponse({"error": "No products found matching the query"}, status=404)
    

@csrf_exempt
def delete_product_view(request, product_id):
    if request.method == 'DELETE':
        delete_result = delete_product_by_id(product_id)
        if delete_result and delete_result["acknowledged"] and delete_result["deletedCount"] > 0:
            return JsonResponse({"message": "Product deleted successfully"}, status=200)
        return JsonResponse({"error": "Product not found or could not be deleted"}, status=404)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def add_product_view(request):
    if request.method == 'POST':
        try:
            product_data = json.loads(request.body)
            inserted_id = add_product(product_data)
            if inserted_id:
                return JsonResponse({"message": "Product added successfully", "id": str(inserted_id)}, status=201)
            return JsonResponse({"error": "Failed to add product"}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def update_product_view(request, product_id):
    if request.method == 'PUT':
        try:
            product_data = json.loads(request.body)
            updated_product = update_product_by_id(product_id, product_data)
            if updated_product:
                return JsonResponse({"message": "Product updated successfully", "product": updated_product}, status=200)
            return JsonResponse({"error": "Failed to update product"}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


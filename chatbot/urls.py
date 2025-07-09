from django.urls import path
from .views import *

urlpatterns = [
    path("products/", product_list_view, name="product-list"),
    path("products/<str:product_id>/", product_detail_view, name="product-detail"),
    path("products/category/<str:category>/", product_category_view, name="product-category"),
    path("products/pagination/<int:nb_page>/<int:limit>/", product_pagination_view, name="product-pagination"),
    path("products/pagination/<int:nb_page>/", product_pagination_view, name="product-pagination-default"),
    path("products/pagination/", product_pagination_view, name="product-pagination-default"),
    path("products/search/", product_search_view, name="product-search"),
    path("products/delete/<str:product_id>/", delete_product_view, name="product-delete"),
    path("products/delete/", delete_product_view, name="product-delete-default"),
    path("products/add/", add_product_view, name="product-add"),
    path("products/update/<str:product_id>/", update_product_view, name="product-update"),
    path("products/update/", update_product_view, name="product-update-default"),
    
]



from django.urls import path
from .views import product_list_view

urlpatterns = [
    path("products/", product_list_view, name="product-list"),
    path("products/<int:product_id>/", product_list_view, name="product-detail"),
    path("products/<int:product_id>/add-to-cart/", product_list_view, name="add-to-cart"),
    path("products/<int:product_id>/remove-from-cart/", product_list_view, name="remove-from-cart"),
    path("products/<int:product_id>/update-quantity/", product_list_view, name="update-quantity"),
    path("products/<int:product_id>/checkout/", product_list_view, name="checkout"),
    path("products/<int:product_id>/search/", product_list_view, name="search-products"),
    path("products/<int:product_id>/filter/", product_list_view, name="filter-products"),
    path("products/<int:product_id>/sort/", product_list_view, name="sort-products"),
    path("products/<int:product_id>/recommendations/", product_list_view, name="product-recommendations"),
    path("products/<int:product_id>/reviews/", product_list_view, name="product-reviews"),
    path("products/<int:product_id>/ratings/", product_list_view, name="product-ratings"),
    path("products/<int:product_id>/related-products/", product_list_view, name="related-products"),
    path("products/<int:product_id>/compare/", product_list_view, name="compare-products"),

    
]



from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list, name="products"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:pk>", views.category_detail, name="category_detail"),
    path("categories/<int:pk>/products", views.category_products),
]
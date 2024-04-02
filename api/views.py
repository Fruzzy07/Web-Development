from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Product, Category


def index(request):
    return HttpResponse("Main page works")


def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    return JsonResponse(data)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = {'product': {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category_id': product.category.id,
        'category_name': product.category.name,
    }}
    return JsonResponse(data)


def category_list(request):
    categories = Category.objects.all()
    data = {'categories': list(categories.values())}
    return JsonResponse(data)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = {'category': {
        'name': category.name,
        'id': category.pk,
        'products': list(category.product_set.values('id', 'name'))
    }}
    return JsonResponse(data)


def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.product_set.values('id', 'name')
    data = {'products': list(products)}
    return JsonResponse(data)

from django.shortcuts import render
from .models import ProductModel, ProductCategoryModel


def shop_index(request):
    products = ProductModel.objects.prefetch_related('category').all()
    categories = ProductCategoryModel.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'products_count': products.count(),
        'categories_count': categories.count(),
    }
    return render(request, 'shop/index.html', context)
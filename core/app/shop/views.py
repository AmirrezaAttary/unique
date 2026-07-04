from django.shortcuts import render
from .models import ProductModel, ProductCategoryModel


def shop_index(request):
    products = list(ProductModel.objects.prefetch_related('category').all())
    print("PRODUCTS COUNT:", len(products))
    for p in products:
        print(p.title, "-> categories:", list(p.category.all()))
    
    categories = ProductCategoryModel.objects.all()
    products.sort(key=lambda p: p.category.first().title if p.category.exists() else '')

    context = {
        'categorized_products': products,
        'categories': categories,
        'products_count': len(products),
        'categories_count': categories.count(),
    }
    return render(request, 'shop/index.html', context)
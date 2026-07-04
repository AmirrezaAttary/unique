from django.shortcuts import render
from .models import ProductModel, ProductCategoryModel


def shop_index(request):
    categories = ProductCategoryModel.objects.prefetch_related('productmodel_set').all()
    
    # ساخت لیستی از (کتگوری، محصولات آن کتگوری)
    categorized_products = []
    for category in categories:
        products = category.productmodel_set.all()
        if products.exists():
            categorized_products.append({
                'category': category,
                'products': products,
            })

    context = {
        'categorized_products': categorized_products,
        'products_count': ProductModel.objects.count(),
        'categories_count': categories.count(),
    }
    return render(request, 'shop/index.html', context)
from django.contrib import admin
from django.utils.html import format_html

from .models import ProductModel, ProductCategoryModel


@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "product_count",
        "created_date",
    )
    search_fields = ("title",)
    ordering = ("-created_date",)
    readonly_fields = ("created_date", "updated_date")

    def product_count(self, obj):
        return obj.productmodel_set.count()

    product_count.short_description = "تعداد محصولات"


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_preview",
        "title",
        "get_categories",
        "created_date",
    )

    list_filter = (
        "category",
        "created_date",
    )

    search_fields = (
        "title",
        "description",
        "category__title",
    )

    filter_horizontal = ("category",)

    readonly_fields = (
        "image_preview",
        "created_date",
        "updated_date",
    )

    list_per_page = 20
    ordering = ("-created_date",)

    fieldsets = (
        ("اطلاعات محصول", {
            "fields": (
                "title",
                "category",
                "description",
            )
        }),
        ("تصویر", {
            "fields": (
                "image",
                "image_preview",
            )
        }),
        ("زمان‌ها", {
            "fields": (
                "created_date",
                "updated_date",
            )
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("category")

    def get_categories(self, obj):
        return ", ".join(cat.title for cat in obj.category.all())

    get_categories.short_description = "دسته‌بندی"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="70" height="70" style="border-radius:8px;object-fit:cover;" />',
                obj.image.url,
            )
        return "-"

    image_preview.short_description = "تصویر"
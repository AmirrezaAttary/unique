from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_index, name='shop-index'),
]
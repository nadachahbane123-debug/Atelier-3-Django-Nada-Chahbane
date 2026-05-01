from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('products/categories/', views.category_list, name='category_list'),
    path('products/category/<int:id>/', views.category_detail, name='category_detail'),
]
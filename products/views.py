from django.shortcuts import render, get_object_or_404
from .models import Product, Category
def index(request):
    return render(request, 'index.html')
# Liste de tous les produits
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

# Détail d'un produit spécifique
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

# Liste de toutes les catégories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    
    products = category.products.all() 
    
    return render(request, 'category_detail.html', {
        'category': category, 
        'products': products
    })
from django.shortcuts import render, get_object_or_404  # <-- Yahan 404 theek kar diya
from .models import Product
from django.db.models import Q

# 1. Home Page View
def home_view(request):
    featured_products = Product.objects.all()[:2]
    return render(request, 'index.html', {'featured_products': featured_products})

# 2. Product Listing Page View (with Search)
def product_list_view(request):
    query = request.GET.get('q', '')
    
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )
    else:
        products = Product.objects.all()
        
    return render(request, 'products.html', {'products': products, 'query': query})

# 3. Product Detail Page View (Last 4 lines)
def product_detail_view(request, product_id):
    # Yeh line ab bilkul theek hai
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product-detail.html', {'product': product})
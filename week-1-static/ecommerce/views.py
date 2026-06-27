from django.shortcuts import render
from django.http import Http404

# Dummy data sirf Week 1 ke liye taake pages khali na lagein
SAMPLE_PRODUCTS = [
    { 'id': '1', 'name': 'Premium Wireless Headphones', 'price': 299, 'image': 'https://via.placeholder.com/150', 'description': 'High-quality sound with noise cancellation.' },
    { 'id': '2', 'name': 'Smart Fitness Watch', 'price': 149, 'image': 'https://via.placeholder.com/150', 'description': 'Track your workouts and health metrics daily.' },
    { 'id': '3', 'name': 'Mechanical Gaming Keyboard', 'price': 99, 'image': 'https://via.placeholder.com/150', 'description': 'RGB backlit mechanical switches for fast typing.' }
]

def home_view(request):
    # Pehle 2 products home page par dikhane ke liye
    context = { 'featured_products': SAMPLE_PRODUCTS[:2] }
    return render(request, 'index.html', context)

def product_list_view(request):
    context = { 'products': SAMPLE_PRODUCTS }
    return render(request, 'products.html', context)

def product_detail_view(request, product_id):
    product = next((p for p in SAMPLE_PRODUCTS if p['id'] == str(product_id)), None)
    if product is None:
        raise Http404("Product nahi mila!")
    context = { 'product': product }
    return render(request, 'product-detail.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product

# 1. Home View
def home_view(request):
    featured_products = Product.objects.all()[:2]
    return render(request, 'index.html', {'featured_products': featured_products})

# 2. Product List View with Search AND Pagination
def product_list_view(request):
    query = request.GET.get('q', '')
    if query:
        products_list = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
    else:
        products_list = Product.objects.all()

    # Pagination Logic: Har page par sirf 2 products dikhane ke liye (Tension free testing)
    paginator = Paginator(products_list, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj, 'query': query})

# 3. Product Detail View
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product-detail.html', {'product': product})

# 4. Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# 5. Add Product View (Sirf Logged-in Users ke liye restricted)
@login_required
def add_product_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        description = request.POST['description']
        stock = request.POST['stock']
        image = request.POST.get('image', '')
        if not image.strip():
            image = "https://via.placeholder.com/150"
        
        Product.objects.create(
            name=name, 
            price=price, 
            category=category, 
            description=description, 
            stock=stock,
            image=image
        )
        return redirect('product_list')
        
    return render(request, 'add-product.html')
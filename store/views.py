from django.shortcuts import render, get_object_or_404
from .models import Product, Gift

def home(request):
    # Show some featured products on homepage
    featured_products = Product.objects.all()[:6]  
    return render(request, 'store/home.html', {'featured_products': featured_products})

def products(request):
    # Get all products that are NOT gifts
    products = Product.objects.exclude(gift__isnull=False)
    return render(request, 'store/product.html', {'products': products})

def gifts(request):
    gifts = Gift.objects.all()
    return render(request, 'store/gifts.html', {'gifts': gifts})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'store/search_results.html', {'results': results, 'query': query})
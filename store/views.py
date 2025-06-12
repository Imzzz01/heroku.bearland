from django.shortcuts import render, get_object_or_404
from .models import Product, Gift
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store:home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'store/login.html')

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
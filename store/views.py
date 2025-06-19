from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Gift
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q 

# Store Views
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
    return render(request, 'store/login.html')# This view handles user login

# This view handles the homepage and displays featured products
def home(request):
    # Show some featured products on homepage
    featured_products = Product.objects.all()[:6]  
    return render(request, 'store/home.html', {'featured_products': featured_products})

def products(request):
   
    products = Product.objects.exclude(gift__isnull=False)
    return render(request, 'store/product.html', {'products': products})
# This view lists all products excluding those that are gifts
def gifts(request):
    gifts = Gift.objects.all()
    return render(request, 'store/gifts.html', {'gifts': gifts})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.exclude(pk=pk).order_by('?')[:3]
    
    return render(request, 'store/product_details.html', {
        'product': product,
        'related_products': related_products
    })

def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        results = Product.objects.none()
        
    return render(request, 'store/search_results.html', {
        'results': results,
        'query': query
    })
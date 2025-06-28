from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Gift
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q 
from django.core.mail import send_mail
from django.shortcuts import redirect
# from wishlist.models import Wishlist, WishlistItem

# Store Views

def login_view(request):
    """
    Handles user authentication and login process.
    
    Args: request HttpRequest object 
    
    Returns: 
    - Redirect to home page if authentication succeeds
    - Rendered login template with error message if authentication fails 
    """
    
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
    """
    Displays the homepage with featured products 
    
    Args: 
        request: HttpRequest object
        
    Returns: 
        Rendered home template with featured products context
    """
    # Show some featured products on homepage
    featured_products = Product.objects.all()[:6]  
    return render(request, 'store/home.html', {'featured_products': featured_products})

def products(request):
   """
   Lists all regular products ( excluding gift items).

   Args: 
       request: HttpRequest object
    
   Returns:
       Rendered products template with product list context
    """
    products = Product.objects.exclude(gift__isnull=False)
    return render(request, 'store/product.html', {'products': products})
# This view lists all products excluding those that are gifts
def gifts(request):
    """
    Lists all gift products
    
    Args: 
        request: HttpRequest object 
        
    Returns: 
        Rendered gifts template with gift items context 
    """
        
    gifts = Gift.objects.all()
    return render(request, 'store/gifts.html', {'gifts': gifts})

def product_detail(request, pk):
    """
    Display detailed view of a single product with related products.
    
    Args: 
        request: HttpRequest object 
        pk: Primary key of the product to display 
        
    Returns: 
        Rendered product detail template with product and related products context
    """
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.exclude(pk=pk).order_by('?')[:3]
    
    return render(request, 'store/product_details.html', {
        'product': product,
        'related_products': related_products
    })

def search(request):
    """
    Handles product search funtionality
    
    Args: 
        request: HttpRequest object with search query parameter
        
    Returns: 
        Rendered search results template with matching products and search query
    """
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
    
 
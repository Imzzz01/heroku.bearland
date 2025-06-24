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
    
    from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Send email
        try:
            send_mail(
                f"Contact Form: {subject}",
                f"From: {name} <{email}>\n\n{message}",
                email,  # from email
                [settings.DEFAULT_FROM_EMAIL], 
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f'There was an error sending your message: {str(e)}')
        
        return redirect('store:home')
    

    return redirect('store:home')
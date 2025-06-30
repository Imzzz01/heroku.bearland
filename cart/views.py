from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Cart, CartItem
from store.models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def get_or_create_cart(request):
    """
    Helper function to get or create a cart for the current session/user

    Handles both authenticated users (tied to user account) and anonymous users (tied to session key)

    Args: 
        request: HttpRequest object containing user/session info 
    
    Returns:
        Cart: The retrieved or newly created cart instance
    """
    if request.user.is_authenticated:
        # For logged in users: get/create cart tied to user account
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For anonymous users: ensure session exists and get/create cart
        if not request.session.session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

@login_required

def cart_view(request):
    """
    Display the shopping cart page

    Requires authentication. Shows all items in the user's cart with quantities and totals.

    Args: 
        request: HttpRequest object
    
    Returns:
        HttpResponse: Rendered cart template with cart context 
    
    """
    cart = get_or_create_cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required

def add_to_cart(request, product_id):
    """
    Add a product to the cart or increment quantity if already present

    Handles AJAX requests and returns JSON response with updated cart info

    Args:
        request: HttpRequest object
        product_id: ID of the product to add

    Returns:
        JsonResponse: Contains success status and updated cart totals
    
    """
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)
    
    # Get existing cart item or create new one with quantity=1
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    # If item already existed, increment quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    # Return JSON response for AJAX calls
    return JsonResponse({
        'success': True,
        'cart_total': cart.total, # Updated cart total
        'item_count': cart.items.count() #Updated item count
    })
  

@login_required
def remove_from_cart(request, item_id):
    """
    Remove an item completely from the shopping cart

    Args:
        request: HttpRequest object
        item_id: ID of the CartItem to remove
    
    Returns:
        HttpResponseRedirect: Redirects back to cart page
    
    """
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart:cart')

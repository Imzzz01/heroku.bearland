from django.shortcuts import render
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from cart.models import Cart
from .models import Order, OrderItem
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_view(request):
    cart = get_or_create_cart(request)
    
    if request.method == 'POST':
        intent = stripe.PaymentIntent.create(
            amount=int(cart.total * 100),
            currency='gdp',
            metadata={'card_id' : cart.id}
        )

        order = Order
from django.shortcuts import render
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from cart.models import Cart
from .models import Order, OrderItem
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from cart.models import Cart
from .models import Order, OrderItem
from cart.views import get_or_create_cart

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_view(request):
    cart = get_or_create_cart(request)
    
    if request.method == 'POST':
        intent = stripe.PaymentIntent.create(
            amount=int(cart.total * 100),
            currency='gbp',
            metadata={'cart_id': cart.id}
        )

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key if not request.user.is_authenticated else None,
            cart=cart,
            stripe_payment_intent=intent.id,
            amount=cart.total,
            status='pending'
        )

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        return render(request, 'checkout/checkout.html', {
            'client_secret': intent.client_secret,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
            'order': order,
        })
    
    return render(request, 'checkout/checkout.html', {'cart': cart})

def payment_success(request):
    payment_intent = request.GET.get('payment_intent')
    if payment_intent:
        try:
            order = Order.objects.get(stripe_payment_intent=payment_intent)
            order.status = 'completed'
            order.save()

            cart = order.cart
            cart.items.all().delete()

            return render(request, 'checkout/success.html', {'order': order})
        except Order.DoesNotExist:
            pass
    return redirect('home')

def payment_cancel(request):
    return render(request, 'checkout/cancel.html')
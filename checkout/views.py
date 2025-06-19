import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect 
from cart.views import get_or_create_cart
from django.core.mail import send_mail
from django.template.loader import render_to_string

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout_view(request):
    cart = get_or_create_cart(request)
    
    if cart.items.count() == 0:
        return redirect('cart:cart')

    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user=request.user,
            total=cart.total,
            status='pending'
        )
        
        # Create order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': f'Order #{order.id}',
                        },
                        'unit_amount': int(order.total * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('checkout:success')
                ) + f'?session_id={{CHECKOUT_SESSION_ID}}',
                cancel_url=request.build_absolute_uri(
                    reverse('checkout:cancel')
                ),
                metadata={
                    'order_id': order.id
                }
            )
            return redirect(checkout_session.url)
        except Exception as e:
            print(f"Error creating Stripe session: {e}")
            return redirect('checkout:cancel')

    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

def payment_success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            order = Order.objects.get(id=session.metadata['order_id'])
            
            # Send confirmation email
            subject = f"Order Confirmation #{order.id}"
            html_message = render_to_string('checkout/order_confirmation_email.html', {
                'order': order
            })
            plain_message = f"Thank you for your order #{order.id}. Total: £{order.total}"
            
            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [order.user.email],
                html_message=html_message,
                fail_silently=False
            )
            
            return render(request, 'checkout/success.html', {'order': order})
        except Exception as e:
            print(f"Error processing success: {e}")
    
    return redirect('store:home')
def payment_cancel(request):
    return render(request, 'checkout/cancel.html')
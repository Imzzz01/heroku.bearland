import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.db import transaction
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from cart.views import get_or_create_cart
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
import logging

stripe.api_key = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)

@login_required
def checkout_view(request):
    cart = get_or_create_cart(request)
    
    if cart.items.count() == 0:
        messages.warning(request, "Your cart is empty")
        return redirect('store:products')

    if request.method == 'POST':
        try:
            # Use transaction.atomic to ensure data consistency
            with transaction.atomic():
                order = Order.objects.create(
                    user=request.user,
                    total=cart.total,
                    status='pending'
                )
                
                for item in cart.items.all():
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        quantity=item.quantity,
                        price=item.product.price
                    )

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
                        'order_id': str(order.id)  # Ensure order_id is string
                    }
                )
                return redirect(checkout_session.url)
                
        except stripe.error.StripeError as e:
            logger.error(f"Stripe error during checkout: {str(e)}")
            messages.error(request, "Payment processing error. Please try again.")
        except Exception as e:
            logger.error(f"Unexpected error during checkout: {str(e)}")
            messages.error(request, "An unexpected error occurred. Please contact support.")
        
        return redirect('checkout:checkout')

    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

def payment_success(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        messages.error(request, "Invalid session")
        return redirect('store:home')

    try:
        session = stripe.checkout.Session.retrieve(session_id)
        order = get_object_or_404(Order, id=session.metadata['order_id'])
        
        # Update order status
        order.status = 'completed'
        order.save()
        
        # Clear the cart
        cart = get_or_create_cart(request)
        cart.items.all().delete()
        
        # Send confirmation email
        try:
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
        except Exception as e:
            logger.error(f"Failed to send confirmation email: {str(e)}")
            # Don't fail the whole process if email fails
        
        return render(request, 'checkout/success.html', {'order': order})
        
    except stripe.error.StripeError as e:
        logger.error(f"Stripe error in payment_success: {str(e)}")
        messages.error(request, "Payment verification failed. Please contact support.")
    except Exception as e:
        logger.error(f"Unexpected error in payment_success: {str(e)}")
        messages.error(request, "Order processing error. Please contact support.")
    
    return redirect('store:home')

def payment_cancel(request):
    messages.info(request, "Your payment was cancelled. You can try again.")
    return render(request, 'checkout/cancel.html')
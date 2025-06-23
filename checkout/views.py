from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
import stripe
import logging
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from cart.views import get_or_create_cart
from django.conf import settings

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
            with transaction.atomic():
                # Create order
                order = Order.objects.create(
                    user=request.user,
                    cart=cart,
                    amount=cart.total,
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

                # Create Stripe checkout session
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=[{
                        'price_data': {
                            'currency': 'gbp',
                            'product_data': {
                                'name': f'Order #{order.id}',
                            },
                            'unit_amount': int(order.amount * 100),
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
                        'order_id': str(order.id)
                    }
                )
                return redirect(checkout_session.url)
                
        except Exception as e:
            logger.error(f"Error during checkout: {str(e)}")
            messages.error(request, "There was an error processing your order. Please try again.")
            return redirect('cart:cart')

    # GET request - show checkout page (KEY FIX: Pass stripe_publishable_key)
    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY  # <-- Critical fix
    })

def payment_success(request):
    """Handle successful payment completion"""
    session_id = request.GET.get('session_id')
    if not session_id:
        messages.error(request, "Invalid session")
        return redirect('store:home')

    try:
        # Retrieve Stripe session
        session = stripe.checkout.Session.retrieve(session_id)
        order_id = session.metadata.get('order_id')
        
        if not order_id:
            raise ValueError("No order_id in session metadata")
        
        # Get and update order
        order = get_object_or_404(Order, id=order_id)
        order.status = 'completed'
        order.stripe_payment_intent = session.payment_intent
        order.save()
        
        # Clear the cart
        cart = get_or_create_cart(request)
        cart.items.all().delete()
        
        # Send confirmation email
        send_order_confirmation(order)
        
        # Render success page
        return render(request, 'checkout/success.html', {
            'order': order,
            'order_items': order.items.all()
        })
        
    except stripe.error.StripeError as e:
        logger.error(f"Stripe error in payment_success: {str(e)}")
        messages.error(request, "Payment verification failed. Please contact support.")
    except Order.DoesNotExist:
        logger.error(f"Order not found for session {session_id}")
        messages.error(request, "Order not found. Please contact support.")
    except Exception as e:
        logger.error(f"Unexpected error in payment_success: {str(e)}")
        messages.error(request, "Order processing error. Please contact support.")
    
    return redirect('store:home')

def payment_cancel(request):
    """Handle payment cancellation"""
    messages.info(request, "Your payment was cancelled. You can try again.")
    return render(request, 'checkout/cancel.html')

def send_order_confirmation(order):
    """Send order confirmation email to customer"""
    try:
        subject = f"Order Confirmation #{order.id}"
        html_message = render_to_string('checkout/order_confirmation_email.html', {
            'order': order
        })
        plain_message = f"""Thank you for your order #{order.id} from Bear Land.
        
        Order Total: £{order.amount}
        
        We'll notify you when your items ship. If you have any questions, please contact our support team.
        """
        
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [order.user.email],
            html_message=html_message,
            fail_silently=False
        )
        logger.info(f"Order confirmation email sent for order #{order.id}")
    except Exception as e:
        logger.error(f"Failed to send order confirmation email for order #{order.id}: {str(e)}")
        if settings.DEBUG:
            raise

def stripe_webhook(request):
    """Handle Stripe webhook notifications"""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, 
            sig_header, 
            settings.STRIPE_ENDPOINT_SECRET
        )
    except ValueError as e:
        logger.error(f"Invalid payload: {str(e)}")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"Invalid signature: {str(e)}")
        return HttpResponse(status=400)

    # Handle successful payment
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        try:
            order_id = session.metadata.get('order_id')
            if not order_id:
                raise ValueError("No order_id in session metadata")
            
            order = Order.objects.get(id=order_id)
            
            # Only process if order is still pending
            if order.status == 'pending':
                order.status = 'completed'
                order.stripe_payment_intent = session.payment_intent
                order.save()
                
                # Send confirmation email
                send_order_confirmation(order)
                
                logger.info(f"Order {order_id} completed via webhook")
            else:
                logger.info(f"Order {order_id} was already completed")
                
        except Order.DoesNotExist:
            logger.error(f"Order not found: {order_id}")
        except Exception as e:
            logger.error(f"Error processing order {order_id}: {str(e)}")

    return HttpResponse(status=200)
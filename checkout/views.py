from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import stripe
from django.conf import settings
from cart.models import Cart
from .models import Order, OrderItem
from cart.views import get_or_create_cart
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout_view(request): # Checkout view for logged-in users
    cart = get_or_create_cart(request)
# Check if the cart is empty
    if cart.items.count() == 0:
        return redirect('cart:cart')

        if request.method == 'POST':
         order = Order.objects.create(
            user=request.user,
            total=cart.total,
            status='pending',
         )

         for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
# Clear the cart after creating the order
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': 'Bear Land Order',
                        },
                        'unit_amount': int(order.total * 100),
                    },
                    'quantity': 1,
                } 
                ],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('checkout:success')
                 ) + f'?session_id={{CHECKOUT_SESSION_ID}}',
                 cancel_url=request.build_absolute_uri(
                    reverse('checkout:cancel')
                ),
                metadata={
                    'order_id': order.id,
                }
            )
            return redirect(checkout_session.url)
        except Exception as e:
            print(e)
            return redirect('checkout:cancel')
    return render(request, 'checkout/checkout.html', {
        'cart': cart,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        })

def payment_success(request):
        session_id = request.GET.get('session_id')
        if session_id:
            try:
                session = stripe.checkout.Session.retrieve(session_id)
                order = Order.objects.get(id=session.metadata['order_id'])
               
               #clear the cart items after successful payment

                cart = order.cart
                cart.items.all().delete()

                return render(request, 'checkout/success.html', {'order': order})
            except (Order.DoesNotExist, stripe.error.StripeError):
                pass

                return redirect('home')

def payment_cancel(request):
        return render(request, 'checkout/cancel.html')

 # Stripe webhook to handle payment events
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        fulfill_order(session)

    return HttpResponse(status=200)

# Function to fulfill the order after payment is successful
def fulfill_order(session):
    order_id = session.metadata.get('order_id')
    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'completed'
            order.save()
            
        except Order.DoesNotExist:
            pass       
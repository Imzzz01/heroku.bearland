import stripe
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Order
from django.core.mail import send_mail
from django.template.loader import render_to_string

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
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

def fulfill_order(session):
    order_id = session['metadata']['order_id']
    order = Order.objects.get(id=order_id)
    order.status = 'completed'
    order.save()
    
    # Send confirmation email
    send_order_confirmation(order)

def send_order_confirmation(order):
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
        html_message=html_message
    )
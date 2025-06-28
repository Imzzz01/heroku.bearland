import logging
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Order
from django.core.mail import send_mail
from django.template.loader import render_to_string

logger = logging.getLogger(__name__) # Create logger instance
stripe.api_key = settings.STRIPE_SECRET_KEY # Set stripe secret key from django settings

@csrf_exempt # Disable CSRF protection for this view
def stripe_webhook(request):
    """
    Handle Stripe webhook events
    
    Args:
        request: HttpRequest object containing Stripe webhook payload

    Returns: 
        HttpResponse: Appropriate HTTP status code for each scenario
    
    """
    payload = request.body #Raw webhook payload
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE') # Get signature header

    try:
        # verify and construct Stripe event from payload
        event = stripe.Webhook.construct_event(
            payload, 
            sig_header, 
            settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Handle invalid payload 
        logger.error(f"Invalid payload: {e}")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Handle invalid signature
        logger.error(f"Invalid signature: {e}")
        return HttpResponse(status=400)

    # Handle successful payment
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object'] # Get checkout session data
        logger.info(f"Processing completed checkout session: {session.id}")
        
        try:
            # Verify the payment was actually successful
            if session.payment_status != 'paid':
                logger.warning(f"Unpaid session: {session.id}")
                return HttpResponse(status=200)
                
            # Update order status in database
            order = Order.objects.get(id=session.metadata.order_id)
            order.status = 'completed'
            order.stripe_payment_intent = session.payment_intent
            order.save()
            
            # Send order confirmation email 
            send_order_confirmation(order)
            
            logger.info(f"Successfully processed order {order.id}")
            return HttpResponse(status=200)
            
        except Order.DoesNotExist:
            # Handle case where order doesn't exist in our database
            logger.error(f"Order not found: {session.metadata.get('order_id')}")
            return HttpResponse(status=404)
        except Exception as e:
            logger.error(f"Error processing order: {str(e)}", exc_info=True)
            return HttpResponse(status=500)
    # Return success for unhandled event types
    return HttpResponse(status=200)

def send_order_confirmation(order):
    """
    Send order confirmation email to customer
    
    Args: 
        order: Order object containing purchase details
    
    Returns:
        None (but logs success/error messages )
    """
    try:
        # Prepare email content
        subject = f"Order Confirmation #{order.id}"
        context = {
            'order': order,
            'items': order.items.all(),
            'total': order.total
        }
        # Render both HTML and plain text versions of email
        html_message = render_to_string('emails/order_confirmation.html', context)
        plain_message = render_to_string('emails/order_confirmation.txt', context)
        
        # Send email using django's mail system
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[order.user.email],
            html_message=html_message,
            fail_silently=False # Raise exception if sending fails
        )
        logger.info(f"Sent confirmation for order {order.id} to {order.user.email}")
        # Log any email sending errors 
    except Exception as e:
        logger.error(f"Failed to send confirmation for order {order.id}: {str(e)}", exc_info=True)
       
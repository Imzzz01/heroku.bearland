from django.urls import path
from . import views
from .webhooks import stripe_webhook

app_name = 'checkout'

urlpatterns = [ 
    path('', views.checkout_view, name='checkout'), # Main checkout page
    path('success/', views.payment_success, name='success'), # Payment success page
    path('cancel/', views.payment_cancel, name='cancel'), # Payment cancellation page
   path('webhook/', stripe_webhook, name='webhook'),
]
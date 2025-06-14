from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [ 
    path('', views.checkout_view, name='checkout'),
    path('success/', views.payment_success, name='success'),
    path('cancel/', views.payment_cancel, name='cancel'),
    path('webhook/', views.stripe_webhook, name='stripe-webhook'),
]
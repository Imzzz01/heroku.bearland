from django.db import models
from django.conf import settings
from cart.models import Cart
from store.models import Product  # Make sure to import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order {self.id}"

    @property
    def total(self):
        """Calculate total from order items or return stored amount"""
        if hasattr(self, 'items'):
            return sum(item.price * item.quantity for item in self.items.all())
        return self.amount

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
from django.db import models
from django.conf import settings
from cart.models import Cart
from store.models import Product  # Make sure to import Product

class Order(models.Model):
    """
    Represents a customer order in the system

    Attributes:
         user (ForeignKey): User who placed the order 
         session_key (CharField): session identifier for guest orders
         cart ( ForeignKey): Cart associated with this order
         stripe_payment_intent (CharField): Stripe payment intent ID
         amount (DecimalField): Total order amount (stored as backup)
         created_at (DateTimeField): When order was created (auto-set)
         updated_at (DateTimeField): When order was last updated (auto-updated)
         status (CharField): Current order status (default: 'Pending')
    """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        """String representation of the order"""
        return f"Order {self.id}"

    @property
    def total(self):
        """
        Calculate total from order items or return stored amount
        
        Returns: 
            Decimal: Total value of the order
        """
        if hasattr(self, 'items'):
            # Calculate from order items if they exist
            return sum(item.price * item.quantity for item in self.items.all())
        return self.amount # Fallback to stored amount

class OrderItem(models.Model):
    """
    Represents an individual product items within an order

    Attributes:
        order (ForeignKey): Parent order
        product (ForeignKey): Product being ordered
        quantity (PositiveIntegerField): Quantity ordered (minimum 1)
        price (DecimalField): Price at time of ordering
         
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        """String representation of order item"""
        return f"{self.quantity} x {self.product.name}"
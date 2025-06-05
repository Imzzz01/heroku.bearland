from django.db import models
from django.conf import settings
from store.models import Product
# Create your models here.

class cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)  # For anonymous users
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"cart {self.id}"
class CartItem(models.Model):
    cart = models.ForeignKey(cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

     @property
     def subtotal(self):
         return self.product.price * self.quantity
     def __str__(self):
            return f"{self.quantity} x {self.product.name}"
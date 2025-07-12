from decimal import Decimal
from django.db import models
from django.conf import settings
from store.models import Product

# cart/models.py
# This file defines the Cart and CartItem models for managing shopping carts in an e-commerce application


class Cart(models.Model):
      """
      Represents a shopping cart that can be associated with: 
      - A registered user (if authenticated)
      - A session key (for anonymous users)

      Attributes:
          user: Authenticated user owner
          session_key: Identifier for anonymous users
          created_at: When cart was created
          updated_at: When cart was last modified 

      """
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,   blank=True)
      session_key = models.CharField(max_length=40, null=True, blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      @property
      def total(self):
        """Calculate total value of all items in cart including shipping"""
        item_total = sum(item.subtotal for item in self.items.all())
        shipping = Decimal('5.00')
        return item_total + shipping

      def __str__(self):
        return f"Cart {self.id}"
# cart/models.py
# This file defines the CartItem model for items in a shopping cart

class CartItem(models.Model):
      """
      Represents an individual product item within a shopping cart

      Attributes:
           cart: Parent cart this item belongs to
           product: Product being added to cart
           quantity: Number of units (minimum 1)

      """

      cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
      product =  models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity =  models.PositiveIntegerField(default=1)
 
      @property
      def subtotal(self):
          """Calculate line total (price × quantity)"""
          return self.product.price * self.quantity
      def __str__(self):
          """String representation of cart item"""
          return f"{self.quantity} x {self.product.name}"
     

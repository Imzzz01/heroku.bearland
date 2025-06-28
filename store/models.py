from django.db import models
from django.urls import reverse

class Product(models.Model):
    """
    Base model representing a product in the store 
    
    Attributes:
        name: Product name (max 100 chars)
        description: Detailed product description
        price: Product price (max 10 digits, 2 decimal places)
        image: Product image (optional) 
        stock: Available quantity
        created_at: Timestamp when product was created 
        updated_at: Timestamp when product was last updated
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the product (returns product name)"""
        return self.name
        
    def get_absolute_url(self):
        """Returns URL for product detail view"""
        return reverse('product_detail', args=[str(self.id)])

class Gift(Product):
    """
    Model representing gift products (inherits from Product)
    
    Additional Attributes:
        is_gift: Flag indicating this is a gift product 
        gift_type: Category/type of gift (optional)
    """
    is_gift = models.BooleanField(default=True)
    gift_type = models.CharField(max_length=50, blank=True, null=True)

class Category(models.Model):
    """
    Model for product categories
    
    Attributes: 
        name: Category name (max 100 chars)
        slug: URL-friendly version of name (unique)
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        """String representation of the category (returns category name)"""
        return self.name
    
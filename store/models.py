from django.db import models
from django.urls import reverse

class Product (models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     price = models.DecimalField(max_digits=10, decimal_places=2)
     image = models.ImageField(upload_to='products/', blank=True, null=True)
     stock = models.PositiveIntegerField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
         return self.name
     def get_absolute_url(self):
         return reverse('product_detail', args=[str(self.id)])

class Gift(Product):
      is_gift = models.BooleanField(default=True)
      gift_type = models.CharField(max_length=50, blank=True, null=True)

class Category(models.Model):
      name = models.CharField(max_length=100)
      slug = models.SlugField(unique=True)

      def __str__(self):
        return self.name

    
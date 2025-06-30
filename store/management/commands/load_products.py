import os
from django.core.management.base import BaseCommand
from django.core.files import File
from store.models import Product, Gift

class Command(BaseCommand):
    help = 'Load products with proper image handling'

    def handle(self, *args, **options):
        # First clear existing products to avoid duplicates
        Product.objects.all().delete()
        
        # Your existing product data...
        products = [
            # ... (keep your existing product data)
        ]
        
        for product_data in products:
            # Create product without image first
            product = Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                stock=product_data['stock']
            )
            
            # Handle image from static folder
            static_image_path = os.path.join('static/images/store', product_data['image'])
            if os.path.exists(static_image_path):
                with open(static_image_path, 'rb') as f:
                    # This will save to media/products/ with Django's default naming
                    product.image.save(product_data['image'], File(f))
                    self.stdout.write(f"Saved image for {product.name} to {product.image.url}")
            else:
                self.stdout.write(self.style.WARNING(f'Image not found: {static_image_path}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(products)} products'))
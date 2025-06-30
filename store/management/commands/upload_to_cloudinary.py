from django.core.management.base import BaseCommand
from django.conf import settings
import os
import cloudinary
import cloudinary.uploader
from store.models import Product

class Command(BaseCommand):
    help = 'Uploads product images to Cloudinary'

    def handle(self, *args, **options):
        # Configure Cloudinary from CLOUDINARY_STORAGE settings
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret=settings.CLOUDINARY_STORAGE['API_SECRET'],
            secure=True
        )

        products = Product.objects.exclude(image__isnull=True).exclude(image__exact='')

        for product in products:
            try:
                local_path = os.path.join(settings.MEDIA_ROOT, product.image.name)
                
                if os.path.exists(local_path):
                    result = cloudinary.uploader.upload(
                        local_path,
                        public_id=f"products/{product.id}",
                        folder="bearland"
                    )
                    product.image = result['secure_url']
                    product.save()
                    self.stdout.write(self.style.SUCCESS(f'Uploaded {product.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Missing image: {product.name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error uploading {product.name}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Finished uploading images'))
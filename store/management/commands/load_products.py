import os
from django.core.management.base import BaseCommand
from django.core.files import File
from store.models import Product, Gift

class Command(BaseCommand):
    help = 'Load all products and gifts into the database with template-matching descriptions'

    def handle(self, *args, **options):
       
        products = [
            {
        'name': 'Brown Bear',
        'description': 'Adopt a brown bear today!',
        'price': 12.00,
        'stock': 50,
        'image': 'brownbear.jpg'
    },
         {
        'name': 'Pink Bear',
        'description': 'Adopt a Pink bear today!',
        'price': 13.00,
        'stock': 40,
        'image': 'pink-bear.jpg'
    },
    {
        'name': 'Brown bear with bow',
        'description': 'Adopt a cute bear today!',
        'price': 12.00,
        'stock': 35,
        'image': 'bowbear.jpg'
    },
    {
        'name': 'Blue Bear',
        'description': 'Adopt a Blue bear today!',
        'price': 14.00,
        'stock': 30,
        'image': 'bluebear.jpg'
    },
    {
        'name': 'White Bear',
        'description': 'Adopt a White bear today!',
        'price': 15.00,
        'stock': 25,
        'image': 'white-bear.jpg'
    },
    {
        'name': 'Grey Bear',
        'description': 'Adopt a Grey bear today!',
        'price': 16.00,
        'stock': 20,
        'image': 'greybear.jpg'
    },
    {
        'name': 'Yellow Bear',
        'description': 'Adopt a Yellow bear today!',
        'price': 17.00,
        'stock': 15,
        'image': 'yellowbear.jpg'
    },
    {
        'name': 'Green Bear',
        'description': 'Adopt a Green bear today!',
        'price': 18.00,
        'stock': 10,
        'image': 'greenbear.jpg'
    },
    {
        'name': 'Purple Bear',
        'description': 'Adopt a Purple bear today!',
        'price': 19.00,
        'stock': 8,
        'image': 'purplebear.jpg'
    },
    {
        'name': 'Orange Bear',
        'description': 'Adopt an Orange bear today!',
        'price': 20.00,
        'stock': 5,
        'image': 'orangebear.jpg'
    },
    {
        'name': 'Red Bear',
        'description': 'Adopt a red bear today!',
        'price': 22.00,
        'stock': 12,
        'image': 'redbear.jpg'
    }

        ]

        gifts = [
            {
        'name': 'Rose Bear Gift',
        'description': 'A romantic gift with a beautiful rose - perfect for someone special!',
        'price': 25.00,
        'stock': 30,
        'image': 'rosybear.jpg',
        'gift_type': 'Romantic'
 },
             {
        'name': 'Bear Necklace',
        'description': 'Adorable bear-themed jewelry for bear lovers!',
        'price': 18.00,
        'stock': 25,
        'image': 'bearnecklace.jpg',
        'gift_type': 'Jewelry'
    },
    {
        'name': 'Bear Keychain',
        'description': 'Cute bear keychain to keep your favorite bear with you always!',
        'price': 8.00,
        'stock': 50,
        'image': 'bearkeychain.jpg',
        'gift_type': 'Accessory'
    },
    {
        'name': 'Wedding Bear Gift',
        'description': 'Perfect wedding gift for the happy couple!',
        'price': 35.00,
        'stock': 15,
        'image': 'teddygift.jpg',
        'gift_type': 'Wedding'
    },
    {
        'name': 'Bear Chocolates',
        'description': 'Delicious bear-shaped chocolates for sweet moments!',
        'price': 15.00,
        'stock': 40,
        'image': 'chocolates.jpg',
        'gift_type': 'Edible'
    },
    {
        'name': 'Teddy Bear Bouquet',
        'description': 'A beautiful bouquet of mini teddy bears - unique and adorable!',
        'price': 28.00,
        'stock': 20,
        'image': 'teddybouquet.jpg',
        'gift_type': 'Decorative'
    },
    {
        'name': 'Valentine Gift Set',
        'description': 'Complete Valentine\'s gift set with bear and treats!',
        'price': 32.00,
        'stock': 18,
        'image': 'valentinegift.jpg',
        'gift_type': 'Romantic'
    },
    {
        'name': 'Gift Box Bears',
        'description': 'Beautifully packaged mini bears in elegant gift boxes!',
        'price': 22.00,
        'stock': 25,
        'image': 'giftboxbears.jpg',
        'gift_type': 'Decorative'
    },
    {
        'name': 'Special Occasion Bear',
        'description': 'Perfect for birthdays, anniversaries, and special celebrations!',
        'price': 30.00,
        'stock': 22,
        'image': 'specialoccasion.jpg',
        'gift_type': 'Celebration'
    }
]
        

        # Add all products
        for product_data in products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock']
                }
            )
            
            # Add image if it doesn't exist
            if not product.image and 'image' in product_data:
                image_path = os.path.join('static/images/store', product_data['image'])
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        product.image.save(product_data['image'], File(f))
                        product.save()
                else:
                    self.stdout.write(self.style.WARNING(f'Image not found: {image_path}'))

        # Add all gifts
        for gift_data in gifts:
            gift, created = Gift.objects.get_or_create(
                name=gift_data['name'],
                defaults={
                    'description': gift_data['description'],
                    'price': gift_data['price'],
                    'stock': gift_data['stock'],
                    'gift_type': gift_data['gift_type']
                }
            )
            
            # Add image if it doesn't exist
            if not gift.image and 'image' in gift_data:
                image_path = os.path.join('static/images/store', gift_data['image'])
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        gift.image.save(gift_data['image'], File(f))
                        gift.save()
                else:
                    self.stdout.write(self.style.WARNING(f'Image not found: {image_path}'))

        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {len(products)} products and {len(gifts)} gifts '
            'with template-matching descriptions'
        ))
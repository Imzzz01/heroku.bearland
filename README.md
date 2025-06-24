# 🐻 Bear Land - Premium Teddy Bear Emporium 🎀

## Table of Contents

- [Purpose of Project](#purpose)
- [UX Design](#ux-design)
- [Key Features](#key-features)
- [Target Audience](#target-audience)
- [Data Models](#data-models)
- [User Stories](#user-stories)
- [Design Rationale](#design-rationale)
- [Features and Functionalities](#features)
- [Technologies used](#technologies)
- [Future Enhancements](#future-enhancements)
- [Test Plan](#test-plan)
- [Internal and External Code](#internal-and-external-code)
- [Commit Messages](#commit-messages)
- [Validation](#validation)
- [Finished Project](#finished-project)
- [Deployment](#deployment)



## 🚀 Project Purpose <a id="project-purpose"></a>

Bear Land aims to introduce teddy bear lovers to our unique eCommerce platform. You'll find a wide selection of soft, adorable, and colourful teddy bears here. We aim to evoke the joy of childhood and the appeal of owning teddy bears, a sentiment that transcends age. As adults, we all appreciate the comfort these bears provide, and their positive impact on our mental health is undeniable.

Key objectives:

- Provide a delightful shopping experience for teddy bear enthusiasts
- Offer unique, high-quality products that evoke nostalgia and comfort
- Create an intuitive platform for gift shopping and collectable purchases.

## 🎨 UX Design <a id="UX-design"></a>  
Color scheme:

- Primary: #8B4513 (SaddleBrown)
- Secondary:#D2691E (Chocolate)
- Accent: #FFB6C1 (light pink)
- Background: #FFF8DC (Cornsilk)

Typography: 

- Primary font: 'Inter' (Modern sans-serif)
- Fallback: System UI fonts

Design Principles: 
- Warm, inviting aesthetic with bear-themed elements
- Responsive layout for all device sizes
- Intuitive navigation with clear CTAs
- Emotional connection through imagery and product presentation

## 🌟 Key Features <a id="key-features"></a>

- Product catalogue: Browse our extensive collection of teddy bears
- Gift Section: Curated bear-themed gifts for special occasions
- User Accounts: Secure Registration and login system
- Shopping Cart: Persistent cart functionality
- Checkout: Secure Stripe payment integration
- Search: Find products quickly with our search functionality


## 👥 Target Audience <a id="target-audience"></a>
### Primary Segments

1.  **Gift Shoppers** (Age 23 - 40)
   - Seeking unique presents for birthdays, anniversaries, and holidays.
   - Value convenience + personalised options
  
2.  **Collectors** (Age 20 - 60)
   - Teddy bear enthusiasts seeking limited editions
   - Interested in artist collaborations and certificates of authenticity

3.  **Parents/Grandparents** (Age 30 - 65)
   - Looking for heirloom-quality stuffed animals
   - Prioritise safety certifications and durability

4.  **Children** (Age 1 - 10)
   - Drawn to colourful, soft and cuddly bears
   - Prefer bears with friendly faces and tactile features

5.  **Teens/Adults** (Age 11-19 & 18+)
   - Nostalgic buyers reconnecting with childhood
   - Seek bears as decorative items or comfort objects



## 📖 User Stories <a id="user-stories"></a>

| **As a...**         | **I Want To**                    |        **So That**                | **Priority**   |
|---------------------|---------------------------       |--------------------------------   |----------------|
| First-time visitor  | Browse curated collections       | I can quickly find suitable gifts | High           | 
| Registred user      | Save multiple shipping addresses | I don't need to re-enter info     | Medium         | 
| Mobile User         | Easy view product details        | I can shop on the go              | High           | 

# Technologies <a id="technologies"></a>

**Frontend**
- HTML5, CSS3, Javascript
- Bootstrap 5.3
- Font Awesome 6
- jQuery 3.7
- AOS (Animate On Scroll)

**Backend**
- Python 3
- Django 5.1
- PostgreSQL (Production)
- SQLite (Development)

**Services**
- Stripe (payments)
- Heroku (Hosting)

## 🎨 Design Rationale <a id="design-rationale"></a>

The design emphasises warmth and nostalgia with:

- Earthy brown colour palette reminiscent of classic teddy bears
- Soft pink accents for a playful touch
- Ample white space to prevent visual clutter
- Large product images to showcase details
- Animated transitions for delightful interactions.
  
# Features and Functionalities<a id="features"></a>

## Current Features
1. Responsive Product Grid
    - Filterable by category
    - Detailed product pages
    - Related product suggestions

2. Shopping Cart
   - Persistent across sessions
   - Quantity adjustment
   - Real-time total calculation

3. User Authentication
   - Custom User Model
   - Social auth integration
  
 4. Checkout process
   - Multi-step form
   - Stripe Payment integration
   - Order confirmation emails.

## Future Features

- Wishlist functionality
- Product reviews and ratings
- Subscription service for collectors

## 🧪 Test Plan <a id="test-plan"></a>

# 1. Introduction

1.1 Purpose 

This document outlines the test strategy for Bear Land, a teddy bear e-commerce website built with Django. The goal is to ensure that all features work as expected across different scenarios.

1.2 Scope

Testing will cover:

- User authentication and accounts
- Product browsing and search
- Shopping cart functionality
- Checkout and payment processing
- Responsive design across devices

# 2. Test Approach 

2.1 Test Types 

- Functional Testing: Verify all features work as specified
- UI Testing: Check visual elements and responsiveness
- Integration Testing: Test interactions between components
- Security Testing: Validate authentication and data protection
- Performance Testing: Assess loading times under load

# 2.2 Test Environment
- Frontend: Chrome, Firefox, Safari, Edge (Latest version)
- Mobile: iOS and Android devices
- Backend: Django 5.1.6 with SQLite (Development), PostgreSQL (production)

## 3. Test Cases

ID: AUTH-01: User Registration

Steps:

1. Navigate to /accounts/register
2. Fill in required/valid input e.g (Full name, Last name, Email, Password, confirm password)
3. Submit the form

Expected:
✔️Account Created.
✔️Redirected to Homepage.
✔️If customer uses an existing name, email or password. It will pass a message "This email is already in use." or The password is too similar to the last name.

AUTH-02: login(Invalid Credentials)

Steps:

1. Enter Incorrect email/password
2. Click "login"

Expected:

✔️Error message displayed.
✔️No account created.

Product Browsing

PROD-01:Product Search

Steps:

1. Search for "bear", or use keywords like "cute".
2. Submit Query

Expected:

✔️Search Results for "bear"
✔️Found 20 results for your search
✔️No results for invalid queries.

PROD-02: Product Details Page

Steps:
1. Go on product section and click on view details for any product.

Expected:

✔️Displays Price, Quantity, Description and stock status.
✔️Shows 3 Related products.

Shoppinng Cart

CART-01: Add Item to cart

Steps:
1. Click "Add to cart" on a product
2. Vist /cart/

Expected:

✔️Item appears with correct price
✔️Cart total updates

CART-02: Remove Item

Steps:
1. Remove an item from cart

Expected:

✔️Item Removed
✔️For 2 items in cart, the total will recalculate
✔️or 1 item in cart, the total will go back to £0.00 + Shipping fee £5

Checkout Process

CHECK-01: Successful Payment

Steps:
1. Proceed to checkout
2. Complete stripe payment

Expected:
✔️Order Marked "Payment Successful"
❌Confirmation Email sent

CHECK-02: Payment cancellation

Steps:
1. Cancel during payment

Expected:
✔️Redirects to cancel page
✔️Order status = "Cancelled".

Responsive Design

RD-01: Mobile View (320px)

Steps:
1. Resize to mobile width

Expected:
✔️Navbar collapses
✔️Text/images scale properly

RD-02: Desktop View (1200px)

Steps:
1. View on Full-Screen

Expected:
✔️No layout overflow
✔️Consistent spacing

Test Reporting: Identified Issues

1. Critical Bug: Payment Confirmation Email Failure

Description:

- After successful stripe payment, the system processes the order but fails to send the confirmation email.

Steps:

1. Complete checkout with test payment
2. Check:
  - Database(order status = "completed")
  - Email inbox (no confirmation recieved)
  - Server logs(no SMTP errors)

Expected Behavior:
Email sent to user with order details(template: order_confirmation_email.html)

Actual behavior:
No email sent, despite payment success.

Severity: High(Impacts user trust and order tracking)

Evidence:

- 

2. UI Bug: Checkout Page Styling Issues

Description:

- The section headings "order summary" and "payment" have poor contrast, while product details and payment remain clearly visible.

Affected Elements:

- Order Summary heading (grey background, with white text)
- Payment heading (grey background, with white text)

Steps to reproduce:
1. Go to /checkout/
2. observe poor text visibility in:
 - order summary card.

Expected Behavior:
Clear contrast (e.g dark text on light background)

Actual Behavior:
Text blends into background(WCAG accessability failure)
Severity: Medium/Low(Impairs usability, but doesn't block functionality)

Evidence:
![image](https://github.com/user-attachments/assets/e8105876-82e8-4601-a751-2ebd973a4719)

## Known Issues and Pending Fixes

### 1. Email Delivery Failure
- **Status**: Investigating
- **Impact**: Users won't receive order confirmations.
- **Workaround**: Manually check "orders" in account dashboard

### 2. Checkout Page Styling
- **Status**: UX fix in progress
- **Impact**: Text readability issues in order summary
- **Temporary Fix**: Browser zoom improves visability

# 4. Test Data

4.1 Test Products 
- 11 sample teddy bear products with varying prices
- 9 gift items with different categories

4.2 Test Users 

# 5. Test Schedule

| Phase       | Duration      |Tasks                                    |
|-------------|---------------|-----------------------------------------|
|Preparation  |  3 days       | Set up test environment, prepare data   |
|Execution    |  6 days       | Run all test cases, document results    |
|Reporting    |  2 days       | Compile test report, log defects        |


# 7. Exit Criteria

Testing will be considered when:
- All critical test cases pass
- No critical defects remain open
- 95% of all test cases pass
- Remaining defects are documented and prioritised.

# 8. Tools
- Automated Testing: Django Test Framework
- Manual Testing: Browser developer tools
- Performance: Chrome
- Security: OWASP ZAP (basic scans)

# 9. Risks

|Risk                         | Mitigation                             |
|-----------------------------|----------------------------------------|
|Payment gateway failures     | Test with Stripe test mode first       |
|Browser compatibility issues | Test early on multiple browsers        |
|Performance under load       | Monitor during peak testing            |


## 🔗 Internal and External Code <a id="internal-and-external-code"></a>
# Core Components 

Custom Business Logic:
- Extended user model with additional profile fields
- Cart Management system supporting both authenticated and guest users
- Order processing workflow with status tracking
- Custom template tags for reusable UI components.

Integration Points:
1. Payment System: Secure Stripe integration handles payment processing with webhook verification.

2. UI Libraries:
   - Bootstrap 5 for responsive layouts and components
   - Font Awesome for iconography
   - Animate on Scroll for scroll-triggered animations

3. Performance Tools:
   - WhiteNoise for static file serving
   - Django compressor for asset optimisation 
     
# Commit messages <a id="commit-messages"></a>
![image](https://github.com/user-attachments/assets/3307a729-4848-46a2-a6ed-9667c6370a86)
![image](https://github.com/user-attachments/assets/dd4b4632-2a50-4679-aef4-84501b135bdb)
![image](https://github.com/user-attachments/assets/fecb8235-0d16-435f-a767-64bbd6464f51)
![image](https://github.com/user-attachments/assets/50885e6d-c361-4d80-a949-11484b620fb2)
![image](https://github.com/user-attachments/assets/19e34342-390c-4963-86ee-2f4fe9ac1f3f)
![image](https://github.com/user-attachments/assets/bfa352d8-285c-4752-91ff-6c8d9a1dc164)
![image](https://github.com/user-attachments/assets/d0eeb8cf-5f3a-43c6-8083-2890b6a1f516)




# Validation <a id="validation"></a>

## View Source HTML Validation:
Home
![image](https://github.com/user-attachments/assets/02c413d5-9bb5-40d6-8fd1-89135d1c6adf)
Products
![image](https://github.com/user-attachments/assets/91a42fa0-799a-47c5-b96d-97355b8623a8)
Gifts
![image](https://github.com/user-attachments/assets/aa4b37e4-f245-4623-ba4f-f2b3dc1f91b3)
Search 
![image](https://github.com/user-attachments/assets/2a7d43f6-a25c-49af-b861-d256d42668eb)
Cart
![image](https://github.com/user-attachments/assets/12a6468a-a640-4d8a-9e04-17022dfa579c)
Login
![image](https://github.com/user-attachments/assets/ea5c8c01-e9ef-49ca-bb07-9aad587d7dc1)
Register
![image](https://github.com/user-attachments/assets/7e8c7f45-c458-41fd-a1cb-61339d3e22fd)




## View Source Style.CSS Validation: 
Store - Style.css
![image](https://github.com/user-attachments/assets/ee2f9f6d-38f1-4cc2-8f5c-97a7f90ccfbc)

Accounts - style.css
![image](https://github.com/user-attachments/assets/9143e710-9139-460b-ad20-8209f67967d3)

Cart - Style.css
![image](https://github.com/user-attachments/assets/bc075bc8-ee38-4edf-bb04-b1627a8c9897)

Checkout - Style.css
![image](https://github.com/user-attachments/assets/73a685ea-a437-4106-85ae-de073613d1cd)

Base.css
![image](https://github.com/user-attachments/assets/6668d477-9e5b-4a57-a1e2-ae86f7166389)


## Finish Project <a id="finished-project"></a>

# Home Page

![image](https://github.com/user-attachments/assets/4fdc61fa-8646-4d2b-a174-eb76e0a5101a)
![image](https://github.com/user-attachments/assets/298eea84-9e8e-4f28-99ce-16e4ad44d9ee)
![image](https://github.com/user-attachments/assets/7a1a7296-9c7a-460b-922a-664d10fbc6dc)


# Product Page 
![image](https://github.com/user-attachments/assets/3cfa030a-df53-45b1-b59f-7d774024a4c6)
![image](https://github.com/user-attachments/assets/945ec97a-2e15-4b31-9cd2-fe4fae9c5d22)
![image](https://github.com/user-attachments/assets/215f053a-5ca1-4b96-980d-5abfb05ba96a)

# Gift Page 
![image](https://github.com/user-attachments/assets/fba6234c-8cee-4a7a-9393-9e52a456903b)
![image](https://github.com/user-attachments/assets/8468d692-e5e7-47ee-93c8-c38bed421388)

# Search Engine / Product & Gift Details
![image](https://github.com/user-attachments/assets/6f230f28-2902-4226-a0ed-3810d4884032)
![image](https://github.com/user-attachments/assets/5b56218e-027a-4b1f-8903-a4b6746cd000)
![image](https://github.com/user-attachments/assets/3c336cb5-49cf-4cbe-aa93-6f7584fe496a)

# Cart / Customer's can only buy products after creating an account and logging in.
![image](https://github.com/user-attachments/assets/0f683972-7486-489a-a020-a3ee1036c2a6)
![image](https://github.com/user-attachments/assets/9a948c19-b121-4bab-aa00-f891d42afd02)

# Checkout

# Stripe Payment / Success Message
![image](https://github.com/user-attachments/assets/c9df3fd2-041b-4cd3-8717-dfab9687275b) With the right information
![image](https://github.com/user-attachments/assets/fd1e5eaf-f5d0-4a54-b88a-e4c5b582274c) With the wrong information
Pay through link which makes it easier for customers to pay quickly just like Apple pay or google pay
![image](https://github.com/user-attachments/assets/a7ccd022-71c9-4e24-a270-246d7c844851)
![image](https://github.com/user-attachments/assets/6752732e-4f5e-41d6-9782-11103117ad26)
Once Payment has been made, it will direct you back to the home page and show you Payment successful message!
![image](https://github.com/user-attachments/assets/331d4d4e-ca72-4a53-a7c8-73a9d6d93a0d)

## Data Models <a id="data-models"></a>

```python
# Store models 

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

# Cart Models

from django.db import models
from django.conf import settings
from store.models import Product


class Cart(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,   blank=True)
     session_key = models.CharField(max_length=40, null=True, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     @property
     def total(self):
          return sum(item.subtotal for item in self.items.all())
     def __str__(self):
          return f"Cart {self.id}"

class CartItem(models.Model):

      cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
      product =  models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity =  models.PositiveIntegerField(default=1)
 
      @property
      def subtotal(self):
          return self.product.price * self.quantity
      def __str__(self):
          return f"{self.quantity} x {self.product.name}"


# Accounts models

from django.contrib.auth.models import AbstractUser
from django.db import models
from store.models import Product

class CustomUser(AbstractUser):
      phone_number = models.CharField(max_length=20, blank=True)
      address = models.TextField(blank=True)

groups = models.ManyToManyField(
      'auth.Group',
       verbose_name='groups',
       blank=True,
       help_text='The group this user belongs to.',
       related_name='customuser_set',
       related_query_name='customuser'
)

user_permissions = models.ManyToManyField(
       'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser'
)

def __str__(self):
         return self.username

# Checkout models

from django.db import models
from django.conf import settings
from cart.models import Cart
from store.models import Product 

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

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"  


## 🚀 Deployment <a id="deployment"></a>

This project is deployed on Heroku with PostgreSQL for production and SQlite for local development. Here are some steps to deploy: 
Heroku Deployment Steps

Required:

- Heroku CLI installed
- Git installed
- A verified Heroku Account
- Stripe account (for payments) install stripe cli 

1. Heroku Setup

Create a heroku app through terminal or through the App

bash 

heroku login -i > if heroku login doesn't work
heroku create your-app-name > # heroku create bearland
heroku addons:create heroku-postgresql:hobby-dev #Free postgresql

Set Environment Variables

Configure required keys in Heroku:

heroku config:set SECRET_KEY='your-django-secret-key'
heroku config:set STRIPE_PUBLIC_KEY='your-stripe-public-key'
heroku config:set STRIPE_SECRET_KEY='your-stripe-key'
heroku config:set STRIPE_WEBHOOK_SECRET='your-stripe-webhook-secret'
heroku config:set EMAIL_HOST_PASS='your-email-password' # This is for order confirmations

2. Django Configuration

Configure settings.py for Production

settings.py

from pathlib import Path
import os
import dj_database_url
from whitenoise import WhiteNoise
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configure Postgres for Heroku
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For production
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files (user-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# WhiteNoise configuration (add this)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

Required Files:

1. Procfile (Heroku)

web: gunicorn bearland.wsgi --log-file - # added my project name 

2. requirements.txt

- Django==5.1.6
- gunicorn==23.0.0
- psycopg2-binary==2.9.10
- python-dotenv==1.1.0
- whitenoise==6.9.0
- django-allauth==65.9.0
- django-crispy-forms==2.4
- crispy-bootstrap5==2025.4
- stripe==12.2.0
- dj-database-url
- Pillow

3. Deploy to Heroku

Push code to heroku

bash 

git add .
git commit -m "Initial deployment setup"
git push heroku main

Run Migrations & Collect Static Files #Important
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput

Optional (Create a superuser)

heroku run python manage.py createsuperuser

5. Post-Deployment Checks
  1. verify live site:
  heroku open
  2. View on the website

2. Check logs for errors:
  heroku logs --tail

3. Test Stripe Payments:
   Use test cards(4242 4242 4242 4242)

Troubleshooting:

Issue: Staticfiles not loading 
Solution: Run heroku run python manage.py collectstatic

Issue: Database connection errors
Solution: Check DATABASE_URL in heroku config

Issue: Stripe webhook failures
Solution: Verify Stripe_webhook_secret in heroku




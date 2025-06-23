# 🐻 Bear Land - Premium Teddy Bear Emporium 🎀

## Table of Contents

- [Purpose of Project](#purpose)
- [UX Design](#ux-design)
- [Target Audience](#target-audience)
- [User Query](#user-query)
- [Features and Functionalities](#features)
- [Technologies used](#technologies)
- [Future Enhancements](#future-enhancements)
- [Design Rationale](#design-rationale)
- [Code Implementation](#code-implementation)
- [Internal and External Code](#internal-and-external-code)
- [Test Plan](#test-plan)
- [Commit Messages](#commit-messages)
- [HTML Validation](#html-validation)
- [Finished Project](#finished-project)
- [Deployment](#deployment)
- [Getting Started](#getting-started)


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

## Data Models 

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

# 3. Test Cases
[https://1drv.ms/w/c/4825e675d30aceda/ESZ0eegzToxGv8gSUPIeVqEB-UO_C1ytDsilXNx6Y3lM0w?e=bG68PV]

# 4. Test Data

4.1 Test Products 
- 10 sample teddy bear products with varying prices
- 5 gift items with different categories

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


# Finish Project <a id="finished-project"></a>




## 🚀 Deployment <a id="deployment"></a>

Heroku Deployment Steps

1. Create a new Heroku app
2. Configure environment variables
3. Set up PostgreSQL add-on
4. Configure static files with WhiteNoise
5. Set up Stripe webhooks

| bash                                        |
|---------------------------------------------|
| git add.                                   |
|---------------------------------------------|
| git commit -m "test1"                       |
|---------------------------------------------|
| git push heroku main                        |
|---------------------------------------------|
| heroku run python manage.py migrate         |
|---------------------------------------------|


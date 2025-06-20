# 🐻 Bear Land - Premium Teddy Bear Emporium 🎀

## Table of Contents
- [UX Design](#ux-design)
- [Purpose of Project](#purpose)
- [Target Audience](#target-audience)
- [User Query](#user-query)
- [Features and Functionalities](#features)
- [Technologies used](#technologies)
- [Future Enhancements](#future-enhancements)
- [Design Rationale](#design-rationale)
- [Code Implementation](#code-implementation)
- [Internal and External Code](#internal-and-external-code)
- [Test Plan](#test-plan)
- [Commit Messages](#internal-and-external-code)
- [HTML Validation](#html-validation)
- [Finished Project](#finished-project)
- [Deployment](#deployment)
- [Getting Started](#getting-started)


## 🚀 Project Purpose <a id="project-purpose"></a>

The goal of Bear Land is to introduce teddy bear lovers to our unique eCommerce platform. Here, you'll find a wide selection of soft, adorable, and colourful teddy bears. Our aim is to evoke the joy of childhood and the appeal of owning teddy bears, a sentiment that transcends age. As adults, we all appreciate the comfort these bears provide, and their positive impact on our mental health is undeniable.

Key objectives:

- Provide a delightful shopping experience for teddy bear enthusiasts
- Offer unique, high qaulity products that evoke nostalgia and comfort
- Create an intuitive platform for gift shopping and collectible purchases.

## 🎨 UX Design <a id="ux-design"></a>  
Color scheme:

- Primary: #8B4513 (SaddleBrown)
- Secondary:#D2691E (Chocolate)
- Accent: #FFB6C1 (lightPink)
- Background: #FFF8DC (Cornsilk)

Typography: 

- Primary font: 'Inter' (Modern sans-serif)
- Fallback: System UI fonts

Design Principles: 
- Warm, inviting aesthetic with bear-themed elements
- Responsive layput for all device sizes
- Intuitive navigation with clear CTAs
- Emotional connection through imagery and product presentation

## 🌟 Key Features <a id="key-features"></a>

- Product catalog: Browse our extensive collection of teddy bears
- Gift Section: Curated bear-themed gifts for special occations
- User Accounts: Secure Registration and login system
- Shopping Cart: Persistent cart functionality
- Checkout: Secure Stripe payment integration
- Search: Find products quickly with our earch functionality


## 👥 Target Audience <a id="target-audience"></a>
### Primary Segments

1.  **Gift Shoppers** (Age 23 - 40)
   - Seeking unique presents for birthdays, aniversaries, and holidays.
   - Value connvenience + personalised options
  
2.  **Collectors** (Age 20 - 60)
   - Teddy bear enthusiasts seeking limited editions
   - Interested in artist collaborations and certificates of authenticity

3.  **Parents/Grandparents** (Age 30 - 65)
   - Looking for heirloom-quality stuffed animals
   - Prioritise safety certifications and durability

4.  **Children** (Age 1 - 10)
   - Drawn to colorful, soft and cuddly bears
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
- Bootsrap 5.3
- Font Awesome 6
- jQuery 3.7
- AOS (Animate On Scroll)

**Backend**
- Python 3
- Django 5.1
- PostgreSQL (Production)
- SQlite (Development)

**Services**
- Stripe (payments)
- Heroku (Hosting)

## 🎨 Design Rationale <a id="design-rationale"></a>

The design emphasizes warmth and nostalgia with:

- Earthy brown color palette reminiscent of classic teddy bears
- Soft pink accents for a playful touch
- Ample white space to prevent visual clutter
- Large product images to showcase details
- Animated transitions for delightful interactions.
  
# Features and Functionalities<a id="features"></a>

## Current Features
1. Responsive Product Grid
    - Filterable by category
    - Detailed product pages
    - Related products suggestions

2. Shopping Cart
   - Persistent across sessions
   - Quantity adjustment
   - Real-time total calculation

3. User Authentication
   - Custom User model
   - Social auth integration
  
 4. Checkout process
   - Multi-step form
   - Stripe Payment integration
   - Order confirmation emails.

## Future Features

- Wishlist functionality
- Product reviews and ratings
- Subcription service for collectors

## 🧪 Test Plan <a id="test-plan"></a>


  

## 🔗 Internal and External Code <a id="internal-and-external-code"></a>
# Core Components 

Custom Business Logic:
- Extended user model with additional profile fields
- Cart Management system supporting both authenticated and guest users
- Order processing workflow with status tracking
- Custom template tags for reusable UI components.

Integration Points:
1. Payment System: Secure Stripe integration handles payment processing with webhook vertification.

2. UI Libraries:
   - Bootsrap 5 for responsive layouts and components
   - Font Awesome for iconography
   - Animate on Scroll for scroll-triggered animations

3. Performance Tools:
   - WhiteNoise for static file serving
   - Django-compressor for asset optimisation 
     

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

1. Create a new heroku app
2. Configure environment variables
3. Set up PostgreSQL add-on
4. Configure static files with WhiteNoise
5. Set up Stripe webhooks

| bash                                        |
|---------------------------------------------|
| git add .                                   |
|---------------------------------------------|
| git commit -m "test1"                       |
|---------------------------------------------|
| Git push heroku main                        |
|---------------------------------------------|
| heroku run python manage.py migrate         |
|---------------------------------------------|







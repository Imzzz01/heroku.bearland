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

# Test Plan <a id="test-plan"></a>
  
   
# Code Implementation <a id="code-implementation"><a>



# Internal and External Code <a id="internal-and-external-code"></a>

Backend:


# Validation <a id="validation"></a>






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







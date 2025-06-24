from django.urls import path
from . import views
from .views import contact_view


app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'), # Home page
    path('products/', views.products, name='products'),  # Products list page
    path('gifts/', views.gifts, name='gifts'), # Gifts page
    path('product/<int:pk>/', views.product_detail, name='product_detail'), # Product detail page
    path('search/', views.search, name='search'), # Search functionality
    path('login/', views.login_view, name='login'),  # Login page
    path('contact/', contact_view, name='contact'),
   
]
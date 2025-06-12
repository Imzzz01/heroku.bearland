from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),  # Changed from 'product' to 'products'
    path('gifts/', views.gifts, name='gifts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),  # Keep this line
]
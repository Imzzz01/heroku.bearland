from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # User authentication URLs
    path('login/', views.login_view, name='login'), #login
    path('register/', views.register_view, name='register'), #register
    path('logout/', views.logout_view, name='logout'), #logout
]
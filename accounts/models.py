from django.contrib.auth.models import AbstractUser 
from django.db import models
from store.models import Product 

class CustomUser(AbstractUser): # Custom user model extending AbstractUser
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    

# This is to prevent clashes with auth.User
groups = models.ManyToManyField(
    'auth.Group',
    verbose_name='groups',
    blank=True,
    help_text='The groups this user belongs to.',
    related_name='customuser_set',
    related_query_name='customuser'
)
# This is the user permissions field
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
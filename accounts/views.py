# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages

User = get_user_model()

def login_view(request):
    """Handle user login with email/password"""
    if request.user.is_authenticated:
        return redirect('store:home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate using email as username
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.email}!')
            next_url = request.GET.get('next', 'store:home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'accounts/login.html')

def register_view(request):
    """Handle new user registration"""
    if request.user.is_authenticated:
        return redirect('store:home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
           
            authenticated_user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, f'Account created for {user.get_full_name()}!')
                return redirect('store:home')
            
            
        # Handle form errors
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    """Handle user logout"""
    if request.user.is_authenticated:
        # Clear all existing messages before logging out
        storage = get_messages(request)
        for message in storage:
            pass  # This clears the message queue
        
        logout(request)
        messages.success(request, 'You have been logged out.')
    return redirect('store:home')

@login_required
def account_view(request):
    """Display user account dashboard"""
    user = request.user
    context = {
        'user': user,
        'orders': user.orders.all()[:5] if hasattr(user, 'orders') else None
    }
    return render(request, 'accounts/account.html', context)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form extending Django's UserCreationForm

    Adds additional required fields (first_name, last_name, email) and custom validation
    uses email as the username automatically

    Attributes:
         first_name: Required text input with custom styling
         last_name: Required text input with custom styling 
         email: Required email input with validation
         password1: Password input with custom styling
         password2: Password confirmation input
    """

    # Form fields with custom widgets and attributes 
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auth-form-input'}),
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auth-form-input'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'auth-form-input'}),
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'auth-form-input'}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'auth-form-input'}),
        label="Confirm Password"
    )
    
    class Meta:
        """Metadata option for the form"""
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
    
    def clean_email(self):
        """
        Validate that the email is unique

        Returns:
            str: The validated email if unique
        Raises:
            ValidationError: If email already exists in database 
        """
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email
    
    def save(self, commit=True):
        """
        Save the user instance, using email as username

        Args: 
            commit: Whether to save to database immediately (default true)

        Returns:
            User: The created user instance

        """
        user = super().save(commit=False) # Create instance without saving
        user.username = self.cleaned_data['email']  # set username = email
        if commit:
            user.save() # save to database if commit=True
        return user
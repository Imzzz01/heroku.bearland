from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Custom user creation form
# This form is used to create a new user with username, email, and password fields.
# It inherits from Django's built-in UserCreationForm.
# The Meta class specifies the model and fields to be used in the form.
# The fields include 'username', 'email', 'password1', and 'password2'.
# 'password1' is the initial password input, and 'password2' is for password
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        
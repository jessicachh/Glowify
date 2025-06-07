# accounts/forms.py

from django import forms
from .models import CustomUser
from .models import BlogPost

class RegistrationForm(forms.ModelForm):
    # Add password field with PasswordInput widget for secure password entry
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser  # Use the CustomUser model for the form
        fields = ['username', 'email', 'password']  # Include username, email, and password


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image',  'content']
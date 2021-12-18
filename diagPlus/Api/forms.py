"""Customer form for user login"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Form Creation"""
    class Meta:
        """Meta"""
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    """Form Update"""
    class Meta:
        """Meta"""
        model = User
        fields = ('email',)

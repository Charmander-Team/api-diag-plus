"""Customer form for user login"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Admin


class CustomUserCreationForm(UserCreationForm):
    """Form Creation"""
    class Meta:
        """Meta"""
        model = Admin
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    """Form Update"""
    class Meta:
        """Meta"""
        model = Admin
        fields = ('email',)

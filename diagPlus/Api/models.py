"""Models Creation"""
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    first_name = models.CharField('First Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    email = models.EmailField(('Email address'), unique=True)
    address = models.TextField('Address')
    phone = PhoneNumberField()
    zip_code = models.CharField("ZipCode", max_length=10)
    city = models.CharField("City", max_length=123)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
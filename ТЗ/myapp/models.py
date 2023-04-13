from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager
from django.utils import timezone


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['email']

    objects = UserManager()


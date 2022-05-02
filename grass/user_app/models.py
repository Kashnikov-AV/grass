from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    @DynamicAttrs
    """

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField()
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'
        unique_together = ('username', 'email', 'phone')
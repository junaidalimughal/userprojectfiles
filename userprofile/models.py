from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length= 100, default="", null=False, blank=False)
    last_name = models.CharField(max_length= 100, default="", null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    date_of_birth = models.DateField(default=timezone.now)
    address = models.CharField(max_length=400, blank=False, null=False, default="")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['address', 'first_name', 'last_name']

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email



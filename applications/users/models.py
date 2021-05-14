from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from applications.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def get_short_name(self):
        return self.username

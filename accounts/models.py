from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserManager (BaseUserManager):
    def create_user (self, username, password=None, **extra_fields):
        if not username:
            raise ValueError ('The phone number must be set')
        user = self. model (username=username, **extra_fields)
        user.set_password (password)
        user.save(wing=self._db)
        return user
    def create_superuser (self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('type', 'S')
        return self.create_user(phone_number, password, **extra_fields)
class CustomUser(AbstractUser):
    USER_TYPE = (
        ('S', 'Superuser'),
        ('E', 'Employer'),
        ('C', 'Candidate'),
    )
    objects = UserManager
    REQUIRED_FIELDS = []
    type = models.CharField(choices=USER_TYPE, default='S', max_length=1)

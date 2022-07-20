from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    objects = CustomUserManager()

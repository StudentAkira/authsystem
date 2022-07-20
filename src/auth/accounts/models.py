from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    status = models.CharField(default='', max_length=127, blank=True, null=True)
    description = models.CharField(default='', max_length=511, blank=True, null=True)


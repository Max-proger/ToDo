from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField('email_address', unique=True, max_length=100)
    date_creation = models.DateTimeField(default=timezone.now)
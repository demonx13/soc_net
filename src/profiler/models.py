from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# class UserNet(AbstractUser):
#     """Custom user model"""
#     middle_name = models.CharField(max_length=50, null=True, blank=True)
#     first_login = models.DateField(null=True)
#     phone = models.CharField(max_length=14)
#     avatar = models.ImageField(upload_to="user/avatar", null=True, blank=True)

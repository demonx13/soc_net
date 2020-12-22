from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserNet(AbstractUser):
    """Custom user model
    """

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    middle_name = models.CharField(max_length=50, null=True, blank=True)
    first_login = models.DateField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to="user/avatar", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    """Technology model"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

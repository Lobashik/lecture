from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='book')

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Default user object with username, email and password"""
    username = models.charField(max_length=32, unique=True)
    email = models.charField(max_length=128, unique=True)

    def __str__(self):
        return self.username

class Wallet(models.Model):
    """Each wallet has an user asossiated with it"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.charField(max_length=64)
    balance = models.IntegerField(default=0)
    percent = models.PositiveSmallIntegerField(default=0, max_value=100)
    cap = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Wallet: {self.name} (${self.balance})'
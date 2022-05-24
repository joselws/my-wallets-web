from django.db import models
from django.contrib.auth.models import AbstractUser
from api.validators import validate_100_max


class User(AbstractUser):
    """Default user object with username, email and password"""
    username = models.CharField(max_length=32, unique=True)
    email = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.username

class Wallet(models.Model):
    """Each wallet has an user asossiated with it"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    balance = models.IntegerField(default=0)
    percent = models.PositiveSmallIntegerField(default=0, validators=[validate_100_max])
    cap = models.PositiveIntegerField(default=0)

    def clean_percent(self):
        """Only accept max values of 100"""
        if self.percent > 100:
            return ValidationError('Max number is 100')

    def __str__(self):
        return f'Wallet: {self.name} (${self.balance})'
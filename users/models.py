from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.

USER_TYPE_CHOICES = (('Business', 'Business'),
                        ('User', 'User'),)

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20,choices=USER_TYPE_CHOICES)

    isVerified = models.BooleanField(default=False)

    profile_picture = models.ImageField(blank=True, null=True)

    business_worth = models.BigIntegerField(blank=True, null=True)
    business_description = models.TextField(blank=True, null=True)
    available_shares = models.BigIntegerField(blank=True, null=True)
    total_shares = models.BigIntegerField(blank=True, null=True)
    buyable_shares = models.BigIntegerField(blank=True, null=True)
    buyable_shares_percentage = models.BigIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'username']

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.username


class EmailVerificationLogs(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    isUsed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email


class PasswordRecoveryLogs(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    isUsed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from uuid import uuid4

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# Defining energy sources

ENERGY_SOURCES = (
    ("Solar", "Solar"),
    ('Petroleum', 'Petroleum')
)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20)
    project_description = models.TextField(blank=True, null=True)
    energy_capacity = models.CharField(max_length=20)
    energy_source = models.CharField(choices=ENERGY_SOURCES, max_length=20)
    location = models.CharField(max_length=50)
    price = models.BigIntegerField()

    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.project_name


PAYMENT_STATUS = (('Pending', 'Pending'),
                  ('Failed', 'Failed'),
                  ('Done', 'Done'),)


TRANSACTION_TYPES = (('Investment', 'Investment'),
                     ('Project Payment', 'Project Payment'),)


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=PAYMENT_STATUS,
                              max_length=20, default='Pending')
    transaction_type = models.CharField(
        choices=TRANSACTION_TYPES, max_length=20, default='Project Payment')

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project


class Investment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_investing')
    business = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_invested_in')
    percentage_of_business = models.IntegerField(default=0)

    amount_invested = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + "investment"

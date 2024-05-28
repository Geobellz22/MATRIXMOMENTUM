from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    account_number = models.CharField(max_length=15, blank=True, null=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_worth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    investment_experience = models.TextField(blank=True, null=True)
    risk_tolerance = models.TextField(blank=True, null=True)
    identification_type = models.TextField(blank=True, null=True)
    identification_number = models.CharField(max_length=255, blank=True, null=True, unique=True)
    identification_expiry_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    social_media_links = models.TextField(blank=True, null=True)
    preferred_currency = models.CharField(max_length=255, blank=True, null=True)
    preferred_language = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Define custom related names for the groups and user_permissions fields
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

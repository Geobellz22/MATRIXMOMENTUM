from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
# Path: profiles/models.py
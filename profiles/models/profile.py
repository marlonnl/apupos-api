from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

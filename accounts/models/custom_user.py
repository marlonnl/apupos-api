from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = "username"  # e-mail is the default idenfication sign-in
    # REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ApupoLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apupo = models.ForeignKey("Apupo", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

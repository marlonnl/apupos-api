from django.db import models

# user
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Apupo(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True)

    class Meta:
        ordering = ["-id"]  # ordem descendente

    def __str__(self):
        return self.content

    def serialize(self):
        return {"id": self.id, "content": self.content, "likes": 10}

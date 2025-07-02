from django.db import models
from django.conf import settings

from .apupo_like import ApupoLike


User = settings.AUTH_USER_MODEL


class Apupo(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name="apupo_user", blank=True, through=ApupoLike
    )
    image = models.FileField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # for rt
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-id"]  # ordem descendente

    # def __str__(self):
    #     return self.content

    @property
    def is_retweet(self):
        return self.parent is not None

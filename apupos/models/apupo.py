from django.db import models
from django.conf import settings
from django.db.models import Q

from .apupo_like import ApupoLike


User = settings.AUTH_USER_MODEL


class ApupoQueryset(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles = user.following.exists()

        feed_users_id = []
        if profiles:
            # QS postagens de todos os usuário que o usuário segue pelo ID
            feed_users_id = user.following.values_list("user__id", flat=True)

        return (
            self.filter(Q(user__id__in=feed_users_id) | Q(user=user))
            .distinct()
            .order_by("-created_at")
        )


class ApupoManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ApupoQueryset(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)


class Apupo(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apupos")
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name="apupo_user", blank=True, through=ApupoLike
    )
    image = models.FileField(upload_to="images/", blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ApupoManager()

    class Meta:
        ordering = ["-id"]  # ordem descendente

    def __str__(self):
        return f"{self.content}"

    @property
    def is_retweet(self):
        return self.parent is not None

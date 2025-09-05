from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL
UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=80, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    image = models.FileField(upload_to="images/", blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    followers = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return f"{self.user}"


def saved_profile(sender, instance, created, *args, **kwargs):
    if created:
        # create a Profile to the new user
        Profile.objects.get_or_create(user=instance)

        # follows admin
        admin_profile = "apupos"
        to_follow = UserModel.objects.filter(username=admin_profile).first()
        profile = to_follow.profile

        profile.followers.add(instance)


post_save.connect(saved_profile, sender=User)

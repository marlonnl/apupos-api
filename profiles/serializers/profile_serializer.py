from rest_framework import serializers

from ..models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "username", "name", "bio", "site", "location"]

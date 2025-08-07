from django.conf import settings
from rest_framework import serializers

from profiles.serializers.profile_serializer import ProfileSerializer
from ..models.apupo import Apupo
from ..serializers import ApupoCreateSerializer

User = settings.AUTH_USER_MODEL


class ApupoSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = ApupoCreateSerializer(read_only=True)
    # user = UserSerializer()
    # user = serializers.SerializerMethodField(read_only=True)
    user = ProfileSerializer(source="user.profile", read_only=True)

    class Meta:
        model = Apupo
        fields = [
            "id",
            "user",
            "content",
            "likes",
            "is_retweet",
            "parent",
            "created_at",
        ]

    def get_likes(self, obj):
        return obj.likes.count()

    def get_content(self, obj):
        content = obj.content

        if obj.is_retweet:
            content = obj.parent.content

        return content

    def get_created_at(self, obj):
        return 2222

from django.conf import settings
from django.utils.timezone import localtime, now

from rest_framework import serializers

from profiles.serializers.profile_serializer import ProfileSerializer
from ..models.apupo import Apupo
from ..serializers import ApupoCreateSerializer

User = settings.AUTH_USER_MODEL


class ApupoSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = ApupoCreateSerializer(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    user = ProfileSerializer(source="user.profile", read_only=True)
    is_liked = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Apupo
        fields = [
            "id",
            "user",
            "content",
            "is_retweet",
            "parent",
            "created_at",
            "likes",
            "is_liked",
        ]

    def get_is_liked(self, obj):
        is_liked = False

        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        if user in obj.likes.all():
            is_liked = True

        return is_liked

    def get_likes(self, obj):
        return obj.likes.count()

    def get_content(self, obj):
        content = obj.content

        if obj.is_retweet:
            content = obj.parent.content

        return content

    def get_created_at(self, obj):
        delta = now() - obj.created_at
        seconds = delta.total_seconds()
        minutes = int(seconds // 60)
        hours = int(seconds // 3600)

        if seconds < 60:
            return "agora"
        elif minutes == 1:
            return "1min"
        elif minutes < 60:
            return f"{minutes}min"
        elif hours == 1:
            return "1h"
        elif hours < 24:
            return f"{hours}h"
        else:
            return localtime(obj.created_at).strftime("%d/%m/%Y %H:%M")

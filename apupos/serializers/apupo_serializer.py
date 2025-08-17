from datetime import datetime, timezone
import time

from django.conf import settings
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apupos.models.apupo_like import ApupoLike
from profiles.serializers.profile_serializer import ProfileSerializer
from ..models.apupo import Apupo
from ..serializers import ApupoCreateSerializer

User = settings.AUTH_USER_MODEL


class ApupoSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = ApupoCreateSerializer(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    # user = UserSerializer()
    # user = serializers.SerializerMethodField(read_only=True)
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
        post_date = obj.created_at
        now_date = datetime.now(timezone.utc)

        elapsed_timedelta = now_date - post_date

        return post_date.strftime("%H:%M:%S %d/%m/%y")

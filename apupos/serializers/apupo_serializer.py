from django.conf import settings
from rest_framework import serializers

from ..models.apupo import Apupo
from ..serializers import ApupoCreateSerializer


class ApupoSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    # content = serializers.SerializerMethodField(read_only=True)
    parent = ApupoCreateSerializer(read_only=True)

    class Meta:
        model = Apupo
        fields = ["id", "content", "likes", "is_retweet", "parent"]

    def get_likes(self, obj):
        return obj.likes.count()

    def get_content(self, obj):
        content = obj.content

        if obj.is_retweet:
            content = obj.parent.content

        return content

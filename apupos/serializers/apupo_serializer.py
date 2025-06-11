from django.conf import settings
from rest_framework import serializers

from ..models.apupo import Apupo


class ApupoSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Apupo
        fields = ["id", "content", "likes"]

    def get_likes(self, obj):
        return obj.likes.count()

    def get_content(self, obj):
        return obj.content

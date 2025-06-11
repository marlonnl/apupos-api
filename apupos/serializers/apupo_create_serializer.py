from django.conf import settings
from rest_framework import serializers

from ..models.apupo import Apupo


class ApupoCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Apupo
        fields = ["id", "content", "likes"]

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > settings.MAX_POST_LENGTH:
            raise serializers.ValidationError("This apupo is too long")
        return value

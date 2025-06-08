from django.conf import settings
from rest_framework import serializers

from ..models.apupo import Apupo


class ApupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apupo
        fields = ["content"]

    def validate_content(self, value):
        if len(value) > settings.MAX_POST_LENGTH:
            raise serializers.ValidationError("This apupo is too long")
        return value

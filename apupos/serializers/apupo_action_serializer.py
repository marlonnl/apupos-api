from django.conf import settings
from rest_framework import serializers


class ApupoActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        if value not in settings.ACTION_OPTIONS:
            raise serializers.ValidationError("Esta ação não é válida.")

        return value

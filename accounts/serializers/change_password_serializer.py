from rest_framework import serializers


class ChangePasswordSerializer(serializers.Serializer):
    oldpassword = serializers.CharField(required=True, write_only=True)
    newpassword = serializers.CharField(required=True, write_only=True)

    def validate_oldpassword(self, attrs):
        user = self.context["request"].user

        if not user.check_password(attrs):
            raise serializers.ValidationError("Incorrect actual password.")

        return attrs

    def validate_newpassword(self, attrs):
        password = attrs
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at lest 8 characters!")

        return attrs

    def create(self, validated_data):
        print("validated", validated_data["newpassword"])
        print("seelf", self.context["request"])
        # if validated_data["newpassword"] != validated_data["newpassword2"]:
        #     raise serializers.ValidationError("New passwords do not match")

        # password = validated_data["newpassword"]
        # validated_data.pop("newpassword2")

        # return validated_data
        return "oi"

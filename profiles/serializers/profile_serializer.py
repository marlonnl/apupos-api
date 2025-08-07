from rest_framework import serializers

from ..models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.SerializerMethodField(read_only=True)

    following_count = serializers.SerializerMethodField(read_only=True)
    followers_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "first_name",
            "bio",
            "site",
            "location",
            "following_count",
            "followers_count",
        ]

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_username(self, obj):
        return obj.user.username

    def get_following_count(self, obj):
        return obj.user.following.count()

    def get_followers_count(self, obj):
        return obj.followers.count()


# class ProfileSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source="user.username", read_only=True)

#     class Meta:
#         model = Profile
#         fields = ["id", "user", "username", "name", "bio", "site", "location"]


class ProfileSerializerLogin(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "username", "name", "bio", "site", "location"]


class FollowingSerializer(serializers.ModelField):
    class Meta:
        model = Profile

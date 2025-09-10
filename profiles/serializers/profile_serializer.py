from rest_framework import serializers

from ..models.profile import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.SerializerMethodField(read_only=True)

    following_count = serializers.SerializerMethodField(read_only=True)
    followers_count = serializers.SerializerMethodField(read_only=True)

    posts = serializers.SerializerMethodField(read_only=True)

    image = serializers.ImageField(use_url=True)

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
            "posts",
            "image",
        ]

    def get_posts(self, obj):
        # print(obj.user.apupos.count())
        return obj.user.apupos.count()

    def get_is_following(self, obj):
        is_following = False

        context = self.context
        request = context.get("request")
        # print(obj.followers.all())

        if request:
            user = request.user
            is_following = user in obj.followers.all()

        return is_following

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_username(self, obj):
        return obj.user.username

    def get_following_count(self, obj):
        return obj.user.following.count()

    def get_followers_count(self, obj):
        return obj.followers.count()


class FollowingSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField(read_only=True)
    followers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ["following", "followers"]

    def get_following(self, obj):
        context = self.context
        request = context.get("request")
        user = request.user

        # print(obj.user.following.all())

        following_list = []
        for userf in obj.user.following.all():
            # print(userf.user.username)
            following_list.append(userf.user.username)

        # print(following_list)
        return following_list

    def get_followers(self, obj):
        # data = serializers.Serializer(obj.followers.all().list())
        # print("followers:", obj.followers.all())
        followers_list = []
        for user in obj.followers.all():
            followers_list.append(user.username)

        return followers_list
        # return obj.followers.all()


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

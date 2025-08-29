import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers

from ..models.profile import Profile
from ..serializers.profile_serializer import FollowingSerializer, ProfileSerializer


@api_view(["GET"])
def profile_api_view(request, username, *args, **kwargs):
    queryset = Profile.objects.filter(user__username=username).first()

    if not queryset:
        return Response({"Profile": "perfil não existe."}, status=404)

    is_following = False
    follows_me = False

    if request.user.is_authenticated:
        user = request.user

        is_following = user in queryset.followers.all()
        follows_me = username in queryset.followers.all()

    # followers_test = FollowingSerializer(queryset.followers.all())

    # test_qs = Profile.objects.filter(user__username=username).first().followers.all()
    test_qs = request.user.following.values_list("user__username")

    # print(list(test_qs))

    followers_qs = queryset.followers.all()
    following_qs = user.following.all()

    serialized_followers = FollowingSerializer(queryset, context={"request": request})
    # serialized_following = FollowingSerializer(following_qs)

    # print("followers:", serialized_followers)
    # print("following:", serialized_following)

    serializer = ProfileSerializer(queryset, context={"request": request})

    data = {
        "username": username,
        "profile": serializer.data,
        "is_following": is_following,
        "follows_me": follows_me,
        "follow": serialized_followers.data,
    }

    return Response(data, status=200)

from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models.profile import Profile
from ..serializers.profile_serializer import ProfileSerializer


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

    serializer = ProfileSerializer(queryset)

    data = {
        "username": username,
        "profile": serializer.data,
        "is_following": is_following,
        "follows_me": follows_me,
    }

    return Response(data, status=200)

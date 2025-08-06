from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# from profiles.models.profile import Profile


User = get_user_model()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_view(request, username, *args, **kwargs):
    user = request.user
    to_follow = User.objects.filter(username=username).first()
    # to_follow = Profile.objects.filter(user__username=username).first()

    if not to_follow:
        return Response({"follow": f"usuário {username} não existe."}, status=404)

    profile = to_follow.profile

    data = request.data or {}

    action = data.get("action")

    if action == "follow":
        profile.followers.add(user)

    elif action == "unfollow":
        profile.followers.remove(user)

    follow_count = profile.followers.all()

    return Response({"follow": follow_count.count()}, status=200)

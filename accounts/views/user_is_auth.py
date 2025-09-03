from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from profiles.models.profile import Profile
from profiles.serializers.profile_serializer import ProfileSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def is_authenticated(request, *args, **kwargs):
    user = request.user
    queryset = Profile.objects.filter(user__username=user).first()

    if not queryset:
        return Response({"authenticated": "usuário não existe."}, status=404)

    serializer = ProfileSerializer(queryset, context={"request": request})

    data = {"authenticated": True, "user": serializer.data}

    return Response(data, status=200)

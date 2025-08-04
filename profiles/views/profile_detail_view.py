from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ..models.profile import Profile
from ..serializers.profile_serializer import ProfileSerializer

User = settings.AUTH_USER_MODEL


@api_view(["GET"])
def profile_detail_view(request, username, *args, **kwargs):
    queryset = Profile.objects.filter(user__username=username)

    if not queryset:
        return Response({"profile": "perfil não existe."}, status=404)

    serializer = ProfileSerializer(queryset, many=True)

    return Response(serializer.data[0])

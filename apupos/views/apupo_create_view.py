from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from ..serializers.apupo_serializer import ApupoSerializer


@api_view(["POST"])  # only POST method
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])  # se estiver autenticado, terá acesso a função
def apupo_create_view(request, *args, **kwargs):
    serializer = ApupoSerializer(data=request.POST)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)  # content=request.content
        return Response(serializer.data, status=201)

    return Response({}, status=400)

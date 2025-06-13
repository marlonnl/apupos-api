from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.apupo import Apupo
from ..serializers.apupo_action_serializer import ApupoActionSerializer
from ..serializers.apupo_serializer import ApupoSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apupo_action_view(request, *args, **kwargs):
    serializer = ApupoActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        apupo_id = data.get("id")
        action = data.get("action")
        content = data.get("content")

    queryset = Apupo.objects.filter(id=apupo_id)

    if not queryset.exists():  # caso o ID seja inválido
        return Response({}, status=404)

    obj = queryset.first()

    # Action logic
    if action == "like":
        obj.likes.add(request.user)
        serializer = ApupoSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == "unlike":
        obj.likes.remove(request.user)
    elif action == "rt":
        new_apupo = Apupo.objects.create(user=request.user, parent=obj, content=content)
        serializer = ApupoSerializer(new_apupo)
        return Response(serializer.data, status=200)

    return Response({}, status=201)

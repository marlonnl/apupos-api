from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.apupo import Apupo


@api_view(["DELETE", "POST"])
@permission_classes([IsAuthenticated])
def apupo_delete_view(request, apupo_id, *args, **kwargs):
    queryset = Apupo.objects.filter(id=apupo_id)

    if not queryset.exists():
        return Response({}, status=404)

    queryset = queryset.filter(user=request.user)

    if not queryset.exists():
        return Response(
            {"Message": "Você não pode deletar este apupo."}, status=401
        )  # sem permissão/ não é o usuário que postou

    obj = queryset.first()
    obj.delete()

    return Response({"Message": "Apupo deletado."}, status=201)

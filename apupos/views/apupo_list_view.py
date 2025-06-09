from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models.apupo import Apupo
from ..serializers.apupo_serializer import ApupoSerializer


@api_view(["GET"])  # only GET method
def apupo_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    """

    queryset = Apupo.objects.all()
    serializer = ApupoSerializer(
        queryset, many=True
    )  # many=True means the queryset has multiple items

    return Response(serializer.data)

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

    username = request.GET.get("username")  # url.. ?username={username}
    if username is not None:
        queryset = queryset.filter(user__username__iexact=username)

    serializer = ApupoSerializer(
        queryset, many=True
    )  # many=True means the queryset has multiple items

    # print(serializer.data)
    return Response(serializer.data)

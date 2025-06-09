from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..serializers.apupo_serializer import ApupoSerializer


@api_view(["POST"]) # only POST method
def apupo_create_view(request, *args, **kwargs):
    serializer = ApupoSerializer(data=request.POST)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)  # content=request.content
        return Response(serializer.data, status=201)

    return Response({}, status=400)

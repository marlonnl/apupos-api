from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import RegistrationSerializer


# TODO: first_name = username
class UserRegistrationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = RefreshToken.for_user(user)

        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}

        return Response(data, status=status.HTTP_201_CREATED)

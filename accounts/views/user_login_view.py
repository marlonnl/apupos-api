from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..serializers import UserLoginSerializer, UserSerializer


# @permission_classes([AllowAny])
class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        serializer = UserSerializer(user)

        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}

        res = Response()

        res.data = data
        res.set_cookie(
            key="accessToken",
            value=token.access_token,
            httponly=True,
            secure=True,
            samesite="None",
            path="/",
        )
        res.set_cookie(
            key="refreshToken",
            value=token,
            httponly=True,
            secure=True,
            samesite="None",
            path="/",
        )

        # print(data)

        return res
        # return Response(data, status=status.HTTP_200_OK)

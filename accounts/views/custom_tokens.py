from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from profiles.models.profile import Profile
from profiles.serializers.profile_serializer import (
    ProfileSerializer,
    ProfileSerializerLogin,
)

from ..serializers import UserSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # insere informações no access token (originalmente apenas user_id)
        token["username"] = user.username
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        user = request.data["username"]

        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens["access"]
            refresh_token = tokens["refresh"]

            qs = Profile.objects.filter(user__username=user).first()
            serializer_unfiltered = ProfileSerializer(qs)
            serializer = {"user": serializer_unfiltered.data}

            res = Response()
            res.data = response.data
            res.data = serializer
            res.set_cookie(
                key="accessToken",
                value=str(access_token),
                httponly=True,
                secure=True,
                samesite="None",
                path="/",
            )
            res.set_cookie(
                key="refreshToken",
                value=str(refresh_token),
                httponly=True,
                secure=True,
                samesite="None",
                path="/",
            )

            # res.cookies["accessToken"]["Partitioned"] = True
            # res.cookies["refreshToken"]["Partitioned"] = True

            res.data.update(tokens)
            return res

        except Exception as e:
            # print("Error: ", e)
            return Response({"Error": str(e)}, status=401)


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get("refreshToken")
            request.data["refresh"] = refresh_token

            response = super().post(request, *args, **kwargs)
            tokens = response.data
            access_token = tokens["access"]
            new_refresh_token = tokens["refresh"]

            res = Response()
            res.data = {"refreshed": True}
            res.set_cookie(
                key="accessToken",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="None",
                path="/",
            )

            res.set_cookie(
                key="refreshToken",
                value=new_refresh_token,
                httponly=True,
                secure=True,
                samesite="None",
                path="/",
            )

            return res

        except Exception as e:
            print("Erro: ", e)
            return Response({"refreshed": False})

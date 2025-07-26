from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from ..serializers import UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens["access"]
            refresh_token = tokens["refresh"]

            serializer = UserSerializer(request.user)  # many=True

            res = Response()
            res.data = {"success": True}
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

            res.data.update(tokens)
            return res

        except Exception as e:
            print("Error: ", e)
            return Response({"success": False})


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get("refreshToken")
            request.data["refresh"] = refresh_token

            response = super().post(request, *args, **kwargs)
            tokens = response.data
            access_token = tokens["access"]

            res = Response()
            res.data = {"refreshed": True}
            res.set_cookie(
                key="accessToken",
                value=str(access_token),
                httponly=True,
                samesite=None,
                path="/",
            )

            return res

        except Exception as e:
            print("Erro: ", e)
            return Response({"refreshed": False})

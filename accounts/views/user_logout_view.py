from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken


# class UserLogoutAPIView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, *args, **kwargs):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(status=status.HTTP_205_RESET_CONTENT)

#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get("refreshToken")
            token = RefreshToken(refresh_token)
            token.blacklist()

            res = Response()
            res.data = {"success": True}
            res.delete_cookie("accessToken", path="/", samesite="None")
            res.delete_cookie("refreshToken", path="/", samesite="None")

            # logout(request)
            return res

        except Exception as e:
            return Response({"success": False})

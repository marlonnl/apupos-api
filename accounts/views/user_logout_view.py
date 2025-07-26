from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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
            res = Response()
            res.data = {"success": True}
            res.delete_cookie("access_token", path="/", samesite="None")
            res.delete_cookie("refresh_token", path="/", samesite="None")

            return res

        except Exception as e:
            return Response({"success": False})

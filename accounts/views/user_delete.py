from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from accounts.models.custom_user import CustomUser
from accounts.serializers.user_serializer import UserSerializer


class DeleteAccount(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        username = request.user
        user = CustomUser.objects.filter(username=username).first()

        user.delete()

        return Response({"Delete account": "success"}, status=200)

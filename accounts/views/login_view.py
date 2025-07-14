# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import login, logout


# def login_view(request, *args, **kwargs):
#     form = AuthenticationForm(request, data=request.POST or None)
#     if form.is_valid():
#         user_ = form.get_user()
#         login(request, user_)
#         return redirect("/")

#     return render(request, "form.html", {"form": form})

from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken

# from .serializers import UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        # if user:
        #     refresh = RefreshToken.for_user(user)
        #     return Response({
        #         'refresh': str(refresh),
        #         'access': str(refresh.access_token),
        #         'user': UserSerializer(user).data
        #     })
        return Response({"error": "Invalid credentials."}, status=401)

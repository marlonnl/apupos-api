from django.urls import path

from .views import (
    user_login_view,
    user_logout_view,
    user_registration_view,
    user_info_view,
    user_is_auth,
    custom_tokens,
)

urlpatterns = [
    path(
        "token/",
        custom_tokens.CustomTokenObtainPairView.as_view(),
        name="token-obatin-pair",
    ),
    path(
        "token/refresh/",
        custom_tokens.CustomTokenRefreshView.as_view(),
        name="token-refresh",
    ),
    path("user/", user_info_view.UserInfoAPIView.as_view(), name="user-info"),
    # path("login/", user_login_view.UserLoginAPIView.as_view(), name="login-user"),
    path("logout/", user_logout_view.UserLogoutAPIView.as_view(), name="logout-user"),
    path("authenticated/", user_is_auth.is_authenticated, name="is-authenticated"),
    path(
        "register/",
        user_registration_view.UserRegistrationAPIView.as_view(),
        name="register-user",
    ),
]

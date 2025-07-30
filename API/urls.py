from django.contrib import admin
from django.urls import path, re_path, include

# from rest_framework_simplejwt import TokenObtainPairView, TokenRefreshView

from apupos.views import (
    home_view,
    apupo_detail_view,
    apupo_list_view,
    apupo_create_view,
    apupo_delete_view,
    apupo_action_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("apupos/", apupo_list_view),
    path("api/apupo/", include("apupos.urls")),
    path("api/auth/", include("accounts.urls")),
    path("api/profile/", include("profiles.urls")),
    # path("create-apupo", apupo_create_view),
    # path("apupo/<int:apupo_id>", apupo_detail_view),
    # path("api/apupo/<int:apupo_id>/delete", apupo_delete_view),
    # path("api/apupo/action", apupo_action_view),
]

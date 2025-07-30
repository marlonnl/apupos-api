from django.contrib import admin
from django.urls import path, include

from apupos.views import (
    home_view,
    apupo_list_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("apupos/", apupo_list_view),
    path("api/apupo/", include("apupos.urls")),
    path("api/auth/", include("accounts.urls")),
    path("api/profile/", include("profiles.urls")),
]

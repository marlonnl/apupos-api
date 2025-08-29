from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from apupos.views import (
    home_view,
    apupo_list_view,
)
from profiles.views import profile_update_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view),
    path("apupos/", apupo_list_view),
    path("api/apupo/", include("apupos.urls")),
    path("api/auth/", include("accounts.urls")),
    path("api/profile/", include("profiles.urls")),
    path("api/profile-update/", profile_update_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

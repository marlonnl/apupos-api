from django.urls import path

from .views import (
    apupo_action_view,
    apupo_create_view,
    apupo_delete_view,
    apupo_detail_view,
    apupo_list_view,
)

urlpatterns = [
    path("", apupo_list_view),
    path("create/", apupo_create_view),
    path("<int:apupo_id>/", apupo_detail_view),
    path("<int:apupo_id>/delete/", apupo_delete_view),
    path("action/", apupo_action_view),
]

# BASE ENDPOIT
# /api/apupo/
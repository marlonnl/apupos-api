from django.urls import path

from .views import profile_detail_view, follow_view, profile_api_view

urlpatterns = [
    # path("<str:username>/", profile_detail_view),
    path("<str:username>/", profile_api_view),
    path("<str:username>/follow/", follow_view),
    # path("<str:username>/update/", profile_update_view),
]

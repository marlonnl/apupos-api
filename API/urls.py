"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

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
    path("create-apupo", apupo_create_view),
    path("apupos/", apupo_list_view),
    path("apupo/<int:apupo_id>", apupo_detail_view),
    path("api/apupo/<int:apupo_id>/delete", apupo_delete_view),
    path("api/apupo/action", apupo_action_view),
]

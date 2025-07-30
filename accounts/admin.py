from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreateForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomAdminUser(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm

    model = CustomUser

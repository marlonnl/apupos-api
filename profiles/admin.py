from django.contrib import admin

from .models.profile import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["__str__", "name", "site"]
    list_filter = ["user", "name"]

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)

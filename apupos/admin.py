from django.contrib import admin

# Register your models here.
from .models.apupo import Apupo


class ApupoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "user"]
    search_fields = ["user__username", "user__email"]

    class Meta:
        model = Apupo


admin.site.register(Apupo, ApupoAdmin)

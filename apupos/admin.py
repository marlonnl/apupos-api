from django.contrib import admin

from .models.apupo import Apupo
from .models.apupo_like import ApupoLike


class ApupoLikeAdmin(admin.TabularInline):
    model = ApupoLike


class ApupoAdmin(admin.ModelAdmin):
    inlines = [ApupoLikeAdmin]
    list_display = ["__str__", "user"]
    search_fields = ["user__username", "user__email"]

    class Meta:
        model = Apupo


admin.site.register(Apupo, ApupoAdmin)

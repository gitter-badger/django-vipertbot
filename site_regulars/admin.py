from django.contrib import admin
from .models import Regular

class RegularModelAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at"]
    list_filter = ["user", "created_at", "updated_at"]
    search_fields = ["name", "user"]

    class Meta:
        model = Regular

# Register your models here.
admin.site.register(Regular, RegularModelAdmin)
from django.contrib import admin

from .models import Role

class RoleModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]

    class Meta:
        model = Role

# Register your models here.
admin.site.register(Role, RoleModelAdmin)

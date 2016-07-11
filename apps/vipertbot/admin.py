from django.contrib import admin
from .models.command import Command
from .models.regular import Regular
from .models.role import Role

# Register your models here.
class CommandModelAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at", "active"]
    list_filter = ["user", "created_at", "updated_at"]
    search_fields = ["name", "text", "user"]

    class Meta:
        model = Command

class RegularModelAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at"]
    list_filter = ["user", "created_at", "updated_at"]
    search_fields = ["name", "user"]

    class Meta:
        model = Regular

class RoleModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]

    class Meta:
        model = Role

admin.site.register(Role, RoleModelAdmin)
admin.site.register(Regular, RegularModelAdmin)
admin.site.register(Command, CommandModelAdmin)
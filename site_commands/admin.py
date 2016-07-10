from django.contrib import admin
from .models import Command

class CommandModelAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "created_at", "updated_at", "active"]
    list_filter = ["user", "created_at", "updated_at"]
    search_fields = ["name", "text", "user"]

    class Meta:
        model = Command

# Register your models here.
admin.site.register(Command, CommandModelAdmin)
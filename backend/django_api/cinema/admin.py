from django.contrib import admin
from cinema import models
from core.admin import BaseAdmin


@admin.register(models.Cinema)
class CinemaAdmin(BaseAdmin):
    list_display = ("name", "address")


@admin.register(models.Room)
class RoomAdmin(BaseAdmin):
    actions = ["generate_chairs_action"]
    list_display = ("number", "cinema")
    list_filter = ("cinema",)

    def generate_chairs_action(self, request, queryset):
        for room in queryset:
            room.generate_chairs()
        self.message_user(request, "Chairs generated successfully.")


@admin.register(models.Movie)
class MovieAdmin(BaseAdmin):
    list_display = ("title", "director")


@admin.register(models.Chair)
class ChairAdmin(BaseAdmin):
    list_display = ("code", "room", "status", "active")
    list_filter = ("room", "room__cinema", "active")

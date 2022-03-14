from django.contrib import admin
from cinema import models
from core.admin import BaseAdmin


@admin.register(models.Cinema)
class CinemaAdmin(BaseAdmin):
    list_display = ("name", "address")


@admin.register(models.Room)
class RoomAdmin(BaseAdmin):
    list_display = ("number", "cinema", "capacity")

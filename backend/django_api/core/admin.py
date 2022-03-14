from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

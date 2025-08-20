from django.contrib import admin
from .models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "is_done", "created_at", "deadline",)
    list_filter = ("is_done", "deadline", "tags")
    search_fields = ("content",)
    ordering = ("is_done", "-created_at")
    date_hierarchy = "created_at"
    readonly_fields = ("created_at",)
    list_per_page = 10

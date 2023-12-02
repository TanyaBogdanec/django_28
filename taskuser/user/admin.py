from django.contrib import admin
from .models import User, Task, Comment


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name_task", "date_creation", "date_completion")
    list_filter = ("name_task", "date_creation")
    search_fields = ("name_task", "description")


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("name", "email")
    search_fields = ("name", "email")


admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Task, TaskAdmin)

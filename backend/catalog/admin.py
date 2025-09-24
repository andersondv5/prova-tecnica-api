from django.contrib import admin
from .models import Course, Discipline

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course", "workload")
    list_filter = ("course",)
    search_fields = ("name",)


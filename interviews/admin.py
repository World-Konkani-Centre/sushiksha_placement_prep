from django.contrib import admin

from .models import Interview, GD


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(GD)
class GDAdmin(admin.ModelAdmin):
    pass


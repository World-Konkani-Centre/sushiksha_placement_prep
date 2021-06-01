from django.contrib import admin

from .models import Interview, GD, Branch


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(GD)
class GDAdmin(admin.ModelAdmin):
    pass

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


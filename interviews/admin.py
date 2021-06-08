from django.contrib import admin

from .models import Interview, GD, Branch


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'type', 'participant_1', 'start_time', 'end_time')
    list_display_links = ('id', 'branch', 'type')
    search_fields = ('branch', 'participant_1', 'type')
    list_filter = ('branch', 'type')
    # list_editable = ('branch',)
    # change_list_template = ''


@admin.register(GD)
class GDAdmin(admin.ModelAdmin):
    pass

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


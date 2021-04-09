from django.contrib import admin

from .models import Interview, GDParticipants, GDList


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(GDParticipants)
class GDParticipantsAdmin(admin.ModelAdmin):
    pass


@admin.register(GDList)
class GDAdmin(admin.ModelAdmin):
    pass

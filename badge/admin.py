from django.contrib import admin
from .models import BadgeCategory, Badge, Reward


@admin.register(BadgeCategory)
class BadgeCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    pass


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

# Register your models here.
from resume_builder.models import  Contact, Skill, Education, InternshipExperience, TrainingCertification, \
    Project, Extra, Language,  Achievement, Template, Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(InternshipExperience)
class InternshipExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainingCertification)
class TrainingCertificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass



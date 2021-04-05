from django.contrib import admin

# Register your models here.
from resume_builder.models import About, Contact, Skill, Education, InternshipExperience, TrainingCertification, \
    Project, Extra, Language, PersonalInterest, Achievement, Declaration,Template


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
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


@admin.register(PersonalInterest)
class PersonalInterestAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass



@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

# Register your models here.
from resume_builder.models import About,Contact,Skill,Education,Internship_Experience,Training_Certification,Project,Extra,Language,Personal_Interest,Achievement,Declaration,Other


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

@admin.register(Internship_Experience)
class InternshipExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Training_Certification)
class TrainingCertificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    pass


@admin.register(Personal_Interest)
class PersonalInterestAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass



@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):
    pass

@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    pass


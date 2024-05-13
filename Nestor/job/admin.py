from django.contrib import admin
from .models import Job, JobType, Application, hasSkills, hasEducation, hasExperience, hasReferences, FavoriteJob
# Register your models here.

admin.site.register(Job) 
admin.site.register(JobType) 
admin.site.register(Application) 
admin.site.register(hasSkills) 
admin.site.register(hasEducation) 
admin.site.register(hasExperience) 
admin.site.register(hasReferences)
admin.site.register(FavoriteJob)


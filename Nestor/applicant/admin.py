from django.contrib import admin
from .models import Experience, EducationLevel, Education, Applicant, References , CVExperience, CVSkills, CVEducation, CVReferences



admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(CVExperience)
admin.site.register(EducationLevel)
admin.site.register(References)
admin.site.register(Applicant)
admin.site.register(CVSkills)
admin.site.register(CVEducation)
admin.site.register(CVReferences)

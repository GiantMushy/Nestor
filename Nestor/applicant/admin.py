from django.contrib import admin
from .models import Experience, EducationLevel, Education, References, Applicant


admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(EducationLevel)
admin.site.register(References)
admin.site.register(Applicant)

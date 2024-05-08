from django.contrib import admin
from .models import Country, City, ZipCode, Skills, SkillGenre, JobCategory  
# Register your models here.


admin.site.register(Country)
admin.site.register(City)
admin.site.register(ZipCode)
admin.site.register(Skills)
admin.site.register(SkillGenre)
admin.site.register(JobCategory)

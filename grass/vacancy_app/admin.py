from django.contrib import admin
from .models import Vacancy
# Register your models here.
class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy
    list_display = ('job_name', 'company', 'created_at')
    


admin.site.register(Vacancy, VacancyAdmin)
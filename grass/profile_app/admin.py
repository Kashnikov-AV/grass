from django.contrib import admin
from .models import Profile, Company, Education, ExpJob
# Register your models here.


class ExpAdmin(admin.ModelAdmin):
    model = ExpJob
    list_display = ('pk', 'profile',)
    ordering = ('pk', )


admin.site.register(ExpJob, ExpAdmin)

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('pk', 'user',)
    list_filter = ('gender', 'birth_date')


admin.site.register(Profile, ProfileAdmin)


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('pk', 'company_name', 'region')
    list_filter = ('user', 'company_name',)

admin.site.register(Company, CompanyAdmin)


class EduAdmin(admin.ModelAdmin):
    model = Education
    list_display = ('pk',
                    'profile',
                    'edu_institution',
                    'speciality',
                    'level_of_education',
                    'year_of_start_edu',
                    'year_of_end_edu',
                    'diploma_certificate',
                    )


admin.site.register(Education, EduAdmin)
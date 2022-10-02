from django.contrib import admin

# Register your models here.
from .models import Profile, Company


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'name', 'surname', 'gender', 'birth_date', 'photo')
    list_filter = ('gender', 'birth_date')


admin.site.register(Profile, ProfileAdmin)


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = ('user', 'company_name', 'about_company')


admin.site.register(Company, CompanyAdmin)

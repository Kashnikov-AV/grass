from django.urls import path, include
from .views import CompanyVacancyListView, hx_create_company_vacancy_view, hx_delete_vacancy, VacancyListView, CompanyVacancyDetailView

urlpatterns = [
    path('company/<int:pk>/vacancies/', CompanyVacancyListView.as_view(), name='company-vacancies'),
    path('company/<int:pk>/add/', hx_create_company_vacancy_view, name='vacancy-add'),
    path('delete/<int:pk>/', hx_delete_vacancy, name='vacancy-delete'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', CompanyVacancyDetailView.as_view(), name='vacancy-detail'),
]
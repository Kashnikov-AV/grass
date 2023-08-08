from django.urls import path, include
from .models import Profile, Company, Education
from .views import (ProfileAboutMeUpdateView,
                    ProfileDetailView,
                    ProfileCompanyDetailView,
                    # ProfileCompanyUpdateView,
                    # hx_update_profile_aboutme_view,
                    hx_update_profile_education_add_view,
                    hx_create_profile_education_add_view,
                    # hx_update_company_contact_data_view,
                    # hx_update_profile_contact_data_view,
                    hx_delete_education,
                    hx_update_view,
                    ProfileEducationListView
                    )

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/update/<str:model>/<str:form>/', hx_update_view, name='hx-update'),
    path('<int:pk>/update/education/', ProfileEducationListView.as_view(), name='profile-education'),
    path('<int:pk>/update/education-add/', hx_create_profile_education_add_view, name='profile-education-add'),
    path('education/delete/<int:pk>/', hx_delete_education, name='education-delete'),
    path('<int:pk>/company/', ProfileCompanyDetailView.as_view(), name='profile-company'),
    ]

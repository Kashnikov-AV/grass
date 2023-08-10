from django.urls import path, include
from .models import Profile, Company, Education
from .views import (
                    ProfileDetailView,
                    ProfileCompanyDetailView,
                    hx_update_view,
                    hx_create_profile_education_add_view,
                    hx_delete_education,
                    ProfileEducationListView,
                    hx_delete_exp,
                    hx_create_profile_exp_add_view,
                    ProfileExpListView,
                    )

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/update/<str:model>/<str:form>/', hx_update_view, name='hx-update'), #update all modals

    path('<int:pk>/update/education/', ProfileEducationListView.as_view(), name='profile-education'),
    path('<int:pk>/update/education-add/', hx_create_profile_education_add_view, name='profile-education-add'),
    path('education/delete/<int:pk>/', hx_delete_education, name='profile-education-delete'),

    path('<int:pk>/update/exp/', ProfileExpListView.as_view(), name='profile-exp'),
    path('<int:pk>/update/exp-add/', hx_create_profile_exp_add_view, name='profile-exp-add'),
    path('exp/delete/<int:pk>/', hx_delete_exp, name='profile-exp-delete'),

    path('<int:pk>/company/', ProfileCompanyDetailView.as_view(), name='profile-company'),
    ]

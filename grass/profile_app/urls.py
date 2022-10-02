from django.urls import path, include
from .views import ProfileUpdateView, ProfileCompanyDetailView, ProfileDetailView, ProfileCompanyUpdateView

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('<int:pk>/company/', ProfileCompanyDetailView.as_view(), name='profile-company'),
    path('<int:pk>/company/update/', ProfileCompanyUpdateView.as_view(), name='profile-company-update'),
    ]

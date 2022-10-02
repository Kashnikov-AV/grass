from django.urls import path, include
from .views import VacancyCreateView, VacancyUpdateView, VacancyDeleteView

urlpatterns = [
    path('create/', VacancyCreateView.as_view(), name='vacancy-create'),
    path('<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy-update'),
    path('<int:pk>/delete/', VacancyDeleteView.as_view(), name='vacancy-delete'),
]
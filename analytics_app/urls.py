from django.urls import path, include
from django.views.generic import TemplateView, ListView
from .views import draw_charts

urlpatterns = [
    path('', draw_charts, name='analytic'),
]
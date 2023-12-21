from django.urls import path, include
from django.views.generic import TemplateView, ListView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name="analytics_app/analytics.html"), name='analytic'),
]
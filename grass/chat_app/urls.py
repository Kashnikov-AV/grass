from django.urls import path, include
from django.views.generic import TemplateView, ListView
from .views import chat

urlpatterns = [
    path('', chat, name='chat'),
]

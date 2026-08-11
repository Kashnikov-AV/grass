from django.urls import path, include
from django.views.generic import TemplateView, ListView
from .views import chat, chatPage

urlpatterns = [
    path('', chat, name='chat'),
    path('<str:email>/', chatPage, name='chat-page'),
]

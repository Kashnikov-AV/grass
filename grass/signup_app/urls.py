from django.urls import path
from .views import SignUpView, CustomLoginView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
]
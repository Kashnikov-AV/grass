from django.urls import path
from .views import CustomLoginView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, LoginForm


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
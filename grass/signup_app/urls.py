from django.urls import path
from .views import CustomLoginView, SignupWizardView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    # path()
]
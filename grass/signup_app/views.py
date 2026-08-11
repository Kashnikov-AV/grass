# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, LoginForm
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponse
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "signup_app/signup-full.html"


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "signup_app/login.html"

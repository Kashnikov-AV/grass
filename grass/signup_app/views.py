# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, LoginForm
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponse

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"


class SignupWizardView(SessionWizardView):
    form_list = [SignUpForm]
    template_name = 'registration/signup.html'

    def done(self, form_list, **kwargs):
        return HttpResponse('Form submitted')
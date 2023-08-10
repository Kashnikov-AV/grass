# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, LoginForm, SignUpForm1, SignUpForm2, SignUpForm3, SignUpForm4Company, SignUpForm4Profile
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


FORMS = [("role", SignUpForm1),
         ("email", SignUpForm2),
         ("pass", SignUpForm3),
         ("profile", SignUpForm4Profile),
         ("company", SignUpForm4Company),
         ]

TEMPLATES = {"role": 'signup_app/signup_1.html',
             "email": 'signup_app/signup_2.html',
             "pass": 'signup_app/signup_3.html',
             "profile": 'signup_app/signup_4_employer.html',
             "company": 'signup_app/signup_4_worker.html',
             }


class SignupWizardView(SessionWizardView):
    instance = None
    form_list = FORMS
    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = CustomUser
        return self.instance
    #
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_form_instance(self, step):
        return self.instance

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        data_for_step = self.get_cleaned_data_for_step('1')

        context = super().get_context_data(form=form, **kwargs)
        context.update({'extra': data_for_step})
        return context

    def done(self):
        return HttpResponse('Welldone!')


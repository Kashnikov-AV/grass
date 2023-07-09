from django.urls import path
from .views import CustomLoginView, SignupWizardView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, LoginForm, SignUpForm1, SignUpForm2, SignUpForm3, SignUpForm4Company, SignUpForm4Profile

FORMS = [("role", SignUpForm1),
         ("email", SignUpForm2),
         ("pass", SignUpForm3),
         ("profile", SignUpForm4Profile),
         ("company", SignUpForm4Company),
         ]



urlpatterns = [
    path("signup/", SignupWizardView.as_view(FORMS), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    #path("signup/", SignUpView.as_view(), name="signup"),
    # path()
]
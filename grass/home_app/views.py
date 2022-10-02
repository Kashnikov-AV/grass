from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from vacancy_app.models import Vacancy


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['vacancies'] = Vacancy.objects.all()
        return context

from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vacancy
from .forms import VacancyForm
from profile_app.models import Company
from django.urls import reverse_lazy


class VacancyCreateView(LoginRequiredMixin, CreateView):
    template_name = 'vacancy_app/vacancy_form.html'
    form_class = VacancyForm
    #success_url = reverse_lazy('profile-company', kwargs={'pk': self.user.pk})

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.company = Company.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        if kwargs != None:
            return reverse_lazy('profile-company', kwargs={'pk': self.request.user.pk})


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'vacancy_app/vacancy_form.html'
    form_class = VacancyForm
    model = Vacancy
    #success_url = reverse_lazy('profile-company', kwargs={'pk': self.request.user.pk})

    def get_success_url(self, **kwargs):
        if kwargs != None:
            return reverse_lazy('profile-company', kwargs={'pk': self.request.user.pk})


class VacancyDetailView(LoginRequiredMixin, DetailView):
    pass


class VacancyListView(LoginRequiredMixin, ListView):
    pass


class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    model = Vacancy
    #success_url = 'profile-company'

    def get_success_url(self, **kwargs):
        if kwargs != None:
            return reverse_lazy('profile-company', kwargs={'pk': self.request.user.pk})

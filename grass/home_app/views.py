from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Create your views here.
class HomeView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'home'
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

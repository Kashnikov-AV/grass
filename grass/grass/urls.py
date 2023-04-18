"""grass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT
from profile_app.views import CompanyListView, ProfileListView
# from chat_app.views import UsersListView
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView, ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('signup_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('home/', include('home_app.urls')),
    path('home/', TemplateView.as_view(template_name="coming-soon.html"), name='coming'),
    path('', RedirectView.as_view(url='home/')),
    path('profile/', include('profile_app.urls')),
    path('companies/', CompanyListView.as_view(), name='companies'),
    path('profiles/', ProfileListView.as_view(), name='profiles'),
    path('vacancy/', include('vacancy_app.urls')),
    path('coming-soon/', TemplateView.as_view(template_name="coming-soon.html"), name='coming'),
    # path('chat/', include()),
    # path('chat/users/', UsersListView.as_view(), name='users_list'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

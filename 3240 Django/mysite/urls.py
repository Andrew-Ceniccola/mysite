"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('projects/', include('projects.urls')),
    path('skills/', include('skills.urls')),
    path('experiances/', include('experiances.urls')),


    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    # iff favicon acts up add this line from 
    # https://simpleit.rocks/python/django/django-favicon-adding/
]

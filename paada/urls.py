"""paada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from ajax_select import urls as ajax_select_urls

from core.views import ResponsaveisAutoComplete, UsuariosAutoComplete,\
    AnosLetivosAutoComplete, ProfessoresAutoComplete, TurmasAutoComplete

urlpatterns = [
    url(r'^paada_admin/', admin.site.urls),

    url(r'^ajax_select/', include(ajax_select_urls)),

    url('^login/', auth_views.login, {'template_name': 'core/login.html'}, name="login_url"),
    url('^logout/', auth_views.logout_then_login, name="logout_url"),

    url('^',  include('core.urls', namespace="core")),

    url(r'^responsaveis-autocomplete/$', ResponsaveisAutoComplete.as_view(),
    name="responsaveis-autocomplete"),
    url(r'^usuarios-autocomplete/$', UsuariosAutoComplete.as_view(),
    name="usuarios-autocomplete"),
    url(r'^anosletivos-autocomplete/$', AnosLetivosAutoComplete.as_view(),
    name="anosletivos-autocomplete"),
    url(r'^professores-autocomplete/$', ProfessoresAutoComplete.as_view(),
    name="professores-autocomplete"),
    url(r'^turmas-autocomplete/$', TurmasAutoComplete.as_view(),
    name="turmas-autocomplete"),
]

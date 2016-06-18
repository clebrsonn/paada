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

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^escolher_disciplina/$', views.escolher_disciplina, name="escolher_disciplina"),
    url(r'^alunos_disciplina/(?P<disciplina_id>[0-9]+)/$', views.alunos_disciplina,
        name="alunos_disciplina"),
    url(r'^adicionar_notas/(?P<disciplina_id>[0-9]+)/(?P<aluno_id>[0-9]+)/$',
        views.adicionar_notas, name="alunos_disciplina"),
    url(r'^acompanhamento_academico/', views.acompanhamento_academico,
        name="acompanhamento_academico"),
    url(r'^boletim_escolar/(?P<aluno_id>[0-9]+)/$', views.boletim_escolar,
        name="boletim_escolar"),
    url(r'^boletim_escolar/(?P<aluno_id>[0-9]+)/(?P<ano_letivo>[0-9]+)$', views.boletim_escolar,
        name="boletim_escolar"),
    url(r'^historico_escolar/(?P<aluno_id>[0-9]+)/$', views.historico_escolar,
        name="historico_escolar"),
    url(r'^mensagem_pais/$', views.mensagem_pais, name="mensagem_pais"),
    url(r'^agenda_virtual_professor/$', views.agenda_virtual_professor1,
        name="agenda_virtual_professor1"),
    url(r'^escrever_nota_agenda_virtual/(?P<disciplina_id>[0-9]+)/$',
        views.escrever_nota_agenda_virtual, name="escrever_nota_agenda_virtual"),

    url(r'^agenda_virtual_pai/(?P<aluno_id>[0-9]+)/$',
        views.agenda_virtual_pai, name="agenda_virtual_pai"),
    url(r'^show_nota_agenda/(?P<disciplina_id>[0-9]+)/$',
        views.show_nota_agenda, name="show_nota_agenda"),
]
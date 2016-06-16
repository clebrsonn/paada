# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib import messages
from django.utils import timezone


from .autocomplete_views import * # importando Autocompletes
from .models import Disciplina, Aluno, Notas
from .forms import NotasForm, NotasAgendaForm

@login_required
def home(request):
    user_group = request.user.groups.first()
    if user_group.name == "pais":
        return redirect(reverse("acompanhamento_academico",urlconf="core.urls"))
    elif user_group.name == "professores":
        return redirect(reverse("escolher_disciplina",urlconf="core.urls"))
    elif user_group.name == "Administrador":
        return redirect("/paada_admin")


@login_required
def escolher_disciplina(request):
    professor = request.user.professor
    disciplinas = professor.disciplinas.all()
    context = RequestContext(request,{'disciplinas': disciplinas})
    return render(request, "core/escolher_disciplina.html", context)


@login_required
def alunos_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    alunos = disciplina.turma.alunos.all()
    context = RequestContext(request,{'disciplina': disciplina, 'alunos': alunos})
    return render(request, "core/alunos_disciplina.html", context)


@login_required
def adicionar_notas(request, disciplina_id, aluno_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)
    aluno = Aluno.objects.get(pk=aluno_id)
    notas, created = Notas.objects.get_or_create(aluno=aluno,disciplina=disciplina)

    if request.POST:
        form = NotasForm(request.POST, instance=notas)
        if form.is_valid():
            form.save()
            mensagem = "Notas de {nome_aluno} salvas com sucesso".format(
                nome_aluno=aluno.nome)
            messages.add_message(request,messages.SUCCESS, mensagem,
                                 extra_tags='dragonball')
            return redirect("core:alunos_disciplina", disciplina_id=disciplina.pk)
    else:
        form = NotasForm(instance=notas)

    context = RequestContext(request,{'disciplina': disciplina, 'aluno': aluno,
                                      'form':form})
    return render(request, "core/adicionar_notas.html", context)


def acompanhamento_academico(request):
    responsavel = request.user.responsavel
    alunos = responsavel.alunos.all()

    context = RequestContext(request,{'alunos': alunos})
    return render(request, "core/acompanhamento_academico.html", context=context)


def boletim_escolar(request, aluno_id, ano_letivo=None):
    aluno = Aluno.objects.get(pk=aluno_id)

    if ano_letivo is None:
        ano = timezone.now().year
        ano_letivo = AnoLetivo.objects.get(data_criacao__year=ano)
    else:
        ano_letivo = AnoLetivo.objects.get(pk=int(ano_letivo))
        ano = ano_letivo.data_criacao.year

    notas = Notas.objects.filter(
        disciplina__turma__ano_letivo__data_criacao__year=ano, aluno=aluno)
    context = RequestContext(request,{'notas': notas, "aluno":aluno,
                                      "ano_letivo":ano_letivo})
    return render(request, "core/boletim_escolar.html", context=context)


def historico_escolar(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    anos_letivos = AnoLetivo.objects.all()

    context = RequestContext(request,{"aluno":aluno, "ano_letivos":anos_letivos})
    return render(request, "core/historico_escolar.html", context=context)


def agenda_virtual_professor1(request):
    professor = request.user.professor
    disciplinas = professor.disciplinas\
        .filter( turma__ano_letivo__data_criacao__year=timezone.now().year)

    context = RequestContext(request,{"disciplinas":disciplinas})
    return render(request, "core/agenda_virtual_professor_escolher_disciplina.html",
                  context=context)


def escrever_nota_agenda_virtual(request, disciplina_id):
    disciplina = Disciplina.objects.get(pk=disciplina_id)

    if request.POST:
        form = NotasAgendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,u"Notificação na Agenda "
                                                          "Virtual criada com Sucesso!",
                                 extra_tags='agenda_virtual')
            return redirect(reverse("agenda_virtual_professor1",urlconf="core.urls"))
    else:
        form = NotasAgendaForm()

    context = RequestContext(request,{"disciplina":disciplina,  "form":form})
    return render(request, "core/escrever_agenda_virtual.html", context=context)


def mensagem_pais(request):
    return render(request, "core/mensagens_pais.html")

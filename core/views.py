from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib import messages
from django.utils import timezone


from .autocomplete_views import * # importando Autocompletes
from .models import Disciplina, Aluno, Notas
from .forms import NotasForm

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

def boletim_escolar(request, aluno_id):
    responsavel = request.user.responsavel
    aluno = Aluno.objects.get(pk=aluno_id)
    notas = Notas.objects.filter(
        disciplina__turma__ano_letivo__data_criacao__year=timezone
                              .now().year, aluno=aluno)
    ano_letivo = AnoLetivo.objects.get(data_criacao__year=timezone.now().year)
    context = RequestContext(request,{'notas': notas, "aluno":aluno,
                                      "ano_letivo":ano_letivo})
    return render(request, "core/boletim_escolar.html", context=context)
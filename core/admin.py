# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import AnoLetivo, Professor, Responsavel, Aluno, Disciplina, Turma

from .forms import AnoLetivoForm, AlunoForm, ProfessorForm, ResponsavelForm, TurmaForm,\
    DisciplinaForm


@admin.register(AnoLetivo)
class AnoLetivoAdmin(admin.ModelAdmin):
    date_hierarchy = u"data_criacao"
    empty_value_display = u"Não existe anos letivos cadastrados."

    form = AnoLetivoForm


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    form = ProfessorForm
    pass


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    search_fields = (u"nome",)
    form = ResponsavelForm


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (u"nome",)
    form = AlunoForm


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    search_fields = (u"nome_disciplina", u"professor", u"turma")
    form = DisciplinaForm


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    search_fields = (u"nome_turma", u"ano_letivo")
    form = TurmaForm
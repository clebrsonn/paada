# -*- coding: utf-8 -*-

from django.contrib import admin
from ajax_select import make_ajax_form

from .models import AnoLetivo, Professor, Responsavel, Aluno
from .forms import AnoLetivoForm


@admin.register(AnoLetivo)
class AnoLetivoAdmin(admin.ModelAdmin):
    date_hierarchy = u"data_criacao"
    empty_value_display = u"Não existe anos letivos cadastrados."

    form = AnoLetivoForm


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    search_fields = (u"nome",)
    pass


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (u"nome", u"adicionar_nota")

    form = make_ajax_form(Aluno, {
        u"responsavel": u"responsavel"
    })
    class Media:
        # customização da tela de inserção e edição de alunos
        css = {
            u"all": (u"core/css/aluno.css",)
        }

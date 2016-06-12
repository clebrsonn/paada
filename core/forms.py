# -*- coding: utf-8 -*-

from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from dal.autocomplete import ModelSelect2
from .models import AnoLetivo, Aluno, Responsavel,Professor, Turma, Disciplina


class AnoLetivoForm(forms.ModelForm):
    """Form para adição de novos anos letivos."""

    def __init__(self, *args, **kwargs):
        super(AnoLetivoForm, self).__init__(*args,**kwargs)
        self.fields[u'titulo'].initial = datetime.now().year
        self.fields[u'titulo'].widget.attrs[u'readonly'] = True

    class Meta:
        model = AnoLetivo
        fields = [u'titulo']


class AlunoForm(forms.ModelForm):
    responsavel = forms.ModelChoiceField(
        queryset= Responsavel.objects.all(),
        widget=ModelSelect2(url='responsaveis-autocomplete')
    )

    class Meta:
        model = Aluno
        fields = ('__all__')

class ResponsavelForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=ModelSelect2(url='usuarios-autocomplete')
    )
    class Meta:
        model = Responsavel
        fields = ('__all__')

class ProfessorForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=ModelSelect2(url='usuarios-autocomplete')
    )
    class Meta:
        model = Professor
        fields = ('__all__')


class TurmaForm(forms.ModelForm):
    ano_letivo = forms.ModelChoiceField(
        queryset=AnoLetivo.objects.all(),
        widget=ModelSelect2(url='anosletivos-autocomplete')
    )
    class Meta:
        model = Turma
        fields = ('__all__')


class DisciplinaForm(forms.ModelForm):
    turma = forms.ModelChoiceField(
        queryset=Turma.objects.all(),
        widget=ModelSelect2(url='turmas-autocomplete')
    )

    professor = forms.ModelChoiceField(
        queryset=Professor.objects.all(),
        widget=ModelSelect2(url='professores-autocomplete')
    )
    class Meta:
        model = Disciplina
        fields = ('__all__')
